from flask import Blueprint, make_response

from crawler_tester.http_codes import CODES_REDIRECT


bp_redirect_chain = Blueprint("redirect_chain", __name__, url_prefix="/redirect-chain")


@bp_redirect_chain.route("/<int:counter>")
def redirect(counter=1):

    if counter > 1:
        resp = make_response("ok", 302)
        resp.headers["Location"] = f"/redirect-chain/{counter - 1}"
        return resp

    elif counter == 1:
        resp = make_response("ok", 302)
        resp.headers["Location"] = "/landing"
        return resp
    
    else:
        return "ok"
