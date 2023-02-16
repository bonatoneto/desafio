from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio')
def hello():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    mensagem = "Esse é o resultado"
    nome = request.form.get('nome')
    sobrenome = request.form.get('sobrenome')
    nomeCompleto = nome + " " + sobrenome
    return render_template('result.html'), nomeCompleto

if __name__ == '__main__':
    app.run(debug=True)