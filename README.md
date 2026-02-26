# metrics-api

A production-style Python microservice built with FastAPI, containerized with Docker, and deployed to Kubernetes. Exposes system metrics via a Prometheus-compatible `/metrics` endpoint, along with health and readiness probes for Kubernetes lifecycle management.

Built as part of a 20-week SRE/DevOps portfolio roadmap.

---

## Tech Stack

- **Python 3.12** + **FastAPI** — async web framework
- **psutil** — system metrics collection
- **prometheus-client** — Prometheus metrics exposition
- **Docker** — containerization
- **Kubernetes** — orchestration (Minikube locally, EKS in production)
- **GitHub Actions** — CI pipeline
- **Ruff + mypy + pytest** — quality gates

---

## Project Structure
```
k8s-microservice/
├── app/
│   ├── main.py          # FastAPI app factory
│   ├── config.py        # Environment-based configuration
│   ├── routers/
│   │   ├── health.py    # /healthz and /readyz probes
│   │   ├── info.py      # /info endpoint
│   │   └── metrics.py   # /metrics Prometheus endpoint
│   └── services/
│       ├── sysstats.py  # psutil-based system stats
│       └── workload.py  # CPU/memory load simulation for HPA testing
├── tests/
│   └── test_health.py
├── k8s/
│   ├── configmap.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   └── servicemonitor.yaml
└── .github/workflows/
    ├── ci.yml
    └── cd-eks.yml
```

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/healthz` | GET | Liveness probe — returns `{"ok": true}` |
| `/readyz` | GET | Readiness probe — returns `{"ready": true}` |
| `/info` | GET | App metadata. Add `?full=true` for system stats |
| `/metrics` | GET | Prometheus metrics exposition |

---

## Local Development

### Prerequisites

- Python 3.12+
- Docker Desktop
- Minikube
- kubectl

### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run locally
```bash
make run
# App available at http://localhost:5050
```

### Quality gates
```bash
make lint    # Ruff auto-fix and format
make type    # mypy type check
make test    # pytest
```

---

## Docker

### Build
```bash
make docker-build
```

### Run container locally
```bash
docker run -d -p 5050:5000 --name metrics-api my-k8s-app:0.1.0
curl -s http://localhost:5050/healthz
docker rm -f metrics-api
```

---

## Kubernetes (Minikube)

### Start Minikube
```bash
minikube start --driver=docker
minikube addons enable metrics-server
minikube addons enable ingress
```

### Build and load image
```bash
make docker-build
make minikube-load
```

### Deploy
```bash
make k8s-apply
kubectl get pods -w
```

### Access the service
```bash
make k8s-forward
# App available at http://localhost:5050
```

### Verify endpoints
```bash
curl -s http://localhost:5050/healthz
curl -s http://localhost:5050/readyz
curl -s http://localhost:5050/info
curl -s http://localhost:5050/metrics | head
```

### Clean up
```bash
make k8s-clean
```

---

## CI Pipeline

GitHub Actions runs on every push and pull request to `main`:

1. **Ruff** — lint check (read-only, no auto-fixes)
2. **mypy** — static type checking
3. **pytest** — unit tests
4. **Docker build** — verifies image builds successfully

CI never modifies source code. Formatting is enforced locally via pre-commit hooks.

---

## License

MIT — see [LICENSE](LICENSE)
