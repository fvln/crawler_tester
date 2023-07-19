from flask import Blueprint, make_response, request, render_template, send_file
import time

bp_delay = Blueprint("delay", __name__, url_prefix="/delay")


@bp_delay.before_request
def check_params():
    def valid_param(name="", low=0, high=100):
        try:
            p = int(request.args.get(name, low))
            if (p < low) or (p >= high):
                raise ValueError()
            return True
        except ValueError:
            return False

    if not valid_param("delay", high=5000):
        return make_response("Invalid delay", 400)
    if not valid_param("count"):
        return make_response("Invalid contents count", 400)


@bp_delay.route("/page")
def delayed_page():
    delay = int(request.args.get("delay", "50"))

    time.sleep(delay / 1000)
    return render_template(f"delay-page.html", delay=delay)


@bp_delay.route("/image")
def delayed_image():
    delay = int(request.args.get("delay", "50"))

    time.sleep(delay / 1000)
    return send_file("static/cats.jpg")


@bp_delay.route("/contents")
def delayed_contents():
    delay = int(request.args.get("delay", "50"))
    count = int(request.args.get("count", "1"))

    return render_template(f"delay-contents.html", delay=delay, count=count)
