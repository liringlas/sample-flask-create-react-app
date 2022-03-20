init:
	pip install -r requirements.txt

test:
	nosetests tests

pip-freeze:
	pip freeze > requirements.txt

activate:
	 source ./venv/bin/activate

serve-dev:
	FLASK_APP=./src/application.py flask run