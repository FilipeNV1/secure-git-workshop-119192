import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Add app directory to sys.path for import
sys_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../app"))
sys.path.insert(0, sys_path)

from get_wheater import get_weather  # noqa: E402


def test_get_weather_success():
    # Mock requests.get to return a custom response
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {"main": {"temp": 20.0}}
        mock_get.return_value = mock_response

        base_url = "https://api.openweathermap.org/data/2.5"
        api_key = "fakekey"
        city = "Lisbon"
        result = get_weather(base_url, api_key, city)
        unittest.TestCase().assertIn("main", result)
        unittest.TestCase().assertEqual(result["main"]["temp"], 20.0)


def test_get_weather_failure():
    # Mock requests.get to return a custom response
    with patch("requests.get") as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "cod": "404",
            "message": "city not found",
        }
        mock_get.return_value = mock_response

        base_url = "https://api.openweathermap.org/data/2.5"
        api_key = "fakekey"
        city = "Nowhere"
        result = get_weather(base_url, api_key, city)
        unittest.TestCase().assertEqual(result["cod"], "404")
        unittest.TestCase().assertEqual(result["message"], "city not found")
