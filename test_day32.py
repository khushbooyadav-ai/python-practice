import pytest

from day32 import ExpenseBook


def make_book():
    book = ExpenseBook()
    book.add("tea", 20)
    book.add("bus", 50)
    return book


def test_total():
    book = make_book()
    assert book.total() == 70


def test_total_of_empty_book_is_zero():
    assert ExpenseBook().total() == 0


def test_find_returns_the_expense():
    book = make_book()
    assert book.find("bus").amount == 50


def test_find_missing_returns_none():
    assert make_book().find("pen") is None


def test_delete_removes_expense():
    book = make_book()
    book.delete("tea")
    assert book.total() == 50


def test_delete_missing_raises():
    book = make_book()
    with pytest.raises(ValueError):
        book.delete("pen")
