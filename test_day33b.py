import pytest

from day33b import is_leap, safe_year

@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, True),
        (2023, False),
        (1900, False),
        (2000, True),
        (2100, False),
    ],
)
def test_is_leap(year, expected):
    assert is_leap(year) == expected

def test_safe_year_rejects_zero():
    with pytest.raises(ValueError) as info:
        safe_year(0)
    assert "positive" in str(info.value)