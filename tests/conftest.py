import pytest
from crawler_tester import create_app


@pytest.fixture()
def app():
    app = create_app()
    yield app
