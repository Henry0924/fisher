from flask import Flask, make_response

__author__ = "Henry"

app = Flask(__name__)
app.config.from_object("config")


@app.route("/movie/search")
def search():
    pass


# app.add_url_rule("/hello", view_func=hello)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=app.config["DEBUG"])
