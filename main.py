from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel
from typing import List

class Receita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas: List[Receita] = []

@app.get("/receitas")
def get_todas_receitas():
    return receitas

@app.get("/")
def hello():
    return{"title":"Livro de Receitas"}


@app.get("/receitas/{nome_receita}")
def get_receita_por_nome (nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
        
    return {"receita não encontrada"}

@app.post("/receitas")
def create_receitas(dados:Receita):
   nova_receita = dados

   receitas.append(nova_receita)
   return nova_receita
   
   
class CreateReceita(BaseModel):
       nome: str
       indredientes: List[str]
       modo_de_preparo: str

class Receitas(BaseModel):
    id: int
    nome: str
    indredientes: List[str]
    modo_de_preparo: str

#nossa logica

nova_receita = Receita(id= '''Nova ID''', nome='''nome que o usuario forneceu''')

receitas = [
    {"id": 1, "nome":"pudim"}
]

@app.get("/receitas/id/{id}")
def get_receita_por_id():
    for receita in receitas:
        if receita["id"] == id:
            return receita
        return{"mensagem": "Receita não encontrada"}
    