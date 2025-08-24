import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from src.module import foo

def test_foo_1():
    assert foo(1, 2) == 3
    assert foo(-1, 1) == 0
    assert foo(0, 0) == 0
