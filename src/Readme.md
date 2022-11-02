```
to launch app: 
    uvicorn src.main:app --host 0.0.0.0 --port 80
    uvicorn main:app --host 0.0.0.0 --port 80

to build docker: 
    docker build -f src/Dockerfile  -t fish --no-cache .

to launch docker:
    docker run --rm --name fish -d -p 80:80 fish:latest
    docker run -it fish:latest uvicorn main:app --host 0.0.0.0 --port 80
    docker stop fish
    docker run --network host -it fish:latest bash
    
to add src as python path:
    (Windows): set PYTHONPATH=%PYTHONPATH%;C:\Users\mnalimov\project\src

celery  -A src.main.celery_ worker -l info --pool=eventlet
celery --broker=redis://127.0.0.1:6379/0 -A src.main.celery_ worker flower --port=5566
```