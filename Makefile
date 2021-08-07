
DOCKER_YAML=-f docker-compose.yml
DOCKER=COMPOSE_PROJECT_NAME=rarejob-tutor-checker docker-compose $(DOCKER_YAML)

build:
	$(DOCKER) build ${ARGS}

up:
	$(DOCKER) up

py-test:
	$(DOCKER) run --rm server ./scripts/py-test.sh '${PACKAGE}' '${ARGS}'

