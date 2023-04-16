.PHONY: build

start: build
	docker-compose up app

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