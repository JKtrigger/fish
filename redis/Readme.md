launch redis: 
    docker run --network host --rm --name redis -d -p 6379:6379 redis:latest
    docker run -it redis:latest bash
    docker stop redis
from local src project: 
    docker run --rm --name redis -d -p 6379:6379 redis:latest
