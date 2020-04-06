# Microblog
Flask script for website 

# A. Development preparation
##  Step 0 : download elastic search
instructions for MAC :
https://medium.com/@felixgondwe/elasticsearch-setup-using-homebrew-2017891f62bb
commands:
- `brew install elasticsearch`
- `brew services start elasticsearch`
- test : http://localhost:9200

##  Step 1 : setting up gmail for password reset
Create .env file and set environment the following ENV variable

export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME=<your-gmail-email>
export MAIL_PASSWORD=<your-gmail-password>
export MS_TRANSLATOR_KEY=<your-azur-translator-key>
export ELASTICSEARCH_URL=http://localhost:9200

## Step 2 : allow you gmail account to send emails
click on https://myaccount.google.com/lesssecureapps and  unlock

##  Step 3: setting up virtual environment
- setting the right python version using pyenv
- running `pipenv install`

## Step 4 : running flask
- running `flask run`

# Production Details
##  Step 1 : ssh connect to instance and prepare environment
`ssh -i ~/.ssh/gc corentinvdk@104.155.161.68`
(protect your instance : https://blog.miguelgrinberg.com/)

## Step 2 : install environment
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
sudo apt-get install git
curl https://pyenv.run | bash
(following instruction)
reload shell
pyenv install --list | grep " 3\.[678]"
pyenv install -v 3.7.2
sudo apt-get update
sudo apt-get -y install mysql-server postfix supervisor nginx git
Internet Configuration for postfix
pip install -U pipenv

# Step 3 : prepare .env
SECRET_KEY=(gen by python -c "import uuid; print(uuid.uuid4().hex)")
MAIL_SERVER=localhost
MAIL_PORT=25
DATABASE_URL=mysql+pymysql://microblog:<db-password>@localhost:3306/microblog
MS_TRANSLATOR_KEY=<your-translator-key-here>

# Step 4 : prepare languages
flask translate compile

# Step 5 : set up db
setting up db
mysql -u root -p
mysql> create database microblog character set utf8 collate utf8_bin;
mysql> create user 'microblog'@'localhost' identified by 'sZQ9NdjghCGykLwaWjPyfQUu';
mysql> grant all privileges on microblog.(star) to 'microblog'@'localhost';
mysql> flush privileges;
mysql> quit;

if issues :
USE mysql;
CREATE USER 'debian'@'localhost' IDENTIFIED BY '';
GRANT ALL PRIVILEGES ON *.* TO 'debian'@'localhost';
UPDATE user SET plugin='unix_socket' WHERE User='debian';

# Step 6 : deploy
gunicorn file:
[program:microblog]
command=/home/ubuntu/microblog/venv/bin/gunicorn -b localhost:8000 -w 4 microblog:app
directory=/home/ubuntu/microblog
user=ubuntu
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true
where gunicorn is referenced from virtualenv

useful commands:
sudo supervisorctl status all
sudo supervisorctl reload
sudo vim /etc/nginx/sites-enabled/microblog
sudo nginx -c /etc/nginx/nginx.conf -t
sudo service nginx reload
service nginx status

# Step 7 : get certificate using certbot
see tutorial. If issues:
sudo apt-get install dirmngr
sudo certbot certonly --webroot -w /home/debian/microblog/app/static -d thementaldoctors.com

# Step 8 : misc

checking storage remaining:
df -H /dev/sda1
allow https on compute :)


