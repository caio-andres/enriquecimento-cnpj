# Ferramenta de Enriquecimento de CNPJ

Uma ferramenta Python para enriquecer dados de CNPJ (Cadastro Nacional da Pessoa Jurídica) com informações adicionais através de APIs públicas e privadas.

## Pré-requisitos

- Python 3.x
- pip
- PostgreSQL
- Acesso à internet

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/caio-andres/enriquecimento-cnpj.git
cd enriquecimento-cnpj
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix/MacOS
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

1. Crie o arquivo `.env`:
```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/nome_do_banco
```

## Uso

1. Ative o ambiente virtual
2. Execute:
```bash
python main.py
```

## Estrutura

- `main.py`: Script principal
- `enrich.py`: Lógica de enriquecimento
- `database.py`: Conexão com PostgreSQL
- `requirements.txt`: Dependências

## Dependências

- pandas: Para manipulação e análise de dados
- requests: Para fazer requisições HTTP às APIs
- sqlalchemy: Para operações com banco de dados PostgreSQL
- python-dotenv: Para gerenciamento de variáveis de ambiente

## Funcionalidades

- Consulta de dados básicos de CNPJ
- Enriquecimento de dados com informações complementares
- Armazenamento em banco de dados PostgreSQL
- Processamento em lote de múltiplos CNPJs 