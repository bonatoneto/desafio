from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    mensagem = "esse é o resultado"
    return mensagem

if __name__ == "__main__":
    app.run(debug=True)