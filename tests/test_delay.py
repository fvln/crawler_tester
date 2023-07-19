from bs4 import BeautifulSoup
from io import BytesIO
import pytest
import time


GOOD_DELAY = [0.25, 0.5, 1.0]
DELAY_MARGIN = 0.100
BAD_DELAY = [-12, 0.00005, 99999, "test"]


@pytest.mark.parametrize("delay", GOOD_DELAY)
def test_delayed_page_ok(client, delay):
    t1 = time.time()
    res = client.get(f"/delay/page?delay={int(delay*1000)}")
    dt = time.time() - t1

    assert (dt - delay) <= (delay + DELAY_MARGIN)
    assert f"Cette page s'est chargée en {float(delay)} seconde(s)" in res.text


@pytest.mark.parametrize("delay", BAD_DELAY)
def test_delayed_page_ko(client, delay):
    res = client.get(f"/delay/page?delay={delay}")

    assert res.status_code == 400
    assert res.text in "Invalid delay"


@pytest.mark.parametrize("delay", GOOD_DELAY)
def test_delayed_image(client, delay):
    img_path = "crawler_tester/static/cats.jpg"
    t1 = time.time()
    res = client.get(f"/delay/image?delay={int(delay*1000)}")
    dt = time.time() - t1

    with open(img_path, "rb") as img:
        imgIO = BytesIO(img.read())
    imgIO.seek(0)

    assert (dt - delay) <= (delay + DELAY_MARGIN)
    assert res.data == imgIO.read()


@pytest.mark.parametrize("count", [1, 5, 10])
def test_delayed_content_ok(client, count):
    res = client.get(f"/delay/contents?count={int(count)}")

    soup = BeautifulSoup(res.text, "html.parser")
    imgs = soup.find_all("img", {"class": "delayed"})

    assert len(imgs) == count
    assert res.status_code == 200


@pytest.mark.parametrize("count", [-10, 9999, 0.0005, "test"])
def test_delayed_content_ko(client, count):
    res = client.get(f"/delay/contents?count={count}")

    assert res.status_code == 400
    assert res.text in "Invalid contents count"
