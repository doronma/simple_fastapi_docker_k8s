# ISTIO

https://istio.io/latest/docs/setup/getting-started/

## Install Istio

istioctl install --set profile=demo -y
kubectl label namespace default istio-injection=enabled

host:localhost, port:80

## Access the Kiali dashboard

istioctl dashboard kiali

# k8s

## Restart main pods

kubectl rollout restart deployment/fastapi-deployment
