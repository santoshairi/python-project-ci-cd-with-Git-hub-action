#  DevSecOps CI/CD Pipeline with GitHub Actions

A hands-on project demonstrating a **production-style DevSecOps CI/CD pipeline** built entirely using **GitHub Actions**.

This project shows how modern DevOps pipelines integrate **security scanning, testing, containerization, and automated deployment** into a single workflow.

---

#  Project Overview

This repository contains a **Flask web application** with a full **CI/CD + DevSecOps pipeline**.

```
app.py                  → Flask application
Dockerfile              → Container image definition
docker-compose.yml      → Production deployment configuration
templates/index.html    → Application frontend
requirements.txt        → Python dependencies
test_app.py             → Application tests (pytest)
```

---

# ⚙️ DevSecOps Pipeline

The pipeline is composed of **reusable workflows (`workflow_call`)** and is triggered on **push to the `main` branch**.

```
Push to main
    ├── Code Quality ──── flake8 + bandit (lint + SAST)
    ├── Secrets Scan ──── gitleaks (detect leaked secrets)
    ├── Dependency Scan ─ pip-audit (dependency vulnerabilities)
    ├── Docker Lint ───── hadolint (Dockerfile best practices)
    └── Tests ─────────── pytest (application tests)
            │
            ▼
        Docker Build & Push ── build image and push to Docker Hub
            │
            ▼
        Image Scan ─────────── Trivy (container vulnerabilities)
            │
            ▼
        Deploy to Server ───── SSH into AWS EC2 and run docker compose
```

---

# 🛠 Tools & Technologies

| Tool | Purpose |
|-----|------|
| GitHub Actions | CI/CD automation |
| Docker | Containerization |
| Gitleaks | Secrets detection |
| Bandit | Python SAST security scanning |
| pip-audit | Dependency vulnerability scanning |
| Hadolint | Dockerfile linting |
| Trivy | Container image vulnerability scanning |
| AWS EC2 | Application deployment |
| Docker Compose | Container orchestration |
| SSH | Remote server deployment |
| Python / Flask | Application framework |

---

# 📂 Workflows

| # | Workflow | Description |
|---|---------|-------------|
| 1 | DevSecOps Pipeline | Main workflow that orchestrates all pipeline stages |
| 2 | Code Quality | Runs flake8 and bandit for linting and security checks |
| 3 | Secrets Scan | Detects secrets using Gitleaks |
| 4 | Dependency Scan | Scans Python dependencies for vulnerabilities |
| 5 | Docker Lint | Validates Dockerfile using Hadolint |
| 6 | Image Scan | Scans container images using Trivy |
| 7 | Deploy to Server | Deploys the application to AWS EC2 |
| 8 | Tests | Runs pytest tests for the application |
| 9 | Docker-build-push | Code build and push to docker hub |

---

# 🔐 Security in CI/CD

Security checks integrated in the pipeline:

- 🔐 Secrets detection with **Gitleaks**
- 📦 Dependency vulnerability scanning with **pip-audit**
- 🐳 Dockerfile best practices using **Hadolint**
- 🛡 Container image vulnerability scanning using **Trivy**

---

#  Deployment

Deployment is automated using **SSH to AWS EC2**.

Deployment process:

1. Connect to EC2 server via SSH  
2. Pull the latest Docker image  
3. Stop the running container  
4. Deploy the updated container using Docker Compose  

---

#  Required GitHub Secrets

Add the following secrets in:

**Repository → Settings → Secrets → Actions**

```
DOCKERHUB_USER
DOCKERHUB_TOKEN
EC2_SSH_HOST
EC2_SSH_USER
EC2_SSH_PRIVATE_KEY
```

---

# 📁 Repository Structure

```
.
├── .github/workflows/
│   ├── devsecops-pipeline.yml
│   ├── code-quality.yml
│   ├── secrets-scan.yml
│   ├── dependency-scan.yml
│   ├── docker-lint.yml
│   └── docker-build-push.yml
│   ├── image-scan.yml
│   ├── deploy-to-server.yml
│   └── tests.yml
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── templates/index.html
└── test_app.py
```

---

# 📊 CI/CD Pipeline Summary

⚙️ Built  
🧪 Tested  
🧹 Linted  
🔍 Code Quality Checked  
🔐 Secrets Scanned (Gitleaks)  
📦 Dockerized  
🛡 Container Security Scan (Trivy)  
🚀 Deployed via GitHub Actions

---

# Learning Outcomes

Through this project I practiced:

- GitHub Actions CI/CD pipeline design
- DevSecOps security integration
- Docker containerization
- Container vulnerability scanning
- Automated deployment to cloud infrastructure

---
Special thanks to **Shubham Bhai** for guidance and mentorship throughout this DevSecOps learning journey.
---

⭐ If you found this project useful, consider giving it a **star**.