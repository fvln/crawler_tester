from flask import Blueprint, make_response

from crawler_tester.http_codes import CODES_REDIRECT

bp_status = Blueprint("status", __name__, url_prefix="/status")


@bp_status.route("/<status_code>")
def status(status_code=""):
    try:
        http_code = int(status_code)
        if http_code not in CODES_REDIRECT:
            raise ValueError("reponse code should be in range [300,308]")
    except Exception as e:
        return make_response(f"Invalid HTTP status response: {e}", 404)

    return make_response(f"Status code {http_code}", http_code)
