APP=metrics-api
IMG=my-k8s-app
TAG=0.1.0

.PHONY: run test lint type docker-build minikube-load k8s-apply k8s-forward k8s-clean

run:
	uvicorn app.main:app --host 127.0.0.1 --port 5050

test:
	pytest -q

lint:
	ruff check app --fix
	ruff format

type:
	mypy app

docker-build:
	docker build -t $(IMG):$(TAG) .

minikube-load:
	minikube image load $(IMG):$(TAG)

k8s-apply:
	kubectl apply -f k8s/configmap.yaml
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml

k8s-forward:
	kubectl port-forward deploy/$(APP) 5050:5000

k8s-clean:
	kubectl delete -f k8s/ --ignore-not-found=true
