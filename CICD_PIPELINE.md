# CI/CD Pipeline Explained

This document explains the complete CI/CD pipeline in this project, defined in `.github/workflows/deploy.yml`.

---

## What is CI/CD?

- **CI (Continuous Integration)** — Every time code is pushed, an automated bot checks it: runs linting, tests, and coverage. Bugs get caught in minutes, not weeks.
- **CD (Continuous Delivery/Deployment)** — Code that passes those checks is automatically packaged into a Docker image and deployed to servers, without manual steps.

---

## When does the pipeline run?

- Pushes to `main` or `DevOps` branches
- Pushes of version tags (`v1.2.0`, etc.)
- Pull Requests targeting `main`/`DevOps`
- Manual trigger (`workflow_dispatch`)

---

## Stage 1 — `validate` (Lint, Test & Coverage Gate)

Runs first on every event.

1. **Flake8** (Python linter) — checks for syntax errors and unused imports. Build stops on real errors.
2. **Django tests** — `coverage run manage.py test`
3. **Coverage gate** — `--fail-under=80` means if test coverage is below **80%**, the build **aborts**.
4. Uploads HTML/XML coverage reports as GitHub artifacts (kept 14 days).

---

## Stage 2 — `security-scans` (Enterprise Security)

Runs only after `validate` passes. 5 scanners:

1. **GitLeaks** — scans git history for accidentally committed secrets (API keys, passwords).
2. **Trivy (filesystem)** — checks `requirements.txt` dependencies for known vulnerabilities. **Fails** on HIGH/CRITICAL.
3. **Semgrep** — SAST scanner for Python/Django security anti-patterns (SQL injection, bad config).
4. **CodeQL** — GitHub's deep security analysis.
5. **SBOM** — generates a bill-of-materials (list of all dependencies) for compliance audits.

---

## Stage 3 — `ai-review` (AI Code Review)

Only runs on **Pull Requests**. Runs `.github/scripts/ai_review.py`:

1. Gets the PR's diff (`git diff origin/main...HEAD`)
2. Sends it to the OpenCode AI API asking for review of Dockerfile, workflows, Kubernetes configs, and Python code
3. Posts the review as a comment directly on the PR
4. Falls back to a mock review if the API call fails.

---

## Stage 4 — `build-and-push` (Build, Scan & Sign Docker Image)

Only runs on **pushes to main/DevOps/tags** (not PRs):

1. **QEMU + Buildx** — sets up building for both `linux/amd64` and `linux/arm64`.
2. **Push to Docker Hub** — `harshal001/django-polls-app:latest` + tagged with git SHA or version tag.
3. **Trivy image scan** — scans the built container image, fails on HIGH/CRITICAL.
4. **Cosign** — signs the image using GitHub OIDC so only trusted images can run in production.

---

## Stage 5 — `deploy-staging`

Runs on push to `main`/`DevOps`. Deploys to the **staging** Kubernetes cluster via **Helm**:

- `helm upgrade --install` with `values-staging.yaml`
- **Auto-rollback** if deployment fails
- Verifies the rollout, then runs **smoke tests** (curls `/health/` and `/metrics/`)
- Notifies Slack on success.

---

## Stage 6 — `deploy-production`

Only runs when you push a **version tag** (`v1.2.0`). Deploys to the **production** environment:

- Requires **manual approval** via the GitHub "environment" gate.
- Same Helm deploy + rollback + smoke tests, using `values-production.yaml`.
- Notifies Slack.

---

## Full Flow Diagram

```
Push / PR
   │
   ▼
┌─ validate ──fail─→ ✖ abort
│   │ pass
│   ▼
│ security-scans ──fail─→ ✖ abort
│   │ pass
│   ├── PR? → ai-review → comment on PR
│   └── Push? → build-and-push (Docker Hub + sign)
│                    │
│                    ▼
│              deploy-staging (main/DevOps)
│              deploy-production (v-tag, manual approval)
└───────────────────────────────────────────
```

---

## How to Run the Security Scan Locally

Install Trivy (one-time):

```bash
curl -sSfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
```

Or on Ubuntu: `sudo apt-get install trivy`

Run the scan from the project folder:

```bash
trivy fs . --scanners vuln --severity HIGH,CRITICAL
```

**Reading results:**

- `0 vulnerabilities` → PASS
- High/Critical found → upgrade that package in `requirements.txt`

**Note:** First run downloads a ~100MB vulnerability database (one-time).
