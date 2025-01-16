import pytest
from app.utils.functions import captalize
from app import create_app


@pytest.fixture
def app():
    """
    Creates and configures a new app instance for each test.
    """
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """
    Provides a test client for the Flask app.
    """
    with app.test_client() as client:
        yield client


def test_main_get(client):
    """
    Test the root route (/) to ensure it renders correctly.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello Flavio!" in response.data


def test_main_get_with_name(client):
    """
    Test the dynamic route /<name> to ensure it renders correctly.
    """
    response = client.get("/john")
    assert response.status_code == 200
    assert b"Hello John!" in response.data


def test_captalize_function():
    """
    Test the 'captalize' utility function.
    """
    assert captalize("flavio") == "Flavio"
    assert captalize("john") == "John"
    assert captalize("DOE") == "Doe"
