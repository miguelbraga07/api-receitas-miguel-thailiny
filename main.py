from http import HTTPStatus
from fastapi import FastAPI, HTTPException 
from schema import CreateReceita, Receita, Usuario, BaseUsuario, UsuarioPublic

app = FastAPI()

usuarios: list[Usuario] = []
receitas: list[Receita] = []

receitas: list[Receita] = []

@app.get("/receitas", response_model=list[Receita], status_code=HTTPStatus.OK)
def get_todas_receitas():
    return receitas

@app.get("/")
def hello():
    return{"title":"Livro de Receitas"}


@app.get("/receitas/{nome_receita}",  response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_nome (nome_receita: str):
   for receita in receitas:
        if receita.nome == nome_receita:
            return receita
   raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")
    
@app.post("/receitas", response_model=Receita, status_code=HTTPStatus.CREATED)
def criar_receita(receita: CreateReceita):

    if len(receitas) == 0:
        novo_id = 1
    else:
        novo_id = receitas[-1].id + 1

    nova_receita = Receita(
        id=novo_id,
        nome=receita.nome,
        ingredientes=receita.ingredientes,
        modo_de_preparo=receita.modo_de_preparo
    )

    receitas.append(nova_receita)

    return nova_receita

@app.get("/receitas/id/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def get_receita_por_id(id:int):
    for receita in receitas:
        if receita.id == id:
            return receita
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")
    
@app.put("/receitas/{id}", response_model=Receita, status_code=HTTPStatus.OK)
def update_receita(id: int, dados: CreateReceita):
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
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Receita não encontrada")
    

@app.delete("/receitas/{id}",  response_model=Receita, status_code=HTTPStatus.OK)
def deletar_receita(id: int):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_deletada = receitas.pop(i)
    return receita_deletada
    
@app.get("/usuarios", status_code=HTTPStatus.OK, response_model=list[UsuarioPublic])
def get_todos_usuarios():
    return usuarios

@app.get("/usuarios/{nome_usuario}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_nome(nome_usuario: str):
    for usuario in usuarios:
        if usuario.nome == nome_usuario:
            return usuario
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuario não encontrada")

@app.get("/usuarios/id/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_id(id: int):
  for usuario in usuarios:
        if usuario.id == id:
            return usuario
  raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuario não encontrada")

@app.post("/usuarios",status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_usuario(dados: BaseUsuario):

    if len(usuarios) == 0:
        novo_id = 1
    else:
        novo_id = usuarios[-1].id + 1

    novo_usuario = Usuario(
        id=novo_id,
        nome_usuario=dados.nome_usuario,
        senha=dados.senha,
        email=dados.email
    )

    usuarios.append(novo_usuario)

@app.put("usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def update_usuario(id: int, dados: BaseUsuario):
     for i in range(len(usuarios)):
        if usuarios[i].id == id:
            usuario_atualizado = Usuario(
                id=id,
                usuario=dados.usuario_atualizado,
                senha=dados.senha_atualizada,
                email=dados.email_atualizado,
            )
            usuarios[i] = (usuario_atualizado)
            return usuario_atualizado
     raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuario não encontrada")

@app.delete("/usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def delete_usuario(id: int) :
   for i in range(len(usuarios)):
        if usuarios[i].id == id:
            usuarios_deletada = usuarios.pop(i)
   return usuarios_deletada