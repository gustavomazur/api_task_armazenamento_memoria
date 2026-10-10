# API Task

API REST de tarefas (CRUD) desenvolvida com **FastAPI**, utilizando armazenamento em memória por meio de uma lista de dicionários.

**Não utiliza banco de dados:** os dados existem apenas enquanto o servidor está em execução e são perdidos quando ele reinicia, voltando ao estado inicial definido em `my_task`.

## Tecnologias

- [Python](https://www.python.org/) 3.10+
- [FastAPI](https://fastapi.tiangolo.com/) — framework web para criação da API
- [Pydantic](https://docs.pydantic.dev/) — validação e estruturação dos dados
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI

## Estrutura do projeto

```text
api_task/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── __init__.py
│       └── task.py
├── requirements.txt
├── .gitignore
└── README.md
```

- `main.py`: cria a aplicação FastAPI e registra as rotas.
- `models.py`: mantém a lista `my_task`, utilizada como armazenamento em memória.
- `schemas.py`: define os modelos Pydantic para entrada e saída de dados.
- `routers/task.py`: define os endpoints do CRUD.

## Pré-requisitos

- Python 3.10 ou superior instalado.

Verifique a versão com:

```bash
python3 --version
```

## Como executar a API

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd api_task
```

Substitua `URL_DO_REPOSITORIO` pelo endereço real do repositório no GitHub.

### 2. Crie e ative um ambiente virtual

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

http://127.0.0.1:8000

A opção `--reload` reinicia o servidor automaticamente quando o código é alterado.
## Documentação interativa

Com o servidor em execução, acesse:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Você pode visualizar e testar os endpoints diretamente pelo Swagger UI ou utilizar o Insomnia para enviar requisições HTTP.

## Endpoints

Prefixo base: `/task`

| Método | Rota | Descrição | Status de sucesso |
|---|---|---|---|
| POST | `/task/` | Cria uma tarefa | 201 Created |
| GET | `/task/` | Lista todas as tarefas | 200 OK |
| GET | `/task/{id}` | Busca uma tarefa pelo ID | 200 OK |
| PATCH | `/task/{id}` | Atualiza parcialmente uma tarefa | 200 OK |
| DELETE | `/task/{id}` | Remove uma tarefa | 204 No Content |

## Modelo de tarefa

Exemplo de objeto retornado pela API:

```json
{
  "id": 1,
  "title": "Estudo FastAPI",
  "description": "CRUD",
  "published": true
}
```

### Campos

- `id`: inteiro gerado automaticamente pela API.
- `title`: string obrigatória.
- `description`: string opcional, podendo ser nula.
- `published`: booleano, com valor padrão `true`.

## Atualização parcial

O endpoint `PATCH /task/{id}` permite atualizar somente os campos desejados.

Por exemplo, você pode enviar apenas `title`, sem precisar enviar novamente a `descrição`,
Ou apenas enviar `descrição` sem enviar `title`.

## Observações importantes

- **Armazenamento em memória:** as tarefas ficam em uma lista no arquivo `app/models.py`. Ao reiniciar o servidor, as tarefas criadas são perdidas e a lista volta ao estado inicial definido no código.
- **IDs:** o próximo ID é calculado com `max(id) + 1`, conforme a implementação atual. Isso evita reutilizar IDs que ainda estejam presentes na lista, inclusive após a remoção de outras tarefas.
- **Finalidade:** projeto desenvolvido para fins de estudo e prática de desenvolvimento de APIs REST com FastAPI.
