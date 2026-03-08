# GitHub Actions: Zero to Hero

A hands-on repo to learn GitHub Actions from scratch. Each workflow covers a real-world concept — start from the top and work your way down.

## What's Inside

This repo contains a **Flask web app** with a full **CI/CD + DevSecOps pipeline** built entirely using GitHub Actions.

```
app.py                  → Flask app (source code)
Dockerfile              → Container image definition
docker-compose.yml      → Production deployment config
templates/index.html    → App frontend
index.html              → Portfolio static site
requirements.txt        → Python dependencies (flask, flake8, bandit, gunicorn, pytest)
test_app.py             → Route tests (pytest)
```

## Workflows

### Part 1 — Fundamentals

| # | Workflow | Concepts Covered | What It Does |
|---|---------|-----------------|-------------|
| 1 | [Hello](.github/workflows/hello.yml) | `workflow_dispatch`, `pull_request`, multiple jobs, runners, parallel execution | Your first workflow — runs echo commands across two jobs |
| 2 | [CICD](.github/workflows/cicd.yml) | `workflow_dispatch` inputs, `type: choice`, `needs` (job dependencies), `if` conditionals | Simulates a CI/CD pipeline (code → build → test → deploy) with manual environment selection |
| 3 | [Portfolio Deploy](.github/workflows/portfolio-deploy.yml) | `permissions`, pre-built actions (`checkout`, `configure-pages`, `deploy-pages`), environments, deployment URLs | Deploys a static site to GitHub Pages using official actions |
| 4 | [Python Lint](.github/workflows/python-matrix.yml) | `strategy.matrix`, `fail-fast: false`, `actions/setup-python`, dependency install | Lints `app.py` with flake8 across Python 3.9–3.13 in parallel |
| 5 | [Docker Build & Push](.github/workflows/docker-build-push.yml) | `workflow_call` (reusable workflow), `secrets`, `vars`, `docker/login-action`, `docker/build-push-action`, multi-tag images | Builds a Docker image and pushes to Docker Hub with branch, latest, and SHA tags |
| 6 | [Deploy App](.github/workflows/deploy-app.yml) | `workflow_run` (chained workflows), `self-hosted` runners, `env` context, Docker Compose | Auto-deploys the Flask app on a self-hosted server after Docker image is pushed |

### Part 2 — DevSecOps Pipeline

A production-grade security pipeline composed from reusable workflows (`workflow_call`). Triggered on push to `main`.

```
push to main
    ├── Code Quality ──── flake8 + bandit SAST (matrix: 3.11–3.13)
    ├── Secrets Scan ──── gitleaks (full git history)
    ├── Dependency Scan ─ pip-audit (package CVEs)
    ├── Docker Lint ───── hadolint (Dockerfile best practices)
    └── Tests ─────────── pytest (route tests)
            │ (all five must pass)
            ▼
        Docker Build & Push ── build image, push to Docker Hub
            │
            ▼
        Image Scan ─────────── Trivy (CRITICAL + HIGH CVEs)
            │
            ▼
        Deploy to Server ───── SSH into EC2, docker compose up
```

| # | Workflow | Concepts Covered | What It Does |
|---|---------|-----------------|-------------|
| 7 | [DevSecOps Pipeline](.github/workflows/devsecops-pipeline.yml) | `on: push`, `workflow_call` composition, `needs` for stage gating, `secrets: inherit` | Orchestrator — chains all security scans → build → deploy |
| 8 | [Code Quality](.github/workflows/code-quality.yml) | `workflow_call`, matrix strategy, linting + SAST in one job | Runs flake8 (lint) and bandit (SAST) across Python 3.11–3.13 |
| 9 | [Secrets Scan](.github/workflows/secrets-scan.yml) | `workflow_call`, `fetch-depth: 0` (full clone), `GITHUB_TOKEN`, third-party action secrets | Scans full git history for leaked secrets using gitleaks |
| 10 | [Dependency Scan](.github/workflows/dependency-scan.yml) | `workflow_call`, `pip-audit`, vulnerability databases | Audits Python packages for known CVEs |
| 11 | [Docker Lint](.github/workflows/docker-lint.yml) | `workflow_call`, `hadolint/hadolint-action` | Validates Dockerfile against best practices |
| 12 | [Image Scan](.github/workflows/image-scan.yml) | `workflow_call`, `aquasecurity/trivy-action`, `severity` filtering, `exit-code: 1` | Scans pushed Docker image for CRITICAL and HIGH CVEs |
| 13 | [Deploy to Server](.github/workflows/deploy-to-server.yml) | `workflow_call`, `appleboy/ssh-action`, `appleboy/scp-action`, remote Docker Compose | SSHs into EC2, copies docker-compose, deploys the app |
| 14 | [Tests](.github/workflows/tests.yml) | `workflow_call`, `pytest`, Flask test client | Runs pytest against Flask routes (/, /health) |

## Concepts Cheat Sheet

