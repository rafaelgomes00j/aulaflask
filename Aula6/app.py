from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

@app.route('/')
def paginaInicial():

    userName = 'João'
    #ENVIAR DICIONARIO
    usuario = {
        "nome":"Rafael",
        "idade": 20,
        "email": "9090rafaelgomes@gmail.com",
        "senha": "senha12"
    }
    
    #ENVIANDO BOLEANO 
    logada = True

    #
    return render_template ('index.html' ,userName = userName, use = usuario, logada = logada)

@app.route('/pagina1',methods=['GET', 'POST'])
def pagina1():
    if request.method ==  'GET':
        return render_template('pagina1.html')
    if request.methods == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        area = request.form.get('area')
        # return f'nome: {nome} - idade: {idade} - area: {area}'
            
        return render_template ('usuarios.html', nome = nome, idade = idade, area = area)
        
@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

app.run(debug=True)