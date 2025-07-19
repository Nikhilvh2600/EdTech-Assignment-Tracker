
# 📘 EdTech Assignment Tracker

A simple Django-based EdTech system that allows **Teachers** to post assignments and **Students** to submit them. Includes JWT-based authentication, SQLite storage, and a clean frontend built with HTML, CSS (Bootstrap), and JavaScript.

---

## 🚀 Features

- 🔒 Role-based Signup/Login (Student, Teacher)
- 📝 Teachers can:
  - Create assignments
  - View submissions
- 📤 Students can:
  - View assignment list
  - Submit assignments
- 🪪 JWT token-based authentication
- 📁 File upload (optional)
- 📄 DRF browsable API support

---

## 📁 Project Structure

```
edtech_tracker/
│
├── assignment_tracker/       # Django app
│   ├── models.py             # Custom User, Assignment, Submission
│   ├── serializers.py        # DRF Serializers
│   ├── views.py              # API Views
│   ├── urls.py               # API routes
│   └── permissions.py        # Role-based permissions
│
├── edtech_tracker/           # Project settings
│   └── settings.py
│
├── frontend/                 # HTML/JS/CSS Frontend
│   ├── signup.html
│   ├── teacher.html
│   ├── student.html
│   └── submissions.html
│
├── manage.py
└── requirements.txt
```

---

## 🛠️ Setup Instructions

### 1. Clone & navigate
```bash
git clone <your-repo-url>
cd edtech_tracker
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the server
```bash
python manage.py runserver
```

Now, the backend will run at: http://127.0.0.1:8000

---

## 🌐 API Endpoints

| Method | Endpoint                        | Description                  | Role     |
|--------|----------------------------------|------------------------------|----------|
| POST   | /signup/                        | Register a user              | All      |
| POST   | /login/                         | Login and get JWT token      | All      |
| POST   | /assignments/                   | Create assignment            | Teacher  |
| GET    | /assignments/                   | View all assignments         | Student  |
| POST   | /assignments/<id>/submit/       | Submit assignment            | Student  |
| GET    | /assignments/<id>/submissions/  | View all submissions         | Teacher  |

---

## 🖥️ Frontend

> Located in `frontend/`

| File            | Purpose                         |
|-----------------|---------------------------------|
| signup.html     | Signup/Login form               |
| teacher.html    | Form to create assignments      |
| student.html    | Form to submit assignment       |
| submissions.html| Teacher view of submissions     |

> ⚠️ Ensure backend is running at `http://127.0.0.1:8000`. JS uses `fetch()` to interact with API.

---

## 🔐 JWT Authentication

- On login, the user gets a token.
- Frontend uses `Authorization: Bearer <token>` header in every request after login.

Example (in JS):
```javascript
headers: {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ' + localStorage.getItem('token')
}
```

---

## 💡 Future Enhancements

- ✅ Assignment deadline
- 🖼️ File preview/download
- 📊 Analytics dashboard for teachers
- 📱 Mobile responsive UI
- 📚 Swagger or ReDoc API Docs

---

## 👨‍💻 Author

**Nikhil V**  
A full-stack intern passionate about Django, REST APIs, and frontend integration.
# EdTech-Assignment-Tracker