| Concept | Where to Find It |
|---------|-----------------|
| Push trigger | [devsecops-pipeline.yml](.github/workflows/devsecops-pipeline.yml) |
| Pull request trigger (`pull_request`) | [hello.yml](.github/workflows/hello.yml) |
| Manual trigger (`workflow_dispatch`) | [hello.yml](.github/workflows/hello.yml), [cicd.yml](.github/workflows/cicd.yml) |
| Input parameters (`type: choice`) | [cicd.yml](.github/workflows/cicd.yml) |
| Job dependencies (`needs`) | [cicd.yml](.github/workflows/cicd.yml), [devsecops-pipeline.yml](.github/workflows/devsecops-pipeline.yml) |
| Conditional execution (`if`) | [cicd.yml](.github/workflows/cicd.yml), [deploy-app.yml](.github/workflows/deploy-app.yml) |
| Permissions | [portfolio-deploy.yml](.github/workflows/portfolio-deploy.yml) |
| Environments & deployment URLs | [portfolio-deploy.yml](.github/workflows/portfolio-deploy.yml) |
| Matrix strategy | [python-matrix.yml](.github/workflows/python-matrix.yml), [code-quality.yml](.github/workflows/code-quality.yml) |
| Reusable workflows (`workflow_call`) | [docker-build-push.yml](.github/workflows/docker-build-push.yml), all Part 2 workflows |
| `secrets: inherit` | [devsecops-pipeline.yml](.github/workflows/devsecops-pipeline.yml) |
| Chained workflows (`workflow_run`) | [deploy-app.yml](.github/workflows/deploy-app.yml) |
| Secrets & variables | [docker-build-push.yml](.github/workflows/docker-build-push.yml), [secrets-scan.yml](.github/workflows/secrets-scan.yml) |
| Self-hosted runners | [deploy-app.yml](.github/workflows/deploy-app.yml) |
| Docker build & push | [docker-build-push.yml](.github/workflows/docker-build-push.yml) |
| Docker Compose deploy | [deploy-app.yml](.github/workflows/deploy-app.yml), [deploy-to-server.yml](.github/workflows/deploy-to-server.yml) |
| SSH remote deployment | [deploy-to-server.yml](.github/workflows/deploy-to-server.yml) |
| SAST (bandit) | [code-quality.yml](.github/workflows/code-quality.yml) |
| Dependency vulnerability scan | [dependency-scan.yml](.github/workflows/dependency-scan.yml) |
| Container image scanning (Trivy) | [image-scan.yml](.github/workflows/image-scan.yml) |
| Dockerfile linting (hadolint) | [docker-lint.yml](.github/workflows/docker-lint.yml) |
| Secrets detection (gitleaks) | [secrets-scan.yml](.github/workflows/secrets-scan.yml) |
| Testing with pytest | [tests.yml](.github/workflows/tests.yml) |

## Getting Started

1. **Fork this repo**
2. **Set up secrets** — Go to repo Settings → Secrets and Variables → Actions:
   - Secret: `DOCKERHUB_TOKEN` (your Docker Hub access token)
   - Secret: `EC2_SSH_HOST`, `EC2_SSH_USER`, `EC2_SSH_PRIVATE_KEY` (for server deploy)
   - Secret: `GITLEAKS_LICENSE` (for gitleaks action)
   - Variable: `DOCKERHUB_USER` (your Docker Hub username)
3. **Push to main** — the DevSecOps pipeline triggers automatically

> **Note:** Deploy and image-scan jobs will fail until you configure your own server and Docker Hub secrets. This is expected — the CI jobs (code quality, tests, scans) will work out of the box.
4. **Try manual triggers** — go to Actions tab → pick a workflow → Run workflow
5. **Read each workflow file** — they are commented for learning

## Repo Structure

```
.
├── .github/workflows/
│   │
│   │  # Part 1 — Fundamentals
│   ├── hello.yml               # 1. Basics — jobs, runners, echo
│   ├── cicd.yml                # 2. Manual CI/CD — inputs, needs, if
│   ├── portfolio-deploy.yml    # 3. GitHub Pages — permissions, environments
│   ├── python-matrix.yml       # 4. Matrix — parallel linting
│   ├── docker-build-push.yml   # 5. Docker CI — build, tag, push (reusable)
│   ├── deploy-app.yml          # 6. Docker CD — workflow_run, self-hosted
│   │
│   │  # Part 2 — DevSecOps Pipeline
│   ├── devsecops-pipeline.yml  # 7. Orchestrator — chains all scans → build → deploy
│   ├── code-quality.yml        # 8. flake8 + bandit (lint + SAST)
│   ├── secrets-scan.yml        # 9. gitleaks (secrets in code)
│   ├── dependency-scan.yml     # 10. pip-audit (package CVEs)
│   ├── docker-lint.yml         # 11. hadolint (Dockerfile checks)
│   ├── image-scan.yml          # 12. Trivy (container image CVEs)
│   ├── deploy-to-server.yml   # 13. SSH + SCP deploy to EC2
│   └── tests.yml              # 14. pytest (route tests)
│
├── app.py                      # Flask application
├── templates/index.html        # Flask template
├── Dockerfile                  # Container definition
├── docker-compose.yml          # Compose config
├── index.html                  # Portfolio static site
├── requirements.txt            # Python dependencies
├── test_app.py                 # pytest route tests
└── CNAME                       # Custom domain for GitHub Pages
```
