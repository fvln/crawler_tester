from flask import Blueprint, make_response

bp_status = Blueprint("status", __name__, url_prefix="/status")


@bp_status.route("/<status_code>")
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
