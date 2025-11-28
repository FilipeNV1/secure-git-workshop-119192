import os
import sys
import unittest

# Add app directory to sys.path for import
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../app")),
)

import get_wheater  # noqa: E402


def test_get_api_key_and_base_url(tmp_path, monkeypatch):
    # Create a temporary config.ini file
    config_content = (
        "[openweathermap]\napi_key = testkey\n" "base_url = http://testurl\n"
    )
    config_path = tmp_path / "config.ini"
    config_path.write_text(config_content)

    # Monkeypatch the config file location
    monkeypatch.chdir(tmp_path)

    # Test get_api_key
    api_key = get_wheater.get_api_key()
    unittest.TestCase().assertEqual(api_key, "testkey")

    # Test get_base_url
    base_url = get_wheater.get_base_url()
    unittest.TestCase().assertEqual(base_url, "http://testurl")
