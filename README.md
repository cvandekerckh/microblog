# microblog
Flask script for website 

# Step 0 : download elastic search
instructions for MAC :
https://medium.com/@felixgondwe/elasticsearch-setup-using-homebrew-2017891f62bb
commands:
- `brew install elasticsearch`
- `brew services start elasticsearch`
- test : http://localhost:9200

# Step 1 : setting up gmail for password reset
# create .env file and set environment the following ENV variable
export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-email>
export MAIL_PASSWORD=<your-gmail-password>
export MS_TRANSLATOR_KEY=<your-azur-translator-key>
export ELASTICSEARCH_URL=http://localhost:9200

# Step 2 : allow you gmail account to send emails
click on https://myaccount.google.com/lesssecureapps and  unlock

# Step 3: setting up virtual environment
- setting the right python version using pyenv
- running `pipenv install`

# Step 4 : running flask
- running `flask run`

# Step 5 : ssh connect to instance and prepare environment
`ssh -i ~/.ssh/gc corentinvdk@104.155.161.68`

(protect your instance : https://blog.miguelgrinberg.com/)

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

sudo apt-get install git

curl https://pyenv.run | bash

(following instruction)

reload shell

pyenv install --list | grep " 3\.[678]"

pyenv install -v 3.7.2
