#!/bin/bash

chmod -R 777 /var/www/html

php-fpm -D
nginx -g "daemon off;"