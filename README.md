# Doctor-Patient Portal

This is a Django-based web application that provides signup and login functionality for two types of users: **Doctors** and **Patients**. Upon login, users are redirected to their respective dashboards.

## Features

- User authentication (Signup, Login, Logout)
- Separate dashboards for Doctors and Patients
- Profile Picture upload (without using Pillow)
- Styled using separate CSS files for each page
- Responsive and modern UI design

## File Structure

```
Signup_Signin_Form/
├── manage.py
├── db.sqlite3
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── accounts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── templates/
    │   └── accounts/
    │       ├── signup.html
    │       ├── login.html
    │       ├── doctor_dashboard.html
    │       └── patient_dashboard.html
    └── static/
        └── accounts/
            ├── Styles_Signup.css
            ├── Styles_login.css
            ├── Styles_Doctor_Dashboard.css
            └── Styles_Doctor_Patient.css

├── File_Structure.txt
└── README.md

```

## Installation

### Prerequisites

- Python 3.x
- Django 4.x
- Git

### Steps to Run Locally

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Rahul-D-Rao/Signup_Signin_Form.git
   cd Signup_Signin_Form
   ```
2. **Create Virtual Environment** (optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate  # For Windows use: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install django
   ```
4. **Run Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/Signup` in your browser.



## Static Files Configuration
Ensure the following settings are in `settings.py` to properly serve static files:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

For production, collect static files using:
```sh
python manage.py collectstatic
```

## Features
- **User Authentication** (Signup, Login, Logout)
- **Profile Picture Uploads** (Default fallback provided)
- **Separate Dashboards for Doctors & Patients**
- **Stylized UI with Individual Stylesheets**

## Troubleshooting
- If static files do not load, ensure you are using `{% load static %}` in templates.
- Check MIME type errors in browser console; verify the correct linking of CSS files.
- Use `python manage.py runserver --insecure` to temporarily serve static files in development.

## Contribution Guidelines
- Fork the repository and create a new branch.
- Make necessary changes and test locally.
- Submit a pull request with a descriptive commit message.

## License
This project is licensed under the MIT License.


