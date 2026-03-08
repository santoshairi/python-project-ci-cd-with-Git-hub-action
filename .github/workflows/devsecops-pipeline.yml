name: DevSecOps End To End Pipeline

on: 
    push:
        branches: [main]

jobs:
    # CI (Continous Integration with Security Scanning)
    code-quality:
        uses: ./.github/workflows/code-quality.yml

    secrets-scan:
        uses: ./.github/workflows/secrets-scan.yml
        secrets: inherit
    
    dependency-scan:
        uses: ./.github/workflows/dependency-scan.yml
    
    docker-scan:
        uses: ./.github/workflows/docker-lint.yml

    tests:
        uses: ./.github/workflows/tests.yml

    # Build once the security scans and tests are complete
    build:
        needs: [code-quality, secrets-scan, dependency-scan, docker-scan, tests]
        uses: ./.github/workflows/docker-build-push.yml
        secrets: inherit

    # Image scan 
    trivy:
        needs: [build]
        uses: ./.github/workflows/image-scan.yml
        secrets: inherit

    # CD : Deploy to Production 
    deploy:
        needs: [trivy]
        uses: ./.github/workflows/deploy-to-server.yml
        secrets: inherit

    
