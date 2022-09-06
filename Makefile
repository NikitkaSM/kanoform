venv:
	source venv/bin/activate && source .env

run: 
	python3 manage.py runserver 8123

migrate:
	python3 manage.py makemigrations && python3 manage.py migrate
