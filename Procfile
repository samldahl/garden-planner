web: gunicorn --chdir gardenPlanner gardenPlanner.wsgi
release: python gardenPlanner/manage.py migrate --noinput && python gardenPlanner/manage.py collectstatic --noinput
