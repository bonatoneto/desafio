from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/resultado')
def resultado():
    return "resultado"

if __name__ == "__main__":
    app.run(debug=True)