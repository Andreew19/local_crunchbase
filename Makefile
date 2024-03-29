.PHONY: bin/example

default: install

serve:
	docker run --restart=always -d -p 8000:8000 local-crunchbase gunicorn -b 0.0.0.0:8000 -w 2 local_crunchbase.wsgi

install:
	pip3 install -r requirements.txt

test:
	DJANGO_SETTINGS_MODULE=local_crunchbase.settings pytest --cov=.

build:
	docker build -t local-crunchbase .

shell:
	docker run --rm -i -t --net=host local-crunchbase python3 manage.py shell

deploy:
	docker build -t local-crunchbase .
	docker rm $$(docker stop $$(docker ps -a -q --filter ancestor=local-crunchbase))
	docker run --restart=always -d -p 8000:8000 local-crunchbase gunicorn -b 0.0.0.0:8000 -w 2 local_crunchbase.wsgi

