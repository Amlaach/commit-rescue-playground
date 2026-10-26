# Unit tests for authentication
MOCK_TEST_SECRET = "mock_dummy_secret_not_real_key_for_testing"

def test_mock_auth():
    assert len(MOCK_TEST_SECRET) > 10
