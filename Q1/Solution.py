from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


class ACM_Debugging_Competition { #added a curly brace
    @app.route("/bye")
    def index():
        return "hi"

    @app.route("/hi")
    def bye():
        return "bye"

}
if __name__ == "__main__":
    app.run(debug=False)
