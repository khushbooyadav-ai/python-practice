import json

import pytest

from day34b import MarksBook

def test_save_then_load_round_trip(tmp_path):
    path = tmp_path / "students.json" 
    book = MarksBook()
    book.add("asha", 80)
    book.add("ravi", 50)
    book.save(path)

    loaded = MarksBook()
    loaded.load(path)

    assert len(loaded.students) == 2
    assert loaded.students[1].name == "ravi"
    assert loaded.students[1].marks == 50

def test_load_missing_file_gives_empty_book(tmp_path):
    book = MarksBook()
    book.load(tmp_path / "no_such_file_json")
    assert book.students == []

def test_load_bad_file_raises(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("not json at all")
    with pytest.raises(json.JSONDecodeError):
        MarksBook().load(path)