web: gunicorn FetcherApp.wsgi --log-file -
web: bundle exec rails server -p $PORT
web: java -jar target/FetcherApp-1.0.0.jar