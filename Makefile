test:
	docker-compose up -d
	pytest --disable-warnings || true
	docker-compose down

build:
	docker-compose down
	docker build -t server .

stop:
	docker-compose down

run:
	docker-compose down
	docker-compose up -d
	docker-compose logs -f
