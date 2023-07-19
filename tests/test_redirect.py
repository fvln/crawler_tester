from flask import url_for
import pytest

from crawler_tester.http_codes import CODES_REDIRECT


@pytest.mark.parametrize("code", CODES_REDIRECT)
def test_redirect_http_nofollow_ok(client, code):
    res = client.get(f"/redirect/http-{code}")
    assert res.status_code == code
    assert res.text == "ok"


@pytest.mark.parametrize("code", CODES_REDIRECT)
def test_redirect_http_follow_ok(client, code):
    res = client.get(f"/redirect/http-{code}", follow_redirects=True)
    assert res.request.path == url_for("landing")
    assert res.text == "Redirect successful"


@pytest.mark.parametrize("code", [202, 403, 500])
def test_redirect_http_ko(client, code):
    res = client.get(f"/redirect/http-{code}")
    assert res.status_code == 404
