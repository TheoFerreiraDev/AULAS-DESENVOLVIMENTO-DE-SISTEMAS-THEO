import uuid
from typing import List, Dict, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


class TarefaBase(BaseModel):
    """Modelo base para dados de entrada (Criação e Atualização)"""
    titulo: str = Field(..., min_length=3, description="Título curto e obrigatório da tarefa.")
    descricao: Optional[str] = Field(None, description="Detalhamento opcional da tarefa.")

class TarefaCreate(TarefaBase):
    """Modelo de dados esperado ao criar uma nova tarefa."""
    pass

class TarefaUpdate(TarefaBase):
    """Modelo de dados esperado ao atualizar uma tarefa existente."""
    concluida: bool = Field(False, description="Status de conclusão da tarefa.")

class Tarefa(TarefaUpdate):
    """Modelo de dados completo da Tarefa (usado na resposta da API)"""
    id: str = Field(..., description="Identificador único gerado automaticamente.")


#Dicionario em Memoria 
db_tarefas: Dict[str, dict] = {}


app = FastAPI(
    title="Trabalho final de Desenvolvimento de Sistema // Théo Ferreira - Lianara Vitória  e Matheus Gorges Machado",
    description="API RESTful para gerenciar tarefas em memória com FastAPI."
)


def _get_tarefa_dict(tarefa_id: str) -> Optional[dict]:
    return db_tarefas.get(tarefa_id)

def _generate_id() -> str:
    return str(uuid.uuid4())





@app.post(
    "/tarefas",
    response_model=Tarefa,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova tarefa"
)
async def criar_tarefa(tarefa_data: TarefaCreate):
    
    novo_id = _generate_id()
    
    nova_tarefa = Tarefa(
        id=novo_id,
        titulo=tarefa_data.titulo,
        descricao=tarefa_data.descricao,
        concluida=False 
    )
    
    db_tarefas[novo_id] = nova_tarefa.model_dump() 
    return nova_tarefa

@app.get(
    "/tarefas",
    response_model=List[Tarefa],
    summary="Lista todas as tarefas"
)
async def listar_tarefas():
    return list(db_tarefas.values())

@app.get(
    "/tarefas/{tarefa_id}",
    response_model=Tarefa,
    summary="Obtém uma tarefa específica por ID"
)
async def obter_tarefa(tarefa_id: str):
    """Retorna a tarefa correspondente ao ID fornecido."""
    
    tarefa = _get_tarefa_dict(tarefa_id)
    
    if not tarefa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID '{tarefa_id}' não encontrada."
        )
    
    return tarefa

@app.put(
    "/tarefas/{tarefa_id}",
    response_model=Tarefa,
    summary="Atualiza uma tarefa existente"
)
async def atualizar_tarefa(tarefa_id: str, tarefa_data: TarefaUpdate):
    
    tarefa_existente = _get_tarefa_dict(tarefa_id)
    
    if not tarefa_existente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID '{tarefa_id}' não encontrada."
        )
    
    if not tarefa_data.titulo or len(tarefa_data.titulo) < 3:
         pass
    
    tarefa_existente.update(tarefa_data.model_dump())
    
    tarefa_existente['id'] = tarefa_id 
    
    db_tarefas[tarefa_id] = tarefa_existente
    
    return tarefa_existente

@app.delete(
    "/tarefas/{tarefa_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Deleta uma tarefa"
)
async def deletar_tarefa(tarefa_id: str):
    """Remove uma tarefa pelo ID."""
    
    if tarefa_id not in db_tarefas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID '{tarefa_id}' não encontrada."
        )
    
    del db_tarefas[tarefa_id]
    
    return None
