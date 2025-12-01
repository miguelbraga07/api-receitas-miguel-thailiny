from http import HTTPStatus
from fastapi import FastAPI, HTTPException, Depends
from schema import CreateReceita, Receita, Usuario, BaseUsuario, UsuarioPublic
from models import User
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import get_session
from sqlalchemy.exc import IntegrityError
app = FastAPI()


receitas: list[Receita] = []
app = FastAPI(tittle='API de receita')

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
def get_todos_usuarios(
       skip: int=0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
        
    return users

@app.get("/usuarios/{nome_usuario}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_nome(nome_usuario: str, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where((User.nome_usuario == nome_usuario))
    )
    if db_user:
        return db_user
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuario não encontrado")

@app.get("/usuarios/id/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def get_usuario_por_id(id: int, session: Session = Depends(get_session)):
     db_user = session.scalar(
         select(User).where((User.id == id))
     )
     if db_user:
         return db_user
 
     raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuario não encontrado")

@app.post("/usuarios",status_code=HTTPStatus.CREATED, response_model=UsuarioPublic)
def create_usuario(dados: BaseUsuario, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select (User).where(
         (User.nome_usuario == dados.nome_usuario) | (User.email == dados. email)
        )
    )

    if db_user:
        if db_user.nome_usuario == dados.nome_usuario:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='Nome de usuário já existe',
            )
        elif db_user.email == dados.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail= 'Esse email já existe',
            )
    db_user= User(
        nome_usuario=dados.nome_usuario, senha=dados.senha, email=dados.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


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

    return novo_usuario

@app.put("usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def update_usuario(id: int, dados: BaseUsuario, session: Session = Depends(get_session)):
    
    db_user = session.scalar(select(User).where(User.id == id))
    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuario nao encontrado'
        )
    
    try:
        db_user.nome_usuario = dados.nome_usuario
        db_user.senha = dados.senha
        db_user.email = dados.email
        session.commit()
        session.refresh(db_user)

        return db_user
    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Nome de usuario ou email ja existe'
        )
@app.delete("/usuarios/{id}", response_model=UsuarioPublic, status_code=HTTPStatus.OK)
def delete_usuario(id: int, session: Session = Depends(get_session)) :
   db_user = session.scalar(select(User).where(User.id == id))

   if not db_user:
       raise HTTPException(
           status_code=HTTPStatus.NOT_FOUND, detail='Usuario nao encontrado'
       )
   
   session.delete(db_user)
   session.commit()
   return db_user