FROM praekeltfoundation/django-bootstrap
ENV DJANGO_SETTINGS_MODULE "ndoh_hub.settings"
RUN ./manage.py collectstatic --noinput
ENV APP_MODULE "ndoh_hub.wsgi:application"
