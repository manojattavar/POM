import pytest


@pytest.fixture()
def setup():
    global num1, num2
    num1 = input("Enter num 1 : ")
    num2 = input("Enter num 2 : ")
    yield
    print("Output : " + str(result))

@pytest.mark.run(order=2)
def test_add(setup):
    global result
    print("addition")
    result = int(num1)+int(num2)


@pytest.mark.run(order=1)
def test_difference(setup):
    global result
    print("Subtraction")
    result = int(num1)-int(num2)

#selenium code =