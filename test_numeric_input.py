import pytest

from numeric_input import read_int, read_float


@pytest.fixture
def mock_input(monkeypatch):
    def _mock_input(inputs):
        input_iter = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    return _mock_input


def test_read_int_valid_input(mock_input):
    mock_input(['5'])
    assert read_int('Enter a number: ', 1, 10) == 5


def test_read_int_below_min(mock_input):
    mock_input(['0', '1'])
    assert read_int('Enter a number: ', 1, 10) == 1


def test_read_int_above_max(mock_input):
    mock_input(['11', '10'])
    assert read_int('Enter a number: ', 1, 10) == 10


def test_read_int_non_numeric(mock_input):
    mock_input(['a', '5'])
    assert read_int('Enter a number: ', 1, 10) == 5


def test_read_int_multiple_invalid(mock_input):
    mock_input(['a', '0', '11', '5'])
    assert read_int('Enter a number: ', 1, 10) == 5


def test_read_float_valid_input(mock_input):
    mock_input(['5.5'])
    assert read_float('Enter a number: ', 1.0, 10.0) == 5.5


def test_read_float_below_min(mock_input):
    mock_input(['0.5', '1.0'])
    assert read_float('Enter a number: ', 1.0, 10.0) == 1.0


def test_read_float_above_max(mock_input):
    mock_input(['10.5', '10.0'])
    assert read_float('Enter a number: ', 1.0, 10.0) == 10.0


def test_read_float_non_numeric(mock_input):
    mock_input(['a', '5.5'])
    assert read_float('Enter a number: ', 1.0, 10.0) == 5.5


def test_read_float_multiple_invalid(mock_input):
    mock_input(['a', '0.5', '10.5', '5.5'])
    assert read_float('Enter a number: ', 1.0, 10.0) == 5.5
