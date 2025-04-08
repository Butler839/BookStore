# 📚 BookStore - Django E-Commerce App

A full-stack bookstore application built with **Django**, featuring full user auth, shopping cart functionality, Stripe integration, and a clean templating system for dynamic rendering.

---

## 🔗 Live Demo (Optional)

**Frontend + Backend (Django):** (https://book-store5643-32cde4e777bf.herokuapp.com/)

---

## ✨ Features

- **🛒 Shopping Cart** – Add/remove books, view total, checkout with Stripe
- **🔐 Authentication** – Signup, login, logout, view + edit user profile
- **📖 Book Management** – Browse all books, view details, genres
- **💳 Stripe Payments** – Full checkout flow with test/live keys
- **📂 Modular App Design** – `books`, `users`, `cart`, `payments` as separate apps
- **📸 Media Support** – Dynamic book covers with file uploads
- **⚙️ Admin Dashboard** – Manage books, users, and purchases

---

## ⚙️ Tech Stack

- **Python 3.11** + Django 5.x
- SQLite (default dev DB)
- HTML + Django Templating
- CSS (light Bootstrap-style)
- Gunicorn + Heroku-ready
- Virtualenv / Pip (`requirements.txt` included)

---

## 🛠 Running Locally

### 1. Clone the repo
```bash
git clone https://github.com/Butler839/BookStore
cd BookStore
```

---

### 2. Set up virtual environment
```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

---

### 3. Add a `.env` file

Create a `.env` file in the root with the following:

```ini
SECRET_KEY=your-django-secret-key
STRIPE_SECRET_KEY=your-stripe-secret
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable
STRIPE_ENDPOINT_SECRET=your-stripe-webhook-secret
DEBUG=True
```

---

### 4. Run migrations & seed sample data (optional)

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py shell < load_books.py  # optional dummy data
```

---

### 5. Run the server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 🔐 Admin Access

```bash
http://127.0.0.1:8000/admin/
```

Use your superuser credentials to log in.

---


---


---


---

## 📌 Notes

- Make sure `.env` is in your `.gitignore`
- Stripe secrets are required to run checkout
- Login and account pages are fully functional
- All views are styled and responsive

---
 ## 🧪 Stripe Checkout (Demo Note)

To test the full Stripe checkout experience, use the live Heroku demo:

👉 [https://your-app-name.herokuapp.com](https://your-app-name.herokuapp.com)

> Stripe keys are securely stored in Heroku and are **not included** in the public repository for security reasons.

If you're running this project locally and want Stripe to work, you'll need to:
1. Create a `.env` file in the root directory.
2. Add your own Stripe keys (test or live) like so:

```ini
STRIPE_SECRET_KEY=your-secret
STRIPE_PUBLISHABLE_KEY=your-pub-key
STRIPE_ENDPOINT_SECRET=your-webhook-secret
```
3. Don't put actual card information it is not meant to checkout fully
