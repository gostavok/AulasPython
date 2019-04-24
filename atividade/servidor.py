from flask import Flask, render_template, request, redirect , url_for

app=Flask(__name__)

class Pessoa:
    def __init__(self,nome,endereco,telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone



lista_de_pessoas=[]


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html", geral = lista_de_pessoas)    

@app.route("/inserir_pessoa")
def inserir_pessoas():
    return render_template("form_inserir_pessoa.html")  

@app.route("/form_alterar_pessoa")
def for_alterar_pessoa():
    procurado = request.args.get("nome")
    for pe in lista_de_pessoas:
        if pe.nome == procurado:
            return render_template("form_alterar_pessoa.html", informacoes = pe)
    return "Não achei: " + procurado + " :("

@app.route("/alterar_pessoa")
def alterar_pessoa():
    procurado = request.args.get("nome_original")
    nome = request.args.get("nome")
    fenix = Pessoa (nome, "rua", "999")
    for i in range(len(lista_de_pessoas)):
        if lista_de_pessoas[i].nome == procurado:
            lista_de_pessoas[i] = fenix
            return redirect (url_for("listar_pessoas"))
    return "Não achei: " + procurado + " :("

@app.route("/cadastrar_pessoa")
def add():
    endereco = request.args.get("endereco")
    nome = request.args.get("nome")
    lista = ([Pessoa(nome,endereco,"23454")])
    lista_de_pessoas.append(Pessoa(nome,endereco,"23454"))
    #return render_template ("listar_pessoas.html", teste = lista, geral = lista_de_pessoas)
    return redirect ( url_for ("listar_pessoas"))
    
@app.route("/excluir_pessoa")
def excluir_pessoa():
    achou = None
    nome = request.args.get("nome")
    for p in lista_de_pessoas:
        if p.nome == nome:
            achou = p 
            break
    if achou != None:
        lista_de_pessoas.remove(achou) 
    return render_template("exibir_mensagem.html")


@app.route("/form_login")
def form_login():
    return render_template("form_login.html")  

app.run( debug = True)