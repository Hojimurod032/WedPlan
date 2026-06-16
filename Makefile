make_l:
	python manage.py makemessages -l ru
	python manage.py makemessages -l uz

make_cop:
	python manage.py compilemessages

mig:
	python manage.py makemigrations
	python manage.py migrate