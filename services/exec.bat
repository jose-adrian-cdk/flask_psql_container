set DATABASE_URL=postgresql://hello_flask:hello_flask@127.0.0.1:5432/hello_flask_dev
set FLASK_APP=web/project/__init__.py
python web/manage.py create_db
python web/manage.py run