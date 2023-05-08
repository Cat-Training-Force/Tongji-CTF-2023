FROM ctftraining/base_image_nginx_mysql_php_56

COPY src /var/www/html
COPY src/flag.sh /flag.sh

RUN chmod +x /flag.sh && \
    chown -R www-data:www-data /var/www/html

CMD ["/flag.sh"]
