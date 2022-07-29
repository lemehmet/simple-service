.PHONY: image build clean help run
DOCKER_REPO := 859254876439.dkr.ecr.us-east-1.amazonaws.com/simple_service
SRV_NAME := simple_service
TAG = $(shell git rev-parse HEAD)
# Get the user:group for docker operations
THE_USER := $(shell id -u):$(shell id -g)

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

image: ## Create docker image
	docker build --platform=linux/amd64 --platform=linux/arm64 -t ${SRV_NAME} .
	docker tag ${SRV_NAME}:latest ${DOCKER_REPO}:latest
	docker tag ${SRV_NAME}:latest ${DOCKER_REPO}:${TAG}

build: image ## One less typo

push: image ## Publish the image
	docker push ${DOCKER_REPO}:latest
	docker push ${DOCKER_REPO}:${TAG}

run: image ## Run the image locally
	docker run --rm --user "$(THE_USER)" -p 8080:8080 $(SRV_NAME):$(TAG)

lambda_run: image
	docker run -p 9000:8080 $(SRV_NAME):$(TAG)

clean: ## Clean up
	@rm -f $(SPEC_FILE)
