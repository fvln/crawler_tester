import pytest

from crawler_tester.http_codes import CODES_REDIRECT


@pytest.mark.parametrize("code", CODES_REDIRECT)
def test_status_ok(client, code):
    res = client.get(f"/status/{code}")
    assert res.status_code == code
    assert res.text == f"Status code {code}"


@pytest.mark.parametrize("code", [202, 403, 500])
def test_status_ko(client, code):
    res = client.get(f"/status/{code}")
    assert res.status_code == 404
    assert "reponse code should be in range [300,308]" in res.text
