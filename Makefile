.PHONY: test
test:
	python manage.py test

.PHONY: run
run:
	python manage.py runserver

.PHONY: freeze
freeze:
	rm -f requirements.txt && pip freeze > requirements.txt
