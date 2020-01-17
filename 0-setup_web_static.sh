#!/usr/bin/env bash
# bash script that sets up web servers for web_static deployment
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

SETUP_TEST="<html>
<head>
</head>
<body>
 HBNB Deployment Configuration
</body>
<html>"
echo "$SETUP_TEST" | sudo tee /data/web_static/releases/test/index.html

# symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

D_Config=https://raw.githubusercontent.com/rcolbert30/AirBnB_clone_v2/master/default
D_File=/etc/nginx/sites-available/default
sudo wget $D_Config -O $D_File

sudo service nginx reload
sudo service nginx restart
