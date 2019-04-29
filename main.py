from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def portfolio():
    return render_template("portfolio.html")


@app.route("/Google")
def Google():
    return render_template("Google.html")


@app.route("/Fakebook")
def Fakebook():
    return render_template("Fakebook.html")


@app.route("/Kirpykla")
def Kirpykla():
    return render_template("Kirpykla.html")

if __name__ == '__main__':
    app.run()
