import pytest

from day32b import MarksBook

def make_book():
    book = MarksBook()
    book.add("asha", 80)
    book.add("ravi", 60)
    return book

def test_average():
    book = make_book()
    assert book.average() == 70

def test_average_of_empty_book_raises():
    with pytest.raises(ValueError):
        MarksBook().average() == 0

def test_find_return_the_student():
    book = make_book()
    assert book.find("asha").marks == 80

def test_delete_removes_student():
    book = make_book()
    book.delete("asha")
    assert book.average() == 60

def test_delete_missing_raises():
    book = make_book()
    with pytest.raises(ValueError):
        book.delete("zoya")

@pytest.fixture
def book():
    b = MarksBook()
    b.add("asha", 80)
    b.add("ravi", 60)
    return b

def test_find_with_fixture(book):
    assert book.find("asha").marks == 80