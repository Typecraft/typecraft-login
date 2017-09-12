.PHONY: test
test:
	python manage.py test

.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8011

.PHONY: freeze
freeze:
	rm -f requirements.txt && pip freeze > requirements.txt
