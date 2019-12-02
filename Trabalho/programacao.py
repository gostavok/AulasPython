import os
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict


arq = 'many−to−many−com−lista.db'
db = SqliteDatabase (arq)

class BaseModel(Model):
    class Meta:
        database = db


class Fornecedor(BaseModel):
    codigo = IntegerField()
    nome = CharField()
    cnpj = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()
    

class Cor(BaseModel):
    codigo = IntegerField()
    nome = CharField()
    preco = CharField()
    validade = CharField()
    fornecedor = ForeignKeyField(Fornecedor)

class Material(BaseModel):
    codigo = IntegerField()
    nome = CharField()
    preco = CharField()
    validade = CharField()
    fornecedor = ForeignKeyField(Fornecedor)

class Estampa(BaseModel):
    codigo = IntegerField()
    nome = CharField()
    preco = CharField()
    validade = CharField()
    fornecedor = ForeignKeyField(Fornecedor)

class Orcamento(BaseModel):
    codigoOrcamento = IntegerField()
    cor = ForeignKeyField(Cor)
    estampa = ForeignKeyField(Estampa)
    material = ForeignKeyField(Material)
    quantidade = IntegerField()
    valorBase = IntegerField()
    valorOrcamento = DoubleField()

class Produto(BaseModel):
    codigo = IntegerField()
    descricaoProduto = CharField()
    cor = ForeignKeyField(Cor)
    estampa = ForeignKeyField(Estampa)
    material = ForeignKeyField(Material)
    valorProduto = DoubleField()

class Cliente(BaseModel):
    codigo = IntegerField()
    nome = CharField()
    cpf = CharField()
    telefone = CharField()
    email = CharField()

class Pedido(BaseModel):
    codigoPedido = IntegerField()
    cliente = ForeignKeyField(Cliente)
    produto = ForeignKeyField(Produto)

class MoldesPreFeitos(BaseModel):
    codigoMolde = IntegerField()
    nomeMolde = CharField()
    cor = ForeignKeyField(Cor)
    estampa = ForeignKeyField(Estampa)
    material = ForeignKeyField(Material)
    valorModel = DoubleField()

class Financeiro(BaseModel):
    codigoRegistro = IntegerField()
    dataVenda = CharField()
    produtoVendido = ForeignKeyField(Produto)


if __name__ == '__main__':

    db.connect()
    db.create_tables([Fornecedor, Cor, Material, Estampa, Orcamento, Produto, Cliente, Pedido, MoldesPreFeitos, Financeiro])


    fornecedor1 = Fornecedor.create( codigo = 1, nome = 'Joao LTDA', cnpj = '28382372', endereco = 'Rua dos Palmares', telefone = '4345676', email = 'JoaoLTDA@gmail.com' )
    cor1 = Cor.create(codigo = 1, nome = 'Amarelo', preco = '23.99', validade = '180 dias', fornecedor = fornecedor1)
    material1 = Material.create(codigo = 1, nome = 'Algodão', preco = '9.99', validade = '3 anos', fornecedor = fornecedor1)
    estampa1 = Estampa.create(codigo = 1, nome='Bolinhas Azuis', preco= '14.98', validade = '1 ano', fornecedor = fornecedor1)
    orcamento1 = Orcamento.create( codigoOrcamento = 1, cor = cor1, material = material1, estampa= estampa1, quantidade = 2, valorBase = 20, valorOrcamento = 54.00)
    produto1 = Produto.create(codigo = 1, descricaoProduto = 'Camisa Polo GG', cor = cor1, estampa= estampa1, material = material1, valorProduto = 37.00)
    cliente1 = Cliente.create(codigo = 1, nome = 'Hylson', cpf='23334564744', telefone= '234526578', email= 'Hylson@gmail.com')
    pedido = Pedido.create(codigoPedido = 1, cliente = cliente1, produto = produto1)
    moldes1 = MoldesPreFeitos.create(codigoMolde = 1, nomeMolde = 'Camisa Polo', cor = cor1, estampa = estampa1, material = material1, valorModel = 15.00)
    financeiro1 = Financeiro.create(codigoRegistro = 1, dataVenda = '23/11/19', produtoVendido = produto1)

    teste = Cor.select()


    ajuda = map(model_to_dict, teste)

    print(ajuda)