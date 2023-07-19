from flask import Blueprint, make_response, request, render_template, send_file
import time

bp_delay = Blueprint("delay", __name__, url_prefix="/delay")


@bp_delay.route("/page")
def delayed_page():
    try:
        delay = int(request.args.get("delay", "50"))
    except ValueError:
        return make_response(f"Invalid delay", 400)

    time.sleep(delay / 1000)
    return render_template(f"delay-page.html", delay=delay)


@bp_delay.route("/image")
def delayed_image():
    try:
        delay = int(request.args.get("delay", "50"))
    except ValueError:
        return make_response(f"Invalid delay", 400)

    time.sleep(delay / 1000)
    return send_file("static/cats.jpg")


@bp_delay.route("/contents")
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
