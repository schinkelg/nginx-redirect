# Nginx redirection generator

This script is a convenient way to generate Nginx vhosts for the single purpose of redirecting users to different sites / URLs. It supports Letsencrypt webroot certificate authentication.

It needs at least Python version 3.6, but works with anything newer.

## Usage

```
$> python3 nginx-redirect.py < example.txt

# Auto-generated file. Please don't make changes to this file, they will be overwritten.
server { listen 80; listen [::]:80; server_name example1.com sub.example1.com; root /var/www/html; location /.well-known/ {try_files $uri =404;} location / {return 302 https://sub.example1.com/login;}}
server { listen 80; listen [::]:80; server_name test-123.example2.com; root /var/www/html; location /.well-known/ {try_files $uri =404;} location / {return 302 https://this-does-not-even-exist.com/;}}
```
