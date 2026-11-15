import pytest

@pytest.fixture
def numbers():
    return [3, 1, 2]

def test_sorted(numbers):
    assert sorted(numbers) == [1, 2, 3]

def test_original_unchanged(numbers):
    sorted(numbers)
    assert numbers == [3, 1, 2]