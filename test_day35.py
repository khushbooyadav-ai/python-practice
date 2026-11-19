import pytest

from day35 import BudgetBook

@pytest.fixture
def book():
    b = BudgetBook(100)
    b.add("tea", 20)
    b.add("bus", 50)
    return b

def test_total(book):
    assert book.total() == 70

def test_remaining(book):
    assert book.remaining() == 30

@pytest.mark.parametrize(
    "extra, expected",
    [
        (30, False),
        (31,True),
    ],
)

def test_over_budget_boundary(book, extra, expected):
    book.add("pen", extra)
    assert book.over_budget() is expected

def test_biggest(book):
    assert book.biggest().item == "bus"

def test_biggest_of_empty_book_is_none():
    assert BudgetBook(10).biggest() is None

def test_above_yield_matches(book):
    assert[e.item for e in book.above(15)] == ["tea", "bus"]

@pytest.mark.parametrize("bad", [0, -5])
def test_add_rejects_bad_amount(book, bad):
    with pytest.raises(ValueError) as info:
        book.add("x", bad)
    assert "positive" in str(info.value)

def test_bad_limit_raises():
    with pytest.raises(ValueError):
        BudgetBook(0)

def test_save_then_load_round_trip(book, tmp_path):
    path = tmp_path / "budget.json"
    book.save(path)
    loaded = BudgetBook(1)
    loaded.load(path)
    assert loaded.limit == 100
    assert loaded.total() == 70
    assert str(loaded.expenses[1]) == "bus: 50"