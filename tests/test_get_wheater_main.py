import builtins
import os
import sys
import unittest

import pytest
from unittest.mock import patch

# Add app directory to sys.path for import
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")),
)

import get_wheater  # noqa: E402


def test_main_usage(capsys):
    test_argv = ["get_wheater.py"]
    with patch.object(sys, "argv", test_argv):
        with pytest.raises(SystemExit) as e:
            get_wheater.main()
        unittest.TestCase().assertIn("Usage", str(e.value))


def test_main_success(monkeypatch, capsys):
    test_argv = ["get_wheater.py", "Lisbon"]
    monkeypatch.setattr(get_wheater, "argv", test_argv)
    monkeypatch.setattr(get_wheater, "get_api_key", lambda: "fakekey")
    monkeypatch.setattr(
        get_wheater,
        "get_base_url",
        lambda: "https://api.openweathermap.org/data/2.5",
    )
    monkeypatch.setattr(
        get_wheater,
        "get_weather",
        lambda base_url, api_key, city: {"main": {"temp": 20.0}},
    )
    monkeypatch.setattr(builtins, "input", lambda _: "30")
    try:
        get_wheater.main()
    except SystemExit as e:
        print("sys.argv during failure:", sys.argv)
        pytest.fail(f"Unexpected SystemExit: {e}")
    out, _ = capsys.readouterr()
    unittest.TestCase().assertIn("30 - currentTemp is:", out)
    unittest.TestCase().assertIn("10.0", out)
