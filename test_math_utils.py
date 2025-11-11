import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from math_utils import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(4, 5) == 20
