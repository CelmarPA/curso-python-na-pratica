from fastapi import FastAPI


# API Server Delivery
api = FastAPI(title="API Server Delivery")


# uvicorn app.main:api iniciar servidor da aplicação
# Decorator: maneira de adicionar informações e comportamentos especiais a uma função
@api.get("/")
def raiz():
    resposta = "Essa é a raiz da aplicação"

    return resposta

