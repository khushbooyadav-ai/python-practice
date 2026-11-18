import json

import pytest

def test_bad_json_raises(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("not json at all")
    with pytest.raises(json.JSONDecodeError):
        json.loads(path.read_text())