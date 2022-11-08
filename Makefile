.PHONY: bin/example

default: install

serve:
	gunicorn -w 4 local_crunchbase.wsgi

install:
	pip3 install -r requirements.txt

test:
	pytest --cov=.