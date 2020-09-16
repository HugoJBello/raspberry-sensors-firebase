curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
export NVM_DIR="$HOME/.nvm"
sudo npm install pm2@latest -g

sudo apt-get install libffi6 libffi-dev
sudo apt-get install pipenv

cd home/pi/Documents/raspberry-sensors-firebase
pipenv install
