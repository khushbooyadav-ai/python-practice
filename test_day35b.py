import pytest

from day35b import ScoreBoard

@pytest.fixture
def board():
    b = ScoreBoard(100)
    b.add("ana", 60)
    b.add("ravi", 30)
    return b

def test_total(board):
    assert board.total() == 90

def test_to_go(board):
    assert board.to_go() == 10

@pytest.mark.parametrize(
    "extra, expected",
    [
        (9, False),
        (10, True),
    ],
)

def test_reached_boundary(board, extra, expected):
    board.add("zed", extra)
    assert board.reached() is expected

def test_best_of_empty_board_is_none():
    assert ScoreBoard(10).best() is None

@pytest.mark.parametrize("bad", [0, -5])
def test_add_rejects_bad_points(board, bad):
    with pytest.raises(ValueError) as info:
        board.add("x", bad)
    assert "positive" in str(info.value)
