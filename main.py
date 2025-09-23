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
    
@app.put("/receitas/{id}")
def update_receita(id: int,dados: CreateReceita):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo,
            )
            receitas[i] = (receita_atualizada)
            return receita_atualizada
        return {"mensagem:": "receita nao encontrada"}
    
    receita = ["brownie", "arroz", "vitamina de morango", "bolo de cenoura", "pudim", "brigadeiro"]

    def editar_nome(nome_atual, nome_alterado):
        if nome_alterado in receitas:
            return {"já existe"}
        for i in range (len(receitas)):
            if receitas[i] == nome_atual:
                receitas[i] == nome_alterado
            return {"nome modificado"}
        return {"receita não encontrada"}
    def editar_receita(nome, ingredientes, modo_de_preparo):
        if nome == "" or ingredientes == "" or modo_de_preparo == "":
          return{"campos vazios nao sao salvos"}
        return {"receita foi editada"}
    
@app.delete("/receitas/{id}")
def deletar_receita(id: int):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_removida = receitas.pop(i)
            return {
                "mensagem": f"Receita '{receita_removida.nome}' foi excluída com sucesso.",
                "receita_excluida": receita_removida
            }
            
            raise HTTPException(status_code=404, detail="Receita não encontrada.")
