#!/bin/bash

if [ ! -d vendor ]; then
    composer install --no-dev --no-interaction --optimize-autoloader
    cp .env.example .env
    php artisan key:generate
    php artisan migrate --seed --force
fi

php-fpm