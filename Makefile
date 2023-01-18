mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

locale:
	python3 manage.py makemessages -l en
	python3 manage.py makemessages -l uz
	python3 manage.py makemessages -l ru

compile:
	python3 manage.py compilemessages
