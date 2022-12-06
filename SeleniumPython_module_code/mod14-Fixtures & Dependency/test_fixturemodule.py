import pytest


@pytest.fixture(scope='module')
def setup():
    global num1, num2
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    yield
    print("Output : " + str(result))

def test_add(setup):
    global result
    result = int(num1)+int(num2)

def test_difference(setup):
    global result
    result = int(num1)-int(num2)

#selenium code =