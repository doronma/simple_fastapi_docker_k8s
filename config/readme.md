# ISTIO

https://istio.io/latest/docs/setup/getting-started/

## Install Istio

istioctl install --set profile=demo -y
kubectl label namespace default istio-injection=enabled

host:localhost, port:80

## Access the Kiali dashboard

istioctl dashboard kiali

## hosts

C:\Windows\System32\drivers\etc
127.0.0.1 simple-fastapi.com

# k8s

## Restart main pods

kubectl rollout restart deployment/fastapi-deployment

## add password

kubectl create secret generic my-secrets --from-literal MYSEC=yaara2005

## run

http://simple-fastapi.com/
http://simple-fastapi.com/redis
http://simple-fastapi.com/persons
