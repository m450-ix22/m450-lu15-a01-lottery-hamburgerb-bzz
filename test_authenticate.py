import pytest

from authenticate import login, load_people
from person import Person


@pytest.fixture
def people_list():
    return [
        Person('Inga', 'geheim', 14.00),
        Person('Peter', 'secrät', 7.00),
        Person('Beatrice', 'passWORT', 23.00)
    ]


def test_load_people(monkeypatch, people_list):
    monkeypatch.setattr('authenticate.load_people', lambda: people_list)
    loaded_people = load_people()
    assert len(loaded_people) == 3
    assert loaded_people[0].givenname == 'Inga'
    assert loaded_people[1].givenname == 'Peter'
    assert loaded_people[2].givenname == 'Beatrice'


def test_login_valid_password(monkeypatch, people_list):
    monkeypatch.setattr('authenticate.load_people', lambda: people_list)
    inputs = iter(['geheim', 'secrät', 'passWORT'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    person = login()
    assert person.givenname == 'Inga'

    person = login()
    assert person.givenname == 'Peter'

    person = login()
    assert person.givenname == 'Beatrice'


def test_login_invalid_password(monkeypatch, people_list):
    monkeypatch.setattr('authenticate.load_people', lambda: people_list)
    inputs = iter(['wrong', 'geheim'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    person = login()
    assert person.givenname == 'Inga'
