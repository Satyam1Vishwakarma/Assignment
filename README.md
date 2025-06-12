# Flask + MongoDB REST API

A scalable, modular REST API built with Flask and MongoDB, containerized using Docker.

## 🧩 Features

- Full CRUD for `User` resource (`id`, `name`, `email`, `password`)
- MongoDB via `Flask-PyMongo`
- Input validation with `Marshmallow`
- Secure password hashing using `werkzeug.security`
- Organized using Flask app-factory and Blueprints
- Configurable via `.env` and `python-dotenv`
- Containerized with Docker and Docker Compose

---

## 📋 API Endpoints

| Method | Endpoint          | Description             |
|--------|-------------------|-------------------------|
| GET    | `/api/users`      | List all users          |
| GET    | `/api/users/<id>` | Get user by ID          |
| POST   | `/api/users`      | Create a new user       |
| PUT    | `/api/users/<id>` | Update user by ID       |
| DELETE | `/api/users/<id>` | Delete user by ID       |

---

## 🚀 Setup and Run Instructions

### Prerequisites

- Docker & Docker Compose installed  
  *(Follow [Docker's official guide](https://docs.docker.com/get-docker/))*

### 1. Clone the repository

```bash
git clone https://github.com/Satyam1Vishwakarma/Assignment.git
cd Assignment
```

### 2. Create a .env file
```bash
MONGO_URI=mongodb://mongo:27017/flask_mongo_api
SECRET_KEY=super-secret
```

### 3. Build & run containers
```bash
docker-compose up --build
```
