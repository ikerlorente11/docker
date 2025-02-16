# Use the official PHP image as the base image
FROM php:8.1-fpm

USER root
ENV COMPOSER_ALLOW_SUPERUSER=1

# Set the working directory in the container
WORKDIR /var/www/html

# Install dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libicu-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip

# Install PHP extensions
RUN docker-php-ext-enable opcache
RUN pecl install apcu && docker-php-ext-enable apcu
RUN docker-php-ext-configure gd --enable-gd --with-freetype --with-jpeg
RUN docker-php-ext-install pdo pdo_mysql mbstring exif pcntl bcmath gd intl

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Set the container user to non-root
RUN chmod -R 777 /var/www/html

# Expose port 9000 and start the PHP-FPM server
EXPOSE 9000
CMD ["php-fpm"]