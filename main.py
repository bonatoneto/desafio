#Importa as bibliotecas
from flask import Flask, render_template, request
import re

app = Flask(__name__)

#Define a rota onde vai iniciar a aplicação
@app.route('/')
def hello():
    return render_template('index.html')

#Define a rota de resultado
@app.route('/resultado', methods= ['POST'])
def resultado():
    #Atribui o nome digitado pelo usuário na variavel "nome"
    nome = request.form.get('nome') or ""
    if nome.isalpha() == False or nome == "":
        #Verifica se o nome contem somente letras
        msgResult = "ERRO, O NOME DEVE CONTER SOMENTE LETRAS!"
        return render_template('result.html', msgResult= msgResult)
    
    sobrenome = request.form.get('sobrenome') or ""
    if sobrenome.isalpha() == False or sobrenome == "":
        #Verifica se o nome contem somente letras
        msgResult = "ERRO, O SOBRENOME DEVE CONTER SOMENTE LETRAS!"
        return render_template('result.html', msgResult= msgResult)
    
    nomeCompleto = nome + sobrenome

    #Atribui o numero digitado pelo usuário na variavel "numero"
    numero = request.form.get('numero', type=int) or 0
    #Atribui o telefone digitado pelo usuário na variavel "telefone"
    telefone = request.form.get('tel') or ""
    #Atribui o e-mail digitado pelo usuário na variavel "email"
    email = request.form.get('email') or ""
    #Verifica se o e-mail informado pelo usuário é um e-mail válido
    def validEmail(email):
        return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))
    if validEmail(email) == False or email == "":
        msgResult = "ERRO, VERIFIQUE SE O E-MAIL DIGITADO É VÁLIDO OU SE O CAMPO FOI PREENCHIDO!"
        return render_template('result.html', msgResult= msgResult)

    #Testa o numero informado pelo usuário
    # a variavel msgResult significa a fica mensagem que vai ser exibida pelo usuário como resposta
    if numero % 3 == 0:
        msgText = "Primeiro nome: "
        msgResult = nome
        return render_template('result.html', msgText=msgText, msgResult=msgResult)
    elif numero % 5 == 0:
        #A variável ddd recebe os 4 primeiros caracteres do telefone para retornar o DDD
        msgText = "Seu DDD: "
        ddd = telefone[0:4]
        msgResult = ddd
        return render_template('result.html', msgText=msgText, msgResult=msgResult)
    elif numero % 7 == 0:
        msgText = "Domínio do seu E-mail: "
        msgResult = email
        return render_template('result.html', msgText=msgText, msgResult=msgResult)
    else:
        #Conta a quantidade de caracteres do nome completo sem espaços e atribui a variavel "numCaracteres"
        numCaracteres =len(nomeCompleto)
        msgResult = numCaracteres
        #Variavel "email2" se refere ao email sem '@'
        email = re.sub("@","", email)
        #Variavel "qntCaracterEmail2" contem a quantidade de caracteres do email sem '@'

        # POR ALGUM MOTIVO NÃO CONSEGUI FAZER TIRAR OS PONTOS DO EMAIL,FUNCIONA PARA O '@' MAS NAO PARA O '.' .... 

        qntCaracterEmail2 = len(email)
        msgResult2 = qntCaracterEmail2
        msgText = "Quantidade de letras do seu nome: "
        msgText2 = "Quantidade de letras do seu email sem '@': "
        return render_template('result.html', msgResult= msgResult, msgResult2= msgResult2, msgText= msgText, msgText2= msgText2)
        
if __name__ == '__main__':
    app.run(debug=True)