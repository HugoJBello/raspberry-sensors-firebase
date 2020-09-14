# raspberry-sensors-firebase

# prerequisites
   

    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
    export NVM_DIR="$HOME/.nvm"
    sudo npm install pm2@latest -g
    
    sudo apt-get install libffi6 libffi-dev
    sudo apt-get install pipenv
    pip3 install -r requirements.txt
    
    
    
    pipenv run pip freeze > requirements.txt

# optional
    curl -sSL https://get.docker.com | sh
    sudo usermod -aG docker pi 
    sudo apt-get install docker-compose

# on startup
    sudo nano /home/pi/.bashrc
add the line    
    
    cd ~/Documents/raspberry-sensors-firebase; bash start.sh