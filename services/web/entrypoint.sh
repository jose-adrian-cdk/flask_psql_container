#!/bin/sh

# hay que darle permisos de ejecución 
# chmod +x entrypoint.sh

if ["$DATABASE" = "postgres"]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py create_db

exec "$@"
