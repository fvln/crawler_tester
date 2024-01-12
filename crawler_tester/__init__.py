from flask import Flask


def create_app():
    app = Flask(__name__)

    from crawler_tester.status import bp_status
    from crawler_tester.redirect import bp_redirect
    from crawler_tester.redirect_chain import bp_redirect_chain
    from crawler_tester.delay import bp_delay

    app.register_blueprint(bp_status)
    app.register_blueprint(bp_redirect)
    app.register_blueprint(bp_redirect_chain)
    app.register_blueprint(bp_delay)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/landing")
    def landing():
        return "Redirect successful"

    return app
