#you can mark (tag) test @pytest.mark.smoke and then run with -m
#you can skip test with @pytest.mark.skip
#@pytest.mark.xfail
#fixtures are used as setup and tear down methods for test cases - conftest file to generalize
#fixture and make it available to all test case
import pytest


@pytest.mark.smoke
@pytest.mark.skip

def test_firstProgram():
    msg = "Hello"  #operation
    assert msg == "Hi", "Test failed because strings do not match"
    #print("Thanh Kieu")

def test_SecondCreeditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

#Command run selected Pytests from set of Tests (Terminal): pytest -k CreditCard -v -s O:\Pycharm\TPosWeb\pytestsDemo


@pytest.fixture()
def setup():
    print("I will be excuting first")

def test_fixtureDemo(setup):
    print("I will be execute steps in fixtureDemo method")