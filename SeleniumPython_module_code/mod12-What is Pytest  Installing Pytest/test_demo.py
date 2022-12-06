#module name should be prefixed : test_ , batch,
#function - def - test_
#class name should start with Test
import pytest


@pytest.mark.skip("Skipping the test case")
def test_demo():
    print("Demostrating test cases")

def test_a():
    print("a")

def test_b():
    print("b")



