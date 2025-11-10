'''Desenvolver uma API RESTful completa para gerenciar uma lista de tarefas (To-Do list). A implementação deve ser feita em Python utilizando um framework de sua escolha (sugestão: FastAPI ou Flask). Para simplificar o projeto e focar na lógica da API, o armazenamento de dados deve ser realizado em um banco de dados em memória (um dicionário ou lista em Python).
Adicionalmente, você deve criar uma suíte de testes unitários (sugestão: usando unittest ou Pytest) para validar todas as funcionalidades da API, garantindo que ela se comporte conforme o esperado.'''
Entidade Principal: Tarefa
A API deve gerenciar recursos do tipo Tarefa, que possuem os seguintes atributos:
id (string ou int): Identificador único da tarefa, que deve ser gerado automaticamente pela API.
titulo (string): Uma descrição curta e obrigatória da tarefa. Deve ter no mínimo 3 caracteres.
descricao (string): Um detalhamento opcional sobre a tarefa.
concluida (boolean): Um status que indica se a tarefa foi finalizada. O valor padrão ao criar uma nova tarefa deve ser false.
1. Requisitos Funcionais (Endpoints da API)

A API deve implementar as seguintes operações de CRUD (Create, Read, Update, Delete):
1.1. Criar uma Nova Tarefa
Endpoint: POST /tarefas
Corpo da Requisição (JSON): Deve conter titulo (obrigatório) e descricao (opcional).
Resposta de Sucesso (Código 201 Created): Retorna o objeto completo da tarefa recém-criada, incluindo o idgerado pelo servidor.
Resposta de Erro (Código 400 Bad Request ou 422 Unprocessable Entity): Retorna uma mensagem de erro se o titulo não for fornecido ou for inválido.
1.2. Listar Todas as Tarefas
Endpoint: GET /tarefas
Resposta de Sucesso (Código 200 OK): Retorna um array com todas as tarefas cadastradas. Se não houver tarefas, retorna um array vazio ([]).
1.3. Obter uma Tarefa Específica por ID
Endpoint: GET /tarefas/{id}
Resposta de Sucesso (Código 200 OK): Retorna o objeto completo da tarefa correspondente ao id.
Resposta de Erro (Código 404 Not Found): Retorna se nenhuma tarefa com o id especificado for encontrada.
1.4. Atualizar uma Tarefa Existente
Endpoint: PUT /tarefas/{id}
Corpo da Requisição (JSON): Deve conter todos os dados da tarefa que podem ser atualizados (titulo, descricao, concluida).
Resposta de Sucesso (Código 200 OK): Retorna o objeto da tarefa com os dados já atualizados.
Respostas de Erro:
Código 404 Not Found: Se o id não existir.
Código 400 Bad Request ou 422 Unprocessable Entity: Se a validação dos dados falhar (ex: titulovazio).
1.5. Deletar uma Tarefa
Endpoint: DELETE /tarefas/{id}
Resposta de Sucesso (Código 204 No Content): Retorna uma resposta sem corpo, indicando que o recurso foi removido com sucesso.
Resposta de Erro (Código 404 Not Found): Retorna se nenhuma tarefa com o id especificado for encontrada.
2. Requisitos de Testes Unitários

Você deve criar testes automatizados para garantir que cada endpoint funcione corretamente nos seguintes cenários:

'''Criação de Tarefa:
Testar a criação bem-sucedida.
Testar a falha na criação por falta do campo titulo.
Listagem de Tarefas:
Testar a listagem quando não há nenhuma tarefa (deve retornar uma lista vazia).
Testar a listagem quando existem uma ou mais tarefas.
Busca de Tarefa por ID:
Testar a busca por um id válido e existente.
Testar a busca por um id que não existe (deve retornar 404).
Atualização de Tarefa:
Testar a atualização bem-sucedida de uma tarefa.
Testar a tentativa de atualizar uma tarefa com um id inexistente (deve retornar 404).
Deleção de Tarefa:
Testar a deleção bem-sucedida de uma tarefa.
Verificar se, após a deleção, uma nova busca pelo mesmo id resulta em um erro 404.
Testar a tentativa de deletar uma tarefa com id inexistente (deve retornar 404).
faça a parte dos teste de acordo com o que se pede a cima como continuação da api a baixo
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict
from itertools import count
app = FastAPI(
    title="API de Tarefas (To-Do List)",
    description="API para realizar operações CRUD em tarefas.",
    version="1.0.0"'''
)'''
# Modelo de dados da tarefa usando Pydantic
class Tarefa(BaseModel):
    titulo: str = Field(..., min_length=3, description="Título da tarefa (mínimo 3 caracteres)")
    descricao: str = Field("", description="Descrição opcional da tarefa")
    concluida: bool = Field(default=False, description="Status da tarefa")
# Banco de dados em memória (dicionário)
db_tarefas: Dict[int, Tarefa] = {}
# Gerador automático de IDs
id_counter = count(1)
# ENDPOINTS DA API 
@app.get("/")
def read_root():
    
    """Endpoint raiz da API."""
    
    return {"message": "Bem-vindo à API de Tarefas! Acesse /docs para testar os endpoints."}
@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
   
    """Cria uma nova tarefa com ID gerado automaticamente."""
    
    tarefa_id = next(id_counter)
    db_tarefas[tarefa_id] = tarefa
    return {"id": tarefa_id, **tarefa.dict()}
@app.get("/tarefas")
def listar_tarefas():
    
    """Lista todas as tarefas cadastradas."""
    
    return [{"id": id, **tarefa.dict()} for id, tarefa in db_tarefas.items()]
@app.get("/tarefas/{id}")
def obter_tarefa(id: int):
    
    """Obtém uma tarefa específica pelo ID."""
    
    if id not in db_tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")
    return {"id": id, **db_tarefas[id].dict()}
@app.put("/tarefas/{id}")
def atualizar_tarefa(id: int, tarefa_atualizada: Tarefa):
    
    """Atualiza os dados de uma tarefa existente."""
    
    if id not in db_tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa atualizada")
    db_tarefas[id] = tarefa_atualizada
    return {"id": id, **tarefa_atualizada.dict()}
@app.delete("/tarefas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(id: int):
    
    """Deleta uma tarefa pelo ID."""
    
    if id not in db_tarefas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa deletada")
    
    del db_tarefas[id]
    return{"message": "tarefa deletada com sucesso!"}
