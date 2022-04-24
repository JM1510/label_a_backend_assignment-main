web: gunicorn autocompany.wsgi
release: sh -c 'python manage.py makemigrations && python manage.py collectstatic && python manage.py migrate --noinput'

