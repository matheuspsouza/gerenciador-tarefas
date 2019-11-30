from  starlette.testclient import TestClient
from gerenciador_tarefas.gerenciador import app,TAREFAS

def test_quando_listar_tarefas_deve_retornar_codifog_200 ():
    cliente=TestClient(app)
    resposta= cliente.get("/tarefas")
    assert resposta.status_code==200

def test_quando_listar_tarefas_o_retorno_da_mensagem_deve_ser_json():
    cliente=TestClient(app)
    respost=cliente.get("/tarefas")
    assert respost.headers["Content-type"]=="application/json"

def test_quando_listar_tarefas_o_retorno_deve_conter_uma_lista():
    cliente=TestClient(app)
    resposta=cliente.get("/tarefas")
    assert isinstance(resposta.json(), list)

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_id():
    TAREFAS.append({"id":1})
    cliente=TestClient(app)
    resposta=cliente.get("/tarefas")
    assert "id" in resposta.json().pop() #pop() retira o primeiro elemento da lista
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_titulo():
    TAREFAS.append({"titulo":"titulo de um deles"})
    cliente=TestClient(app)
    resposta=cliente.get("/tarefas")
    assert "titulo" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_desecricao():
    TAREFAS.append({"descricao":"descricao"})
    cliente=TestClient(app)
    resposta=cliente.get("/tarefas")
    assert "descricao" in resposta.json().pop()
    TAREFAS.clear()

def test_quando_listar_tarefas_a_tarefa_retornada_deve_possuir_estado():
    TAREFAS.append({"estado":"finalizado"})
    cliente=TestClient(app)
    resposta=cliente.get("/tarefas")
    assert "estado" in resposta.json().pop()
    TAREFAS.clear()