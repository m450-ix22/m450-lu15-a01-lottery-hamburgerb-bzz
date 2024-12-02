import pytest

from lottery import create_ticket, select_numbers, print_ticket
from ticket import Ticket


class MockPerson:
    def __init__(self, balance):
        self.balance = balance


@pytest.fixture
def person():
    return MockPerson(balance=50.0)


@pytest.fixture
def ticket():
    return Ticket(0, [])


def test_create_ticket_sufficient_balance(monkeypatch, person):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    create_ticket(person)
    assert person.balance == 48.0


def test_create_ticket_insufficient_balance(person):
    person.balance = 1.0
    create_ticket(person)
    assert person.balance == 1.0


def test_select_numbers(monkeypatch, ticket):
    inputs = iter(['1', '2', '3', '4', '5', '6', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    select_numbers(ticket)
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]
    assert ticket.joker == 1


def test_print_ticket(capsys, ticket):
    ticket.numbers = [1, 2, 3, 4, 5, 6]
    ticket.joker = 1
    print_ticket(ticket)
    captured = capsys.readouterr()
    assert "X" in captured.out
    assert "Jokerzahl:  1" in captured.out
