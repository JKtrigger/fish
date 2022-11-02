```
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