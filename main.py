from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel
from typing import List

class Receita(BaseModel):
    nome: str
    ingredientes: List[str]
    modo_de_preparo: str

receitas: List[Receita] = [
  Receita(
        nome="Brownie",
        ingredientes=[
            "1 xícara de manteiga derretida",
            "2 xícaras de açúcar",
            "1 xícara de chocolate em pó",
            "1 colher de chá de essência de baunilha",
            "4 ovos",
            "1 xícara de farinha de trigo"
        ],
        modo_de_preparo=(
            "Misture a manteiga, o açúcar e o chocolate em pó. "
            "Adicione a baunilha e os ovos, um a um. "
            "Incorpore a farinha e misture bem. "
            "Despeje em uma forma untada e asse em forno pré-aquecido a 180°C por 30 minutos."
        )
    ),
    Receita(
        nome="Macarrão à Bolonhesa",
        ingredientes=[
            "500g de macarrão",
            "2 colheres de sopa de óleo",
            "1 cebola picada",
            "2 dentes de alho picados",
            "500g de carne moída",
            "2 xícaras de molho de tomate",
            "Sal e pimenta a gosto"
        ],
        modo_de_preparo=(
            "Cozinhe o macarrão até ficar al dente. "
            "Em outra panela, refogue a cebola e o alho no óleo. "
            "Adicione a carne moída e cozinhe até dourar. "
            "Coloque o molho de tomate, tempere e deixe ferver por 10 minutos. "
            "Misture com o macarrão e sirva quente."
        )
    ),
    Receita(
        nome="Omelete Simples",
        ingredientes=[
            "2 ovos",
            "Sal a gosto",
            "Pimenta-do-reino a gosto",
            "1 colher de sopa de óleo",
            "Queijo (opcional)",
            "Presunto (opcional)"
        ],
        modo_de_preparo=(
            "Bata os ovos com sal e pimenta. "
            "Aqueça o óleo em uma frigideira, despeje os ovos batidos e cozinhe em fogo baixo. "
            "Adicione queijo e presunto, se desejar. "
            "Dobre a omelete ao meio e sirva."
        )
    ),
    Receita(
        nome="Arroz de Couve-Flor",
        ingredientes=[
            "1 cabeça de couve-flor",
            "1 colher de sopa de azeite",
            "1 dente de alho picado",
            "Sal a gosto"
        ],
        modo_de_preparo=(
            "Rale a couve-flor até ficar com textura parecida com arroz. "
            "Aqueça o azeite e refogue o alho. "
            "Adicione a couve-flor, tempere com sal e refogue por 5 a 7 minutos. "
            "Sirva como substituto do arroz tradicional."
        )
    ),
    Receita(
        nome="Vitamina de Banana",
        ingredientes=[
            "2 bananas maduras",
            "2 xícaras de leite",
            "1 colher de sopa de aveia",
            "1 colher de mel (opcional)"
        ],
        modo_de_preparo=(
            "Coloque todos os ingredientes no liquidificador e bata até ficar homogêneo. "
            "Sirva gelado."
        )
    ),
    Receita(
        nome="Tapioca com Queijo",
        ingredientes=[
            "3 colheres de sopa de goma de tapioca hidratada",
            "1 fatia de queijo coalho ou mussarela",
            "Sal a gosto"
        ],
        modo_de_preparo=(
            "Aqueça uma frigideira antiaderente. "
            "Espalhe a goma de tapioca até cobrir o fundo da frigideira. "
            "Deixe firmar, vire, coloque o queijo e dobre ao meio. "
            "Cozinhe até o queijo derreter e sirva."
        )
    )
]

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
