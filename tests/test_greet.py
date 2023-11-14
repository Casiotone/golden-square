from lib.greet import *

def test_greet_given_name():
    result = greet('Henry')
    assert result == "Hello, Henry!"