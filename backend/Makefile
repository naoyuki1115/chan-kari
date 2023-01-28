plantuml:
	docker run -d --rm -p 12345:8080 --name plantuml plantuml/plantuml-server

run-prod:
	stage=prod docker compose up --build
run-dev:
	stage=dev docker compose up --build
enter-container:
	docker compose up --build -d
	docker exec -it chankari-backend bash

# available from docker container
api-from-container:
	uvicorn main:app --host 0.0.0.0 --reload
db-from-container:
	psql -h db -U postgres
