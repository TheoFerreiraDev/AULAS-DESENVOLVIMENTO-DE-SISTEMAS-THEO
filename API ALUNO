from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(
    title="API de Cadastro de Alunos",
    description="API para realizar as quatro operações básicas (CRUD) para alunos.",
    version="1.0.0"
)

# Modelo de dados
class Aluno(BaseModel):
    nome: str
    turma: str
    idade: int

# Banco de dados em memória (dicionário)
alunos_db: Dict[int, Aluno] = {
    1: Aluno(nome= "João Guilherme De Souza", turma="1 ano 06", idade="15"),
    2: Aluno(nome= "Julia Marina Carvalho", turma="2 ano 02", idade="16"),
    3: Aluno(nome= "Pedro Luis Oliveira", turma="3 ano 04", idade="18"),
}

@app.get("/")
def read_root():
    """Endpoint raiz da API."""
    return {"message": "Bem-vindo à API de Alunos! Acesse /docs para a documentação interativa."}

# Criar cadastro
@app.post("/alunos/{matricula}")
def criar_aluno(matricula: int, aluno: Aluno):
    if matricula in alunos_db:
        raise HTTPException(status_code=409, detail="Matrícula já cadastrada.")
    
    alunos_db[matricula] = aluno
    return {"message": "Aluno cadastrado com sucesso!", "Matricula": matricula, "aluno": aluno}

# Listar todos
@app.get("/alunos/")
def listar_alunos():
    return list(alunos_db.values())

# Buscar por matrícula
@app.get("/alunos/{matricula}")
def buscar_aluno(matricula: int):
    if matricula not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return alunos_db[matricula]

# Atualizar cadastro
@app.put("/alunos/{matricula}")
def atualizar_aluno(matricula: int, aluno: Aluno):
    if matricula not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    alunos_db[matricula] = aluno.dict()
    return {"mensagem": "Cadastro atualizado com sucesso!", "aluno": aluno}

# Deletar cadastro
@app.delete("/alunos/{matricula}")
def deletar_aluno(matricula: int):
    if matricula not in alunos_db:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    del alunos_db[matricula]
    return {"mensagem": "Aluno deletado com sucesso!"}
