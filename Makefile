IMAGE_NAME = test-k8s
CONTAINER_NAME = test-k8s-container


build:
	@docker build -t $(IMAGE_NAME) .

run:
	@docker run -d -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

stop: 
	@docker stop $(CONTAINER_NAME)

remove:
	@docker rm $(CONTAINER_NAME)
removei:
	@docker rmi $(IMAGE_NAME)

.PHONY: build run stop remove removei
