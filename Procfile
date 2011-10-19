web: bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT bookere/settings.py
worker: bin/python bookere/manage.py celeryd -E -B --loglevel=INFO
