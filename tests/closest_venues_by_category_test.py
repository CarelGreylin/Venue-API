"""Unit tests for the closest_venues_by_category function.

Testing using pytest.
"""
from src.error import InputError
import json
import json
import requests
import tests.expected
from src.config import URL

def test_documentation_one():
    expected = json.loads(tests.expected.TEST_1)
    latitude = 49
    longitude = -97
    response = requests.get(
        f"{URL}/venues/by_category?latitude={latitude}&longitude={longitude}"
    )
    assert expected == response.json()

def test_documentation_two():
    expected = json.loads(tests.expected.TEST_2)
    latitude = 49
    longitude = -97
    limit = 3
    response = requests.get(
        f"{URL}/venues/by_category?latitude={latitude}\
            &longitude={longitude}&limit={limit}"
    )
    assert expected == response.json()

def test_bad_request_type():
    latitude = 49
    longitude = -97
    limit = "string"
    response = requests.get(
            f"{URL}/venues/by_category?latitude={latitude}\
                &longitude={longitude}&limit={limit}"
        )
    assert response.status_code == InputError.code

def test_bad_request_missing():
    latitude = 49
    response = requests.get(f"{URL}/venues/by_category?latitude={latitude}")
    assert response.status_code == InputError.code

def test_null():
    expected = []
    latitude = 49
    longitude = -97
    limit = 0
    response = requests.get(
        f"{URL}/venues/by_category?latitude={latitude}\
            &longitude={longitude}&limit={limit}"
    )
    assert expected == response.json()

def test_negative_lim():
    expected = []
    latitude = 49
    longitude = -97
    limit = -3
    response = requests.get(
        f"{URL}/venues/by_category?latitude={latitude}\
            &longitude={longitude}&limit={limit}"
    )
    assert response.status_code == InputError.code
