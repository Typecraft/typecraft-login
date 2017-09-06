.PHONY: test
test:
	python manage.py test

.PHONY: run
run:
	python manage.py runserver