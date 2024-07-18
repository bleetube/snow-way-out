import pytest
from os import environ
from snow_way_out.ServiceNowAPI import ServiceNowAPI

@pytest.fixture(scope="module")
def sn_api():
    snow_endpoint = environ.get('SNOW_ENDPOINT') or input("Please enter the ServiceNow endpoint URL: ")
    snow_api_username = environ.get('SNOW_API_USERNAME') or input("Please enter the ServiceNow API username: ")
    snow_api_password = environ.get('SNOW_API_PASSWORD') or input("Please enter the ServiceNow API password: ")
    return ServiceNowAPI(snow_endpoint, snow_api_username, snow_api_password)

def test_authentication(sn_api):
    assert sn_api.test_authentication(), "Authentication failed."

def test_version(sn_api):
    version_info = sn_api.get_version()
    assert version_info, "Failed to retrieve ServiceNow version."

    # Check that the version is within sane bounds
    version_parts = version_info.split('-')
    assert len(version_parts) >= 3, "Version format is unexpected."

    # Optional: Check specific version parts
    # Here we just log them for manual verification if needed
    print(f"Version parts: {version_parts}")

if __name__ == "__main__":
    pytest.main()
