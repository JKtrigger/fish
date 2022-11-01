launch : 
    docker-compose build; 
    docker-compose up -d;
    docker ps;
down : 
    docker-compose down ; 
    stop docker <name>

self test via curl: 
    curl -X GET http://127.0.0.1/