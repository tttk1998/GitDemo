import pytest


@pytest.mark.smoke
def test_firstCreditCard():
    print("Hello")

@pytest.mark.xfail
def test_SecondCreeditCard():
    print("Thanh Kieu")