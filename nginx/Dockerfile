FROM nginx:latest

RUN mkdir -p /var/www/staticfiles/

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
