import pytest
from string_editor import add, capital, up

def test_add():
    assert add('a', 'b') == 'ab'
    assert add(2, 3) =='23'
    assert add('a', 1, 'b') == 'a1b'

def test_capital():
    assert capital('aaa') == 'Aaa'
    assert capital('AAA') == 'AAA'
    assert capital('123') == '123'
    
def test_up():
    assert capital('aaa') == 'AAA'
    assert capital('AAA') == 'AAA'
    assert capital('123') == '123'

def test_not_string():
    with pytest.raises(ValueError):
        capital(1)
        up(1)

