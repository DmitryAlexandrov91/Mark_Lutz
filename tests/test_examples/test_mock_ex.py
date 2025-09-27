"""Mock request example."""
from http import HTTPStatus
import pytest
from unittest.mock import MagicMock
from pytest_mock import MockerFixture


@pytest.fixture
def mock_requests_get(mocker: MockerFixture) -> MagicMock:
    response = MagicMock()
    response.status_code = HTTPStatus.NOT_FOUND
    response.json.return_value = {}
    return mocker.patch('requests.get', return_value=response)


def test_mocker_request(mock_requests_get: MagicMock) -> None:
    google_url = 'www.google.com'
    response = mock_requests_get(google_url)

    mock_requests_get.assert_called_once_with(google_url)

    assert response.status_code == HTTPStatus.NOT_FOUND
