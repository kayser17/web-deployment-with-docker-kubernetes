# 🚀 Scalable Application Deployment Practice

This repository contains the complete deployment practice for a web application, developed as part of a cloud and DevOps university course. The objective was to deploy the same application in various environments and architectural models, moving from a traditional monolith to a microservices-based architecture using Docker and Kubernetes.

---

## 🌐 Technologies Used

- Python, Ruby, Java, Node.js (Polyglot microservices)
- Docker, Docker Compose
- Kubernetes (GKE / Minikube / Play-with-K8s)
- Google Cloud VM
- Bash & Python scripting

---

## ✅ Practice Structure

### 1. 🌟 Monolithic Deployment on Virtual Machine

- Python script to deploy the application in a Google Cloud VM or local VM.
- The app runs on a custom port (e.g., 5060).
- The environment variable `GROUP_NUM` is passed and rendered in the HTML `<title>`.
- The app is made publicly accessible via the VM's external IP and selected port.

### 2. 🐳 Monolithic Deployment using Docker

- A `Dockerfile` is defined using `python:3.7.7-slim` as base image.
- The environment variable `GROUP_NUM` is passed to the container.
- Docker image is built and tagged as `product-page/<group_number>`.
- Container is launched with a name format like `product-page-gXX`.

Example command:

```bash
docker run --name product-page-gXX -p 5060:5060 -e GROUP_NUM=XX -d product-page/gXX
```
### 3. 🧩 Microservices Deployment with Docker Compose

The application is split into multiple microservices:

- `productpage` (Python)
- `details` (Ruby)
- `reviews` (Java) – with versions: `v1`, `v2`, `v3`
- `ratings` (Node.js)

Each service has its own `Dockerfile`.

- The `reviews` service is built using Gradle and versioned via the `SERVICE_VERSION` environment variable.
- A `docker-compose.yml` file is used to orchestrate all the services.
- Only one version of the `reviews` service can be active at a time.
- Environment variables and container names follow consistent naming conventions.

### 4. ☸️ Microservices Deployment with Kubernetes

A Kubernetes cluster is created in GKE with **3 nodes** (no autoscaling).

Each microservice is deployed as an independent pod with the following replica strategy:

- `details`: 3 replicas
- `ratings`: 2 replicas

Each service has its own **Deployment** and **Service** YAML definition.

External access is provided through a `productpage` service, which exposes a public IP.

Reference YAML files are located under platform/kube/.

---
## ⚠️ Disclaimer

This repository was created for academic purposes. Some configurations, scripts, and images were adapted from official course material provided during the course.
