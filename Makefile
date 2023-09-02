include ./.env

build:
	docker build -t address_services --no-cache .

run:
	docker run --env-file .env --network ${DEV_CONTAINER_NETWORK} -p ${APPLICATION_PORT}:8000 --name address_services -d address_services
