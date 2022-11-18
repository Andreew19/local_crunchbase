.PHONY: bin/example

default: install

serve:
	docker run --restart=always -d --net=host local-crunchbase gunicorn -w 4 local_crunchbase.wsgi

install:
	pip3 install -r requirements.txt

test:
	pytest --cov=.

build:
	docker build -t local-crunchbase .

shell:
	docker run --rm -i -t --net=host local-crunchbase python3 manage.py shell
