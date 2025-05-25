import pytest
from app import create_app, db
from models import User
from config import TestConfig


@pytest.fixture
def client():
    app = create_app(TestConfig)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client, app


def test_create_user(client):
    client, app = client  # ✅ Unpack the tuple here

    response = client.get('/create_user/testuser')
    assert response.status_code == 200
    assert b"User testuser created" in response.data

    with app.app_context():
        from models import User
        user = User.query.filter_by(username='testuser').first()
        assert user is not None


