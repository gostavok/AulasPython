from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar_pessoas")
def listar_pessoas():
    return render_template("listar_pessoas.html")    

@app.route("/inserir_pessoa")
def inserir_pessoas():
    return render_template("form_inserir_pessoa.html")  

@app.route("/alterar_pessoas")
def alterar_pessoas():
    return render_template("form_alterar_pessoa.html")  

@app.route("/exibir_mensagem")
def exibir_mensagem():
    return render_template("exibir_mensagem.html")  
    
app.run()