test:
	docker-compose up -d
	pytest --disable-warnings || true
	docker-compose down

reload:
	docker-compose down
	docker build -t server .

stop:
	docker-compose down
