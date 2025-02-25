# Django Authentication System

## Overview
This project is a Django-based authentication system that allows users to:
- Sign up with a username and email
- Log in using a username or email
- Reset their password via email
- Change their password when logged in
- Access a dashboard and profile page
- Log out securely

The system ensures proper authentication and authorization for protected pages.

## Features
- **User Authentication**: Login with email or username
- **User Registration**: Sign up with a username, email, and password
- **Password Reset**: Request a password reset link via email
- **Password Change**: Change password while logged in
- **Dashboard**: Accessible only to authenticated users
- **Profile Page**: Displays user information
- **Logout**: Securely log out

## Technologies Used
- **Django 5.1.1** (Web framework)
- **Python 3.12.6**
- **Django’s built-in authentication system**

## Installation
### Prerequisites
Ensure you have Python and Django installed:

### Clone the Repository
```sh
git clone <repository_url>
cd auth_assignment
```

### Apply Migrations
```sh
python manage.py migrate
```

### Create a Superuser (Optional)
```sh
python manage.py createsuperuser
```

### Run the Server
```sh
python manage.py runserver
```

## Usage
1. **Sign up** at `/signup/`
2. **Log in** at `/`
3. **Forgot password?** Request reset at `/forgot-password/`
4. **Reset password** via the email link
5. **Change password** at `/change-password/`
6. **View dashboard** at `/dashboard/`
7. **View profile** at `/profile/`
8. **Logout** at `/logout/`

## Email Configuration (For Password Reset)
Since this project doesn’t use a real email backend, emails are displayed in the terminal.
To enable email debugging:
```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```
After submitting a password reset request, check the terminal for the reset link.

## Project Structure
```
├── accounts/  # Authentication app
│   ├── templates/accounts/  # HTML templates
│   ├── views.py  # Class-based views
│   ├── urls.py  # URL routing
├── auth_assignment/  # Main project folder
│   ├── settings.py  # Django settings
│   ├── urls.py  # Project URLs
├── db.sqlite3  # SQLite database
├── manage.py  # Django management script
```

