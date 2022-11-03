```
apply service: 
    - kubectl apply -f .\manifest\service.yaml
    - kubectl get svc
    - minikube service k8s-service --url
    >> http://127.0.0.1:62820
    >> http://127.0.0.1:6282
delete service:
    - kubectl delete -f .\manifest\service.yaml

apply deployment:
    - kubectl apply -f .\manifest\deployment.yaml
    - kubectl get deploy
delete deployment:
    - kubectl delete -f .\manifest\deployment.yaml

apply pods:
    - kubectl apply -f .\manifest\pods.yaml
    - kubectl describe pods fish-pods
    - kubectl get pods

delete pods: 
    - kubectl delete -f .\manifest\pods.yaml

debug pods:
    - kubectl port-forward fish-pods 6379:6379
    - kubectl logs -f fish-pods -c container-fastapi-fish
    - kubectl port-forward fish-pods 80:80
    - curl -X GET http://127.0.0.1/
    - kubectl exec --stdin --tty fish-pods -c container-worker-fish -- /bin/bash

to avoid local storage for minikube:
     minikube image load fish
```