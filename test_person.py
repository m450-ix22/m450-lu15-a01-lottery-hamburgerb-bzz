import pytest

from person import Person


@pytest.fixture
def person_with_balance():
    return Person('Max', '1234', 10.0)


def test_person_constructor(person_with_balance):
    p = person_with_balance
    assert p.givenname == 'Max'
    assert p.password == '1234'
    assert p.balance == 10.0


def test_person_givenname(person_with_balance):
    p = person_with_balance
    p.givenname = 'John'
    assert p.givenname == 'John'


def test_person_password(person_with_balance):
    p = person_with_balance
    p.password = '5678'
    assert p.password == '5678'


def test_person_balance(person_with_balance):
    p = person_with_balance
    p.balance = 20.0
    assert p.balance == 20.0


def test_person_balance_invalid(person_with_balance):
    p = person_with_balance
    with pytest.raises(ValueError):
        p.balance = 'invalid_balance'
