---
launch: 
    docker-compose build --no-cache
    docker-compose up -d
    docker ps
down: 
    docker-compose down 
    stop docker <name>

self test:
    -   via curl: 
            curl -X GET http://127.0.0.1/
    -   via State
            docker-compose ps
            docker logs project_celery_worker_1
---
minikube launch: 
    