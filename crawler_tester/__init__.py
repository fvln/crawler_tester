from flask import Flask, abort, make_response, request, render_template, send_file
import time


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/landing")
def landing():
    return "Redirect successful"


def redirect_http(status_code=""):
    try:
        http_code = int(status_code)
        if http_code < 300 or http_code > 308:
            raise ValueError("reponse code should be in range [300,308]")
    except Exception as e:
        return make_response(f"Invalid HTTP status response: {e}", 404)

    if http_code == 304:
        # To be implemented
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/304
        abort(501)

    resp = make_response("ok", http_code)
    resp.headers["Location"] = "/landing"
    return resp


def redirect_js(page_name=""):
    try:
        delay = int(request.args.get("delay", "50"))
    except ValueError:
        return make_response(f"Invalid delay", 400)

    return render_template(f"{page_name}.html", delay=delay)


@app.route("/status/<status_code>")
def status(status_code=""):
    allowed_codes = [
        200,  # OK
        201,  # Created
        202,  # Accepted
        203,  # Non-Authoritative Information
        204,  # No Content
        205,  # Reset Content
    ]

    try:
        http_code = int(status_code)
        if http_code < 300 or http_code > 308:
            raise ValueError("reponse code should be in range [300,308]")
    except Exception as e:
        return make_response(f"Invalid HTTP status response: {e}", 404)

    return make_response(f"Status code {http_code}", http_code)


@app.route("/redirect/<type_>")
def redirect(type_=None):
    if type_[:5] == "http-":
        return redirect_http(status_code=type_[5:])

    if type_[:3] == "js-":
        return redirect_js(page_name=type_[3:])

    else:
        abort(404)


@app.route("/delay/page")
def delayed_page():
    try:
        delay = int(request.args.get("delay", "50"))
    except ValueError:
        return make_response(f"Invalid delay", 400)

    time.sleep(delay / 1000)
    return render_template(f"delay-page.html", delay=delay)


@app.route("/delay/image")
def delayed_image():
    try:
        delay = int(request.args.get("delay", "50"))
    except ValueError:
        return make_response(f"Invalid delay", 400)

    time.sleep(delay / 1000)
    return send_file("static/cats.jpg")


@app.route("/delay/contents")
def delayed_contents():
    try:
        delay = int(request.args.get("delay", "50"))
    except ValueError:
        return make_response(f"Invalid delay", 400)

    try:
        count = int(request.args.get("count", "1"))
    except ValueError:
        return make_response(f"Invalid contents count", 400)

    return render_template(f"delay-contents.html", delay=delay, count=count)
