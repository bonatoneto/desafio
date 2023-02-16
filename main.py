from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio')
def hello():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    mensagem = "Esse é o resultado"
    nome = request.form.get('nome')
    numero = request.form.get('numero', type=int) or 0
    telefone = request.form.get('tel', type=int)
    email = request.form.get('email')
    if numero % 3 == 0:
        return render_template('result.html', nome=nome)
    elif numero % 5 ==0:
        return render_template('result.html', telefone=telefone)
    elif numero % 7 ==0:
        return render_template('result.html', email=email)
    else:
        return render_template('result.html', mensagem= mensagem)

if __name__ == '__main__':
    app.run(debug=True)