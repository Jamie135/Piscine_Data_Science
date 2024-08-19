DOCKER_COMPOSE = docker-compose.yaml

all : build run

build:
	docker-compose -f $(DOCKER_COMPOSE) build

run:
	docker-compose -f $(DOCKER_COMPOSE) up

list:
	docker images
	@echo "-------"
	docker ps -a
	@echo "-------"
	docker volume ls -q
	@echo "-------"
	docker network ls

stop: 
	docker stop $$(docker ps -aq)

start: 
	docker start $$(docker ps -aq)

clean: stop
	docker-compose -f $(DOCKER_COMPOSE) down --remove-orphans
	docker images prune

fclean:	clean
	docker volume rm $$(docker volume ls -q)
	docker rmi $$(docker images -aq)
	docker system prune --all --volumes --force

re:	fclean all

.PHONY: all clean fclean re
