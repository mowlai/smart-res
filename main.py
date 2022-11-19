from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """Route and function for landing page"""
    return render_template("index.html")




if __name__ == '__main__':
    app.run(debug=True)