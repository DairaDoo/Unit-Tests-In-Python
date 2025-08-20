import pytest
from service import UserService, APICLIENT


def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APICLIENT)  # Create a mock API client

    # Mock get_user_data to return a fake user
    mock_api_client.get_user_data.return_value = {"id": 1, "name": "Joe"}

    service = UserService(mock_api_client)  # Inject mock api client

    result = service.get_username(1)  # call method that depends on the mock

    # Assertionts
    assert result == "JOE"  # Check if processing was done correctly
    mock_api_client.get_user_data.assert_called_once_with(
        1
    )  # Check if the mock was called correctly
