import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as info:
        10 / 0
    assert "division" in str(info.value)