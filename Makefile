BASE_COMPOSE=docker-compose.yml
LOCAL_COMPOSE=docker-compose-local.yml

test:
	docker-compose up -d
	python -m pytest --disable-warnings || true
	docker-compose down

build:
	docker-compose down
	docker build -t server .

prune:
	docker-compose -f $(BASE_COMPOSE) down --rmi all --volumes --remove-orphans

stop:
	docker-compose down

run:
	docker-compose up -d
	docker-compose logs -f

reload:build run
