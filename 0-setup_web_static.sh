#!/usr/bin/env bash
# Prepare your web servers:
apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Nginx Works Fine" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -Rh ubuntu:ubuntu /data/
printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;

	root /var/www/html;

	location /hbnb_static {
                alias /data/web_static/current/;
        }
        index index.html index.htm index.nginx-debian.html;

	error_page 404 /404.html;

	add_header X-Served-By $HOSTNAME always;

	location /redirect_me {
                error_page 404 =301 https://www.youtube.com;
        }
}" > /etc/nginx/sites-available/default
service nginx restart
