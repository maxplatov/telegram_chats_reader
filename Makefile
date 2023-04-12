ifneq (,$(wildcard ./.env))
    include .env
    export
endif

ifeq ($(IMAGE_NAME),none)
	NAME=$(IMAGE_NAME)
else
	NAME=telegram_chat_reader
endif

.PHONY: all
all: stop build run logs

.PHONY: build
build:
	docker build -t $(NAME) .

.PHONY: run
run:
	docker run -d --restart=always \
		--net=host \
		--ipc=host \
		--name=$(NAME) \
		$(NAME) \
		python main.py

.PHONY: stop
stop:
	-docker stop $(NAME)
	-docker rm $(NAME)

.PHONY: logs
logs:
	docker logs -f $(NAME)

.PHONY: exec
exec:
	docker exec -it $(NAME) bash