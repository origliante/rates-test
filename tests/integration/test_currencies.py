import vcr
import pytest

import api


@pytest.fixture
def client():
    client = api.app.test_client()
    yield client


@vcr.use_cassette('tests/integration/get_currencies.yml')
def test_currencies(client):
    rv = client.get('/currencies')
    assert b'United States Dollar' in rv.data


