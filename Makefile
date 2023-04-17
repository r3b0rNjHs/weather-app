.PHONY: build

start: build _start

_start:
	docker-compose up app

test: build
	docker-compose run mamba test

shell: build _shell

_shell:
	docker-compose run app sh

build: launch_services
	docker-compose build

launch_services: stop
	docker-compose up --build -d postgres
	docker-compose run dependencies dockerize \
		-wait tcp://postgres:5432 \
		-timeout 60s
		echo "Services running"

stop:
	docker-compose down -v