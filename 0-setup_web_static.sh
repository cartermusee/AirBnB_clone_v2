#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get -y update
  sudo apt-get -y install nginx
fi
sudo ufw allow 'Nginx HTTP'

if [ ! -d /data/ ]; then
    mkdir -p /data
fi

if [ ! -d /data/web_static/ ]; then
    mkdir -p /data/web_static/
fi

if [ ! -d /data/web_static/releases/ ]; then
    mkdir -p /data/web_static/releases/
fi

if [ ! -d /data/web_static/shared/ ]; then
    mkdir -p /data/web_static/shared/
fi

if [ ! -d /data/web_static/releases/test/ ]; then
    mkdir -p /data/web_static/releases/test/
fi

if [ ! -d /data/web_static/releases/test/ ]; then
    mkdir -p /data/web_static/releases/test/
fi

echo "<html>
  <head>
  </head>
  <body>
     Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

current="/data/web_static/current"
test_t="/data/web_static/releases/test"

sudo ln -s -f "$test_t" "$current"
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
sudo service nginx restart
