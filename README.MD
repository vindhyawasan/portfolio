# 🚀 Django Developer Portfolio

A modern, responsive, and dynamic personal portfolio website built with **Django**. This portfolio showcases my skills, projects, education, experience, resume, and contact information through a clean and professional interface.

## 🌐 Live Demo

Coming Soon

## 📌 Features

- 🏠 Professional Home Page
- 👨‍💻 About Me Section
- 🛠️ Dynamic Skills Section
- 💼 Dynamic Projects Section
- 🎓 Education Section
- 💻 Experience Section
- 📄 Resume Upload and View
- 📩 Contact Form
- 🌙 Dark / Light Mode
- 📱 Fully Responsive Design
- ✨ Smooth Animations and Hover Effects
- 📂 Dynamic Content using Django Models
- 🔐 Django Admin Dashboard for Content Management
- 🖼️ Profile and Project Image Upload
- 🔗 GitHub and LinkedIn Integration
- 🗄️ SQLite Database

## 🛠️ Technologies Used

### Backend
- Python
- Django

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- SQLite
- Django ORM

### Tools
- Git
- GitHub
- VS Code

## 📂 Project Structure

```text
portfolio/
│
├── manage.py
│
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── main/
│   ├── migrations/
│   ├── static/
│   │   └── main/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── script.js
│   │
│   ├── templates/
│   │   └── main/
│   │       └── index.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── media/
│   ├── profile_images/
│   ├── project_images/
│   └── pdf/
│
├── db.sqlite3
├── requirements.txt
└── README.md


⚙️ Installation and Setup
1. Clone the Repository
git clone https://github.com/yourusername/your-repository.git
2. Navigate to the Project
cd your-repository
3. Create a Virtual Environment
python -m venv venv
4. Activate Virtual Environment
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Apply Migrations
python manage.py makemigrations
python manage.py migrate
7. Create Django Superuser
python manage.py createsuperuser
8. Run the Development Server
python manage.py runserver

Open the website:

http://127.0.0.1:8000/

Django Admin:

http://127.0.0.1:8000/admin/
🗄️ Database Models

The portfolio uses Django models to manage content dynamically.

Profile

Stores:

Name
Professional Title
Email
Bio
Profile Image
Phone
Location
GitHub
LinkedIn
Skill

Stores:

Skill Name
Project

Stores:

Project Title
Description
Project Image
Technologies
GitHub Link
Live Project Link
Education

Stores:

Degree
Institution
Start Year
End Year
Experience

Stores:

Job Title
Company
Start Date
End Date
Description
Resume

Stores:

Resume Title
Resume File
ContactMessage

Stores:

Name
Email
Subject
Message
Contact
🔐 Django Admin

Django Admin is used as the content management system for the portfolio.

The following sections can be managed from the admin panel:

Profile
Skills
Projects
Education
Experience
Resume
Contact Messages

This allows portfolio content to be updated without manually changing the HTML.

🔄 How It Works
Django Admin
     ↓
SQLite Database
     ↓
Django Models
     ↓
Django Views
     ↓
Context
     ↓
Django Templates
     ↓
HTML + CSS + JavaScript
     ↓
Browser
🎨 UI Features

The frontend includes:

Professional navigation bar
Hero section
About section
Skills section
Project cards
Education section
Experience section
Resume section
Contact section
Footer
Dark/light theme
Responsive layout
Smooth transitions
Hover effects
Mobile-friendly navigation
Responsive images
📱 Responsive Design

The portfolio is designed for:

💻 Desktop
💻 Laptop
📱 Mobile
📟 Tablet
🌙 Dark Mode

The portfolio includes a dark/light mode toggle using JavaScript.

The selected theme can be stored using browser localStorage so that the user's preference remains after refreshing the page.

🖼️ Media Files

The project supports uploading:

Profile images
Project images
Resume PDF

Django media configuration:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
🚀 Future Improvements
 Add project category filtering
 Add project search
 Add contact email notifications
 Add pagination
 Add SEO optimization
 Add Open Graph metadata
 Deploy on Render / AWS
 Connect custom domain
 Add analytics
 Add Django REST API
👨‍💻 Author
Vindhyawasan Singh

Computer Science Engineering Student | Python & Django Developer | Machine Learning & Data Science

Connect With Me
GitHub: https://github.com/vindhyawasan
LinkedIn: Add your LinkedIn profile here
Email: Add your email here
📄 License

This project is open-source and available for educational and personal use.