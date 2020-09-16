# raspberry-sensors-firebase

# clone repo and install dependencies
    cd home/pi/Documents/
    git clone https://github.com/HugoJBello/raspberry-sensors-firebase.git

# prerequisites install libraries nvm y pipenv
   
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    sudo npm install pm2@latest -g
    
    sudo apt-get install libffi6 libffi-dev
    sudo apt-get install pipenv
    
    cd home/pi/Documents/raspberry-sensors-firebase
    pipenv install
    
  
# add .env with firebase config and other configs
    nano .env
    
add this contents:

    firebase_config_json_token= ...
    sensor_id=sensor_test
    device_id=device_test
  
# add script on startup
    sudo nano /home/pi/.bashrc
add the line    
    
    cd ~/Documents/raspberry-sensors-firebase; bash start.sh


# (optional) docker
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker pi 
    sudo apt-get install docker-compose
