import pytest

import ticket


def test_ticket_constructor():
    t = ticket.Ticket(0, list())
    assert t.joker == 0
    assert t.numbers == list()

def test_ticket_joker():
    t = ticket.Ticket(0, list())
    t.joker = 1
    assert t.joker == 1

def test_ticket_joker_wrong_input():
    t = ticket.Ticket(0, list())
    with pytest.raises(ValueError):
        t.joker = 'a'

def test_ticket_numbers():
    t = ticket.Ticket(0, list())
    t.numbers = [1, 2, 3, 4, 5, 6]
    assert t.numbers == [1, 2, 3, 4, 5, 6]

def test_ticket_numbers_empty():
    t = ticket.Ticket(0, list())
    t.numbers = []
    assert t.numbers == []