import pytest
from string_editor import add, capital, up, reverse


def test_add():
    assert add('a', 'b') == 'ab'
    assert add(2, 3) =='23'
    assert add('a', 1, 'b') == 'a1b'
    assert add(1.5, 'a') =='1.5a' # новый тест с числом с плавающей точкой


def test_capital():
    assert capital('aaa') == 'Aaa'
    assert capital('AAA') == 'Aaa'
    assert capital('123') == '123'


def test_up():
    assert up('aaa') == 'AAA'
    assert up('AAA') == 'AAA'
    assert up('123') == '123'


def test_reverse():
    assert reverse('abc') == 'cba'
    assert reverse(123) == '321'
    assert reverse(1.25) == '52.1'


def test_not_string():
    with pytest.raises(ValueError):
        capital(1)
        up(1)

