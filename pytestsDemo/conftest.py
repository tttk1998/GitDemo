import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be excuting first")
    yield #yielder step will be executed after your test execution is complete
    print("I will executed last")