test:
	docker-compose up -d
	pytest --disable-warnings || true
	docker-compose down

build:
	docker-compose down
	docker build -t server .

stop:
	docker-compose down
