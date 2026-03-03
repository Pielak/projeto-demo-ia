from fastapi import FastAPI, HTTPException
from app.models import Cliente
from app import database

app = FastAPI(title="API de Clientes", version="1.0")

@app.get("/clientes")
def listar():
    return database.get_all()

@app.get("/clientes/{id}")
def buscar(id: int):
    cliente = database.get_by_id(id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente

@app.post("/clientes", status_code=201)
def criar(cliente: Cliente):
    return database.create(cliente)

@app.put("/clientes/{id}")
def atualizar(id: int, cliente: Cliente):
    resultado = database.update(id, cliente)
    if not resultado:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return resultado

@app.delete("/clientes/{id}", status_code=204)
def deletar(id: int):
    if not database.delete(id):
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
# teste salvar artefatos
# teste reprovacao pipeline
import os
password = "admin123"  # senha hardcoded
token = "ghp_xxxxxxxxxxx"  # token exposto
def funcao_sem_tratamento_erro():
    x = 1/0
