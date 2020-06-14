#!/bin/sh

echo "start entrypoint..."
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    sleep 0.5
    echo "PostgreSQL started"
fi

# python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic --no-input --clear

exec "$@"
