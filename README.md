# DevOps Poll App 🎯

A simple Django-based web app that allows users to vote for their favorite DevOps tool. This project demonstrates form handling, frontend styling, and basic backend logic.

---

## 📃 Project Description
This application presents users with a poll asking: **"Which DevOps tool do you use the most?"** Users can choose from popular tools like Docker, Kubernetes, Jenkins, Terraform, and Ansible.

---

## 🔹 Features
- Interactive voting form using HTML and Django
- Emojis for a more engaging UI
- Radio button selection and a vote button
- Easy integration with a Django backend
- Ready for AJAX-based submission (optional upgrade)

---

## 📆 Screenshots

### ✅ Poll Form Interface:
![Poll Screenshot](screenshots/Screenshot_20250405_144216.png)

### ✉️ Form Submission Layout:
![Submission Screenshot](screenshots/Screenshot_20250405_144314.png)

> Place these images in a folder named `screenshots/` inside your project root directory for proper rendering.

---

## 📊 Technologies Used
- **Frontend**: HTML5, CSS3 (with emoji styling)
- **Backend**: Django (Python)
- **Database**: SQLite (default for development)

---

## 📁 Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/devops-poll-app.git
cd devops-poll-app
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations and Start Server
```bash
python manage.py migrate
python manage.py runserver
```

### 5. View in Browser
Open your browser and go to: `http://127.0.0.1:8000/`

---

## 🎡 Project Structure
```
devops-poll-app/
├── polls/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── screenshots/
│   ├── Screenshot_20250405_144216.png
│   └── Screenshot_20250405_144314.png
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👥 Author
**Harshal**

GitHub: [@joshiharshal](https://github.com/joshiharshal)

---

## 🚀 Want to Expand It?
- Add real-time vote results display
- Store results in a Django model
- Integrate AJAX for no-reload form submission
- Secure votes using session or IP validation
- Dockerize and deploy on AWS EC2 with Nginx

Let me know if you want help with any of these upgrades!

