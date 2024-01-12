from flask import url_for
import pytest

from crawler_tester.http_codes import CODES_REDIRECT


def test_redirect_chain_counter_zero(client):
    res = client.get(f"/redirect-chain/0")
    assert res.status_code == 200
    assert res.text == "ok"


@pytest.mark.parametrize("counter", [1, 10])
def test_redirect_chain(client, counter):
    res = client.get(f"/redirect-chain/{counter}", follow_redirects=True)
    assert res.request.path == url_for("landing")
    assert res.text == "Redirect successful"

