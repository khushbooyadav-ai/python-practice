import pytest

from day33 import grade

@pytest.mark.parametrize(
    "marks, expected",
    [
        (100, "A"),
        (80, "A"),
        (79, "B"),
        (60, "B"),
        (59, "C"),
        (40, "C"),
        (39, "F"),
        (0, "F"),
    ],
)
def test_grade(marks, expected):
    assert grade(marks) == expected

@pytest.mark.parametrize("bad", [-1, 101])
def test_grade_rejects_out_of_range(bad):
    with pytest.raises(ValueError) as info:
        grade(bad)
    assert "between 0 and 100" in str(info.value)
