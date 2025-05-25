# Flask Test App

A minimal and modular Flask application that demonstrates how to integrate SQLAlchemy for database operations and Pytest for backend unit testing. This project uses a simple user model, includes one API route for user creation, and is fully testable with an in-memory SQLite test database.

---

## 📦 Features

- 🐍 Flask application factory pattern  
- 🛢 SQLAlchemy ORM integration  
- 🧪 Unit testing with Pytest and Flask's test client  
- 🧩 Clean, modular structure for scalability  
- ⚙️ Separate configurations for development and testing environments

---

## 🗂 Project Structure

```

flask\_test\_app/
├── app.py              # App factory and DB setup
├── config.py           # Configurations for dev and test
├── models.py           # SQLAlchemy models
├── routes.py           # Flask routes (e.g., create user)
├── test\_app.py         # Pytest test cases
└── requirements.txt    # Python dependencies

````

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/nitinkumar30/flask-sqlalchemy-starter.git
cd flask-test-app
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔧 Running the App

### Start the Flask development server:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Or on Windows CMD:

```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

---

## 🌐 Test the API

Open your browser or Postman:

```
GET http://127.0.0.1:5000/create_user/testuser
```

You should see:

```
User testuser created
```

---

## ✅ Running Tests

Run the tests using Pytest:

```bash
pytest -s test_app.py
```

Use `-s` to show `print()` output during the test run.

---

## 📄 Example Test Case

```python
def test_create_user(client_app):
    client, app = client_app

    response = client.get('/create_user/testuser')
    assert response.status_code == 200
    assert b"User testuser created" in response.data

    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None
```

---

## 🛠 Tech Stack

* **Flask** – lightweight Python web framework
* **Flask-SQLAlchemy** – ORM for database management
* **Pytest** – testing framework
* **SQLite** – simple file-based database (in-memory for testing)

---

## 🧩 Future Improvements

* Add Flask-Migrate for migrations
* Add JWT-based user authentication
* Dockerize for deployment
* Support for PostgreSQL and MySQL

---


## 🤝 Contributing

Feel free to fork this repo, open issues, or submit pull requests. Contributions are welcome!

