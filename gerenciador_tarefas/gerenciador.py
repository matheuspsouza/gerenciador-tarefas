from fastapi import FastAPI

app=FastAPI()

TAREFAS=[{"id":1,"titulo":"titulo 1", "descricao":"descricao 1","estado":"finalizado"}]

@app.get("/tarefas")
def listar():
    return TAREFAS