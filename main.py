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

@app.get ("/receitas/{receita}")
def get_receita(nome: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
        
        return {"receita não encontrada"}
    


@app.get("/receitas/{nome_receita}")
def get_receita_por_nome (nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
            return receita
        
    return {"receita não encontrada"}

@app.post("/receitas")
def create.receitas(dados:Receitas):
   nova-receita = dados

   receitas.append(nova_receita)
   return nova_receita