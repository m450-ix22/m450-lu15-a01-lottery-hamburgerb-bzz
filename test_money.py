import pytest

from money import transfer_money, select_transaction


class MockPerson:
    def __init__(self, balance):
        self.balance = balance


@pytest.fixture
def person():
    return MockPerson(balance=50.0)


def test_transfer_money_deposit(monkeypatch, person):
    inputs = iter(['E', '20.0', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('numeric_input.read_float', lambda prompt, min_val, max_val: 20.0)
    transfer_money(person)
    assert person.balance == 70.0


def test_transfer_money_withdrawal(monkeypatch, person):
    inputs = iter(['A', '20.0', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('numeric_input.read_float', lambda prompt, min_val, max_val: 20.0)
    transfer_money(person)
    assert person.balance == 30.0


def test_transfer_money_invalid_transaction(monkeypatch, person):
    inputs = iter(['A', '60.0', 'Z']) 
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    monkeypatch.setattr('numeric_input.read_float', lambda prompt, min_val, max_val: 60.0)
    with pytest.raises(ValueError):
        transfer_money(person)


def test_select_transaction_valid(monkeypatch):
    inputs = iter(['A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'A'


def test_select_transaction_invalid_then_valid(monkeypatch):
    inputs = iter(['X', 'E'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_transaction() == 'E'
