"""
@author: matheus cardoso
 
Copyright (C) 2014 MVM Tecnologia
"""

from google.appengine.ext import db
class Participante(db.Model):
    
    nome = db.StringProperty()
    dataNascimento = db.StringProperty()
    sexo = db.StringProperty()
    identidade = db.StringProperty()
    
    logradouro = db.StringProperty()
    complemento = db.StringProperty()
    cidade = db.StringProperty()
    uf = db.StringProperty()
    bairro = db.StringProperty()
    
    telCelular1 = db.StringProperty()
    telCelular2 = db.StringProperty()
    telResidencial = db.StringProperty()
    email = db.StringProperty()
    
    alergias = db.StringProperty()
    medicamentos = db.StringProperty()
    
    nomeContato = db.StringProperty()
    telCelular1Contato = db.StringProperty()
    telCelular2Contato = db.StringProperty()
    telResidencialContato = db.StringProperty()
    telComercialContato = db.StringProperty()
    ficouSabendo = db.StringListProperty()
    
    pagouInscricao = db.StringProperty()
    
    dataInscricao = db.DateTimeProperty(auto_now=True, auto_now_add=True)