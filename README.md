# 🌟 Automated CI/CD Pipeline for TaskManager App

This project demonstrates a **complete CI/CD pipeline** for the TaskManager web application using **Jenkins, Docker, and Kubernetes (Minikube)**.  
It automates the entire workflow from **code commit → CI build → Docker image push → Kubernetes deployment**, reflecting real-world DevOps practices. 🚀

---

## 🛠️ Technology Stack

| Component       | Technology                   |
|-----------------|-----------------------------|
| CI/CD            | Jenkins                     |
| Containerization | Docker                      |
| Container Registry | DockerHub                 |
| Orchestration    | Kubernetes (Minikube)       |
| Backend          | Python (Flask)             |
| Frontend         | Nginx                       |
| Version Control  | Git + GitHub                |

---

## 🚀 Features

- ✅ Automatic build of backend & frontend images  
- ✅ Push images to DockerHub  
- ✅ Deploy to Kubernetes cluster using manifests  
- ✅ Jenkins pipeline for full automation  
- ✅ Namespace support in Kubernetes deployments  

---

## 📦 Project Structure
```
kubernetes_project/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── index.html
│ └── Dockerfile
├── k8s/
│ ├── namespace.yaml
│ ├── backend-deployment.yaml
│ ├── backend-service.yaml
│ ├── db-deployment.yaml
│ ├── db-service.yaml
│ ├── frontend-deployment.yaml
│ └── frontend-service.yaml
├── Jenkinsfile
└── README.md

```
---

## 🧪 Prerequisites

Before running this project, ensure you have:

- Docker 🐳 installed  
- Minikube 🖥️ installed  
- Jenkins ⚙️ installed (or running in a container)  
- Git 🔗 configured  

---
```
## 📌 Setup & Deployment

### 1️⃣ Start Minikube
minikube start

2️⃣ Apply Kubernetes Namespace
kubectl apply -f k8s/namespace.yaml

3️⃣ Deploy Kubernetes Resources
kubectl apply -f k8s/

4️⃣ Open the Frontend
minikube service frontend-service -n taskmanager

```

🔧 Jenkins Pipeline

The CI/CD pipeline performs:

1.Checkout code from GitHub
2.Build backend & frontend Docker images
3.Tag and push images to DockerHub
4.Deploy Kubernetes resources

🧑‍💻 Kubernetes Manifests

All Kubernetes deployment and service YAML files are in the k8s/ folder.

These define:

1.Deployments & replicas
2.Container images from DockerHub
3.Services (ClusterIP / NodePort)
4.Namespace support

```
🚀 Outcomes

✅ Fully automated CI/CD pipeline
✅ Repeatable deployments with Kubernetes
✅ Hands-on DevOps experience
✅ Real-world deployment automation

```
