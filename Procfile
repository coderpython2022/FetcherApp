release: python manage.py migrate
web: gunicorn FetcherApp.wsgi
web: python manage.py runserver 0.0.0.0:\$PORT