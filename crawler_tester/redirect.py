from flask import Blueprint, abort, make_response, request, render_template

from crawler_tester.http_codes import CODES_REDIRECT


bp_redirect = Blueprint("redirect", __name__, url_prefix="/redirect")


def redirect_http(status_code=""):
    try:
        http_code = int(status_code)
        if http_code not in CODES_REDIRECT:
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


@bp_redirect.route("/<type_>")
def redirect(type_=None):
    if type_[:5] == "http-":
        return redirect_http(status_code=type_[5:])

    if type_[:3] == "js-":
        return redirect_js(page_name=type_[3:])

    else:
        abort(404)
