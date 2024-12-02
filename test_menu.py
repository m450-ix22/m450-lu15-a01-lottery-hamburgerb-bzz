from menu import show_menu, select_menu


def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert "Lotto" in captured.out
    assert "A) Konto Ein- und Auszahlungen tätigen" in captured.out
    assert "B) Lottotipps abgeben" in captured.out
    assert "Z) Beenden" in captured.out


def test_select_menu_valid_A(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    assert select_menu() == 'A'


def test_select_menu_valid_B(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'B')
    assert select_menu() == 'B'


def test_select_menu_valid_Z(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Z')
    assert select_menu() == 'Z'


def test_select_menu_invalid_then_valid(monkeypatch):
    inputs = iter(['X', 'A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_menu() == 'A'
