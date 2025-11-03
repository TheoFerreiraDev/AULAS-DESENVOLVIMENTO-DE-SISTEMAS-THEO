iimport pytest
from fastapi.testclient import TestClient
from main import app, db_tarefas # Importa a app e o DB em memória

client = TestClient(app)

@pytest.fixture(autouse=True)
def clean_db():
    """Limpa o dicionário em memória antes de cada teste."""
    db_tarefas.clear()
    yield # Executa o teste


def test_criar_tarefa_sucesso():
    """Testa a criação bem-sucedida de uma tarefa (Com título e descrição)."""
    response = client.post(
        "/tarefas",
        json={"titulo": "Fazer compras", "descricao": "Comprar pão e leite"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "Fazer compras"
    assert data["descricao"] == "Comprar pão e leite"
    assert data["concluida"] is False
    assert "id" in data
    assert data["id"] in db_tarefas

def test_criar_tarefa_titulo_minimo():
    """Testa a criação bem-sucedida de uma tarefa com o mínimo de caracteres no título."""
    response = client.post(
        "/tarefas",
        json={"titulo": "ABC"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["titulo"] == "ABC"
    assert data.get("descricao") is None
    assert data["concluida"] is False

def test_criar_tarefa_falha_sem_titulo():
    """Testa a falha na criação por falta do campo 'titulo' (Deve retornar 422)."""
    response = client.post(
        "/tarefas",
        json={"descricao": "Detalhe da tarefa sem título"}
    )
    assert response.status_code == 422
    assert "field required" in response.json()["detail"][0]["msg"]

def test_criar_tarefa_falha_titulo_curto():
    """Testa a falha na criação se o 'titulo' tiver menos de 3 caracteres (Deve retornar 422)."""
    response = client.post(
        "/tarefas",
        json={"titulo": "AB"}
    )
    assert response.status_code == 422
    assert "ensure this value has at least 3 characters" in response.json()["detail"][0]["msg"]


def test_listar_tarefas_vazia():
    """Testa a listagem quando não há nenhuma tarefa (deve retornar uma lista vazia)."""
    response = client.get("/tarefas")
    assert response.status_code == 200
    assert response.json() == []

def test_listar_tarefas_existentes():
    """Testa a listagem quando existem uma ou mais tarefas."""
    tarefa1 = {"id": "1", "titulo": "Tarefa Um", "descricao": None, "concluida": False}
    tarefa2 = {"id": "2", "titulo": "Tarefa Dois", "descricao": "Detalhe", "concluida": True}
    db_tarefas["1"] = tarefa1
    db_tarefas["2"] = tarefa2
    
    response = client.get("/tarefas")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert any(t["id"] == "1" for t in data)
    assert any(t["id"] == "2" for t in data)
    

def test_buscar_tarefa_por_id_valido():
    """Testa a busca por um ID válido e existente."""
    tarefa = {"id": "abc-123", "titulo": "Tarefa Teste", "descricao": None, "concluida": False}
    db_tarefas["abc-123"] = tarefa
    
    response = client.get("/tarefas/abc-123")
    assert response.status_code == 200
    assert response.json()["id"] == "abc-123"
    assert response.json()["titulo"] == "Tarefa Teste"

def test_buscar_tarefa_por_id_nao_existente():
    """Testa a busca por um ID que não existe (deve retornar 404)."""
    response = client.get("/tarefas/non-existent-id")
    assert response.status_code == 404
    assert "não encontrada" in response.json()["detail"]
    

def test_atualizar_tarefa_sucesso():
    """Testa a atualização bem-sucedida de uma tarefa."""
    tarefa_original = {"id": "upd-1", "titulo": "Antigo Título", "descricao": "Antiga Descrição", "concluida": False}
    db_tarefas["upd-1"] = tarefa_original
    
    novos_dados = {
        "titulo": "Novo Título Atualizado", 
        "descricao": "Nova Descrição Detalhada", 
        "concluida": True
    }
    
    response = client.put("/tarefas/upd-1", json=novos_dados)
    assert response.status_code == 200
    data = response.json()
    
    assert data["titulo"] == "Novo Título Atualizado"
    assert data["descricao"] == "Nova Descrição Detalhada"
    assert data["concluida"] is True
    
    tarefa_atualizada_db = db_tarefas["upd-1"]
    assert tarefa_atualizada_db["titulo"] == "Novo Título Atualizado"
    assert tarefa_atualizada_db["concluida"] is True

def test_atualizar_tarefa_id_nao_existente():
    """Testa a tentativa de atualizar uma tarefa com um ID inexistente (deve retornar 404)."""
    novos_dados = {"titulo": "Título", "descricao": "Descrição", "concluida": True}
    response = client.put("/tarefas/non-existent-id-put", json=novos_dados)
    assert response.status_code == 404
    assert "não encontrada" in response.json()["detail"]

def test_atualizar_tarefa_falha_titulo_invalido():
    """Testa a falha na atualização com um título inválido (curto) (Deve retornar 422)."""
    
    tarefa_original = {"id": "upd-2", "titulo": "Original", "descricao": None, "concluida": False}
    db_tarefas["upd-2"] = tarefa_original
    
    
    dados_invalidos = {"titulo": "A", "descricao": "Nova", "concluida": False}
    
    response = client.put("/tarefas/upd-2", json=dados_invalidos)
    assert response.status_code == 422
    assert "ensure this value has at least 3 characters" in response.json()["detail"][0]["msg"]
    
    assert db_tarefas["upd-2"]["titulo"] == "Original"


def test_deletar_tarefa_sucesso_e_verificacao():
    """Testa a deleção bem-sucedida e verifica se a tarefa sumiu."""
    tarefa_id_to_delete = "del-1"
    db_tarefas[tarefa_id_to_delete] = {"id": tarefa_id_to_delete, "titulo": "Para Deletar", "descricao": None, "concluida": False}
    
    response_delete = client.delete(f"/tarefas/{tarefa_id_to_delete}")
    assert response_delete.status_code == 204
    assert response_delete.content == b"" 
    
    response_get = client.get(f"/tarefas/{tarefa_id_to_delete}")
    assert response_get.status_code == 404
    assert tarefa_id_to_delete not in db_tarefas

def test_deletar_tarefa_id_nao_existente():
    """Testa a tentativa de deletar uma tarefa com ID inexistente (deve retornar 404)."""
    response = client.delete("/tarefas/non-existent-id-delete")
    assert response.status_code == 404
    assert "não encontrada" in response.json()["detail"]
