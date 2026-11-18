from day34 import ExpenseBook

def test_save_then_load_round_trip(tmp_path):
    path = tmp_path / "expenses.json"
    book = ExpenseBook()
    book.add("tea", 20)
    book.add("bus", 50)
    book.save(path)

    loaded = ExpenseBook()
    loaded.load(path)

    assert len(loaded.expenses) == 2
    assert loaded.expenses[1].item == "bus"
    assert loaded.expenses[1].amount == 50

def test_load_missing_file_gives_empty_book(tmp_path):
    book = ExpenseBook()
    book.load(tmp_path / "no_such_file_json")
    assert book.expenses == []