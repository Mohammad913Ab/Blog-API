# 📰 Blog API

A powerful blog API built with Django Rest Framework, supporting user registration, JWT authentication, post creation with media (image or short video), nested comments, and documentation via Swagger.


---

## 🚀 Features

- User registration & JWT authentication
- Create, update, delete, and list posts
- Nested comment system (reply to comments)
- Post categorization
- Upload image or video (less than 1 minute)
- API documentation with Swagger & Redoc


---

## ⚙️ Tech Stack

- Python 3.11+
- Django 5
- Django REST Framework
- drf-spectacular
- SimpleJWT


---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/blog-api.git
cd blog-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver
```


---

## 🔐 JWT Authentication

### Register
```
POST /api/account/register/
```

### Obtain Token
```
POST /api/token/
```

### Refresh Token
```
POST /api/token/refresh/
```

Send access token in headers:
```
Authorization: Bearer <your_access_token>
```


---

## 📁 Media Upload

When creating a post, you can upload either an image or a video under 1 minute:
```
POST /api/posts/
```
Use `multipart/form-data` for uploads.


---

## 📚 API Documentation

- Swagger UI → `/api/docs/swagger/`
- Redoc → `/api/docs/redoc/`
- Raw OpenAPI → `/api/schema/`


---

## 🧪 Sample Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/posts/` | List all posts |
| `POST` | `/api/posts/` | Create a new post |
| `PATCH` | `/api/posts/{id}/` | Edit a post |
| `DELETE` | `/api/posts/{id}/` | Delete a post |
| `POST` | `/api/comments/` | Add or reply to comment |
| `GET` | `/api/categories/` | List categories |


---

## 📦 License

This project is licensed under the MIT License.

