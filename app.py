from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")


@app.route("/obrigado")
def obrigado():
    return render_template("obrigado.html")


if __name__ == "__main__":
    app.run(debug=True)
