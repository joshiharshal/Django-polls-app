# QuickPolls - DevOps Poll App 🎯

A beautiful, modern Django-based web application that allows users to create, participate in, and analyze polls. This application features a premium dark-mode interface with a glassmorphic design, robust database migration pipelines, and is containerized and automated with CI/CD for cloud deployments.

---

## 📃 Project Description

QuickPolls features an interactive poll asking: **"Which DevOps tool do you use the most?"** Users can vote for industry-standard tools like Docker, Kubernetes, Jenkins, Terraform, and Ansible, and immediately view real-time graphical statistics of the voting results.

---

## 🔹 Features

- **Interactive Voting Dashboard**: Clean, responsive layout utilizing radio indicators and cards.
- **Real-Time Visual Results**: Live vote count calculation and stylized progress bars dynamically presenting percentages.
- **Premium Dark Mode & Glassmorphic UI**: Beautiful aesthetics built with Outfit & Inter typography, sleek gradients, and subtle hover animations.
- **Django Admin Panel Integration**: Fully integrated console at `/admin/` to manage questions, choices, and track live database objects.
- **Containerized Architecture**: Multi-stage `Dockerfile` and optimized `docker-compose.yml` defining separated Python (Gunicorn) and PostgreSQL database services.
- **Automated CI/CD Pipeline**: GitHub Actions workflow that automatically tests/builds the Docker image, pushes it to Docker Hub, and deploys it directly to a VPS.
- **Production Static Assets**: Pre-configured with WhiteNoise to collect and serve static files under production environments.

---

## 📆 Screenshots

### ✅ Active Polls Dashboard
![Dashboard Screenshot](screenshots/dashboard.png)

---

## 📊 Technologies Used

- **Frontend**: HTML5, CSS3 (with Outfit/Inter Google Fonts and FontAwesome Icons)
- **Backend**: Django 5.1.3 (Python 3.13)
- **Database**: 
  - SQLite (Local development default)
  - PostgreSQL 16 (Production/Compose default)
- **Web/App Server**: Gunicorn 23.0.0
- **Static Hosting**: WhiteNoise
- **DevOps & CI/CD**: Docker, Docker Compose, GitHub Actions

---

## 📁 Installation & Running Guide

### Option A: Local Development (SQLite)

#### 1. Clone the Repository
```bash
git clone https://github.com/joshiharshal/devops-poll-app.git
cd Django-polls-app
```

#### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run Migrations and Start Server
```bash
python manage.py migrate
python manage.py runserver
```

#### 5. View in Browser
Open your browser and navigate to: `http://127.0.0.1:8000/`

---

### Option B: Containerized Development (Docker Compose & PostgreSQL)

You can launch the entire stack—including the Django application and a PostgreSQL database—locally using Docker.

#### 1. Start Containers
```bash
docker compose up --build -d
```
*Note: The compose environment automatically runs migrations and hosts the web application with Gunicorn.*

#### 2. View in Browser
Open your browser and navigate to: `http://127.0.0.1:8000/`

---

## 🚀 Enterprise CI/CD Pipeline (GitHub Actions)

This project contains an advanced, production-ready CI/CD pipeline configured at `.github/workflows/deploy.yml` that automates testing, security compliance, quality gates, AI code reviews, multi-architecture image builds, and container signing.

### 📋 Pipeline Stages

The pipeline is split into distinct security and quality-assurance stages:
1. **Lint & Test**: Performs Python code linting via `flake8` and runs Django unit and integration tests.
2. **Quality Gate**: Enforces a strict **minimum of 80% test coverage** using `coverage`. If coverage drops below 80%, the build fails and blocks code merging.
3. **Security Gates**:
   - **GitLeaks**: Scans the commit history to detect accidentally committed credentials and secrets.
   - **Trivy (FS)**: Scans filesystem dependencies for critical vulnerabilities, failing the pipeline if any are found.
   - **Semgrep SAST**: Performs static analysis for common Django/Python anti-patterns and vulnerabilities.
   - **CodeQL**: Standard GitHub SAST scanning for deeper vulnerability validation.
   - **SBOM**: Automatically compiles and uploads a CycloneDX Software Bill of Materials (SBOM).
4. **AI Code Review**: Run on pull requests using **OpenCode and Antigravity AI**. It scans your diff, analyzes Dockerfiles/workflows, and automatically comments feedback directly onto the PR.
5. **Multi-Arch Build & Push**: Automatically sets up Docker Buildx and QEMU to compile the application for both `linux/amd64` and `linux/arm64` simultaneously.
6. **Container Image Scanning**: Runs Trivy container scans on the final image.
7. **Cosign Signatures**: Signs the published image using OIDC keyless signing, providing cryptographically verifiable container integrity.

### 🔑 Required GitHub Secrets

To activate this pipeline, configure the following secrets in your repository settings (**Settings > Secrets and variables > Actions > Repository secrets**):

| Secret Name | Description | Example / Recommended Value |
| :--- | :--- | :--- |
| `DOCKER_USERNAME` | Docker Hub username. | `harshal001` |
| `DOCKER_PASSWORD` | Docker Hub Personal Access Token (PAT). | `dckr_pat_...` |
| `SLACK_WEBHOOK` | Webhook URL for Slack build notifications. | `https://hooks.slack.com/services/...` |
| `OPENCODE_API_KEY` | API Key for OpenCode review API. | `oc_api_...` |

### 🛠️ Workflow Triggers

- **Pull Requests (to main/DevOps)**: Runs linting, tests, coverage verification, security scans, and triggers the AI Code Review comment on the PR. Does not build or push Docker images.
- **Pushes (to main/DevOps)**: Runs all tests, scans, builds the multi-arch Docker image, tags it with the Git Commit SHA, pushes it to Docker Hub, signs it with Cosign, and sends a Slack notification.
- **Release Tags (`v*`)**: Triggered when a semantic version tag (e.g. `v1.0.0`) is pushed. Builds the production image, tags it with the release tag name, signs it, and posts a Slack release announcement.


---

## 🎡 Project Structure

```text
Django-polls-app/
├── .github/
│   └── workflows/
│       └── deploy.yml        # CI/CD deployment pipeline configuration
├── mysite/
│   ├── settings.py           # Core Django settings
│   ├── urls.py               # Main URL router
│   └── wsgi.py               # WSGI entrypoint for Gunicorn
├── polls/
│   ├── migrations/           # Database migration files
│   ├── static/               # CSS styles and static assets
│   ├── templates/            # Django template HTML views
│   ├── models.py             # Database schemas (Question, Choice)
│   ├── urls.py               # Poll routes
│   └── views.py              # Controller / View handlers
├── screenshots/
│   └── dashboard.png         # Active Polls Dashboard screenshot
├── Dockerfile                # Production multi-stage Docker container build
├── docker-compose.yml        # Docker Compose configuration (Django & PostgreSQL)
├── requirements.txt          # Python project dependencies
├── db.sqlite3                # SQLite database (local development)
└── README.md                 # Project documentation
```

docker build -t harshal001/django-polls-app:latest .
docker push harshal001/django-polls-app:latest
---

## 👥 Author

**Harshal**

GitHub: [@joshiharshal](https://github.com/joshiharshal)

---

## ✏️ License

- This project is licensed under the MIT License. Feel free to use, modify, and share it.
- See the LICENSE file for more details.