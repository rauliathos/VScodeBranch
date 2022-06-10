import pytest
from program import list_of_squares

def test_zero():
    assert list_of_squares.list_of_squares(0)=={}

def test_one():
    assert list_of_squares.list_of_squares(1)=={1:1}


def test_two():
    assert list_of_squares.list_of_squares(2)=={1:1, 2:4}
#kjhgkjhgjh
def test_three():
    assert list_of_squares.list_of_squares(3)=={1:1, 2:4, 3:9}