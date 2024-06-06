web: gunicorn FetcherApp.wsgi --log-file -
worker: celery -A FetcherApp worker --loglevel=info