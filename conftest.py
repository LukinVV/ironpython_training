import pytest
import pytest
from fixture.application import ApplicationHelper


fixture = None

@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture = ApplicationHelper()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.close_app()
    request.addfinalizer(fin)
    return fixture