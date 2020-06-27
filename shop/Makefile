.PHONY: build run bash exec

build:
	docker build . -t django-app

run:
	docker run --rm --user=$(shell id -u ${USER}):$(shell id -g ${USER}) -p 8000:8000 --name=app1 --volume $(shell pwd):/src django-app

bash:
	docker run -it --rm --user=$(shell id -u ${USER}):$(shell id -g ${USER}) -p 8000:8000 --name=app1 --volume $(shell pwd):/src django-app bash

exec:
	docker exec -it django-app bash

clean:
	docker run --rm --name=app1-clean --volume $(shell pwd):/src django-app bash -c "rm -rf ./temp *.log"
