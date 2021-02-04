import os
import tempfile
import pytest

from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            pass
        yield client

    app.config['TESTING'] = True
