# Ferramenta de Enriquecimento de CNPJ

Uma ferramenta Python simples e eficiente para enriquecer dados de CNPJ (Cadastro Nacional da Pessoa Jurídica) com informações adicionais através da API da ReceitaWS.

## O que você precisa

- Python 3.x (recomendamos a versão mais recente)
- pip (gerenciador de pacotes do Python)
- Acesso à internet (para consultar a API)

## Vamos começar!

1. Primeiro, clone este repositório:
```bash
git clone https://github.com/caio-andres/enriquecimento-cnpj.git
cd enriquecimento-cnpj
```

2. Crie e ative seu ambiente virtual (isso ajuda a manter as coisas organizadas):
```bash
python -m venv .venv

# No Windows
.venv\Scripts\activate

# No Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com a URL base da API:
```
API_BASE_URL="https://receitaws.com.br/v1/cnpj/"
```

O banco de dados SQLite será criado automaticamente na primeira vez que você rodar o programa, então não precisa se preocupar com isso! Ele ficará salvo em `db/empresas.db`.

## Como está organizado o projeto

```
enriquecimento-cnpj/
├── src/                    # Aqui está todo o código fonte
│   ├── main.py            # O ponto de entrada do programa
│   ├── enrich.py          # A mágica acontece aqui: enriquecimento dos dados
│   ├── database.py        # Tudo relacionado ao banco de dados
│   └── __init__.py        # Arquivo de inicialização do pacote
├── db/                     # Onde ficam os dados
│   └── empresas.db        # Nosso banco de dados SQLite
├── csv/                    # Arquivos CSV para processamento
│   ├── empresas.csv       # Coloque aqui os CNPJs que você quer enriquecer
│   └── empresas_enriquecidas.csv  # Aqui ficam os resultados
├── .venv/                  # Ambiente virtual Python
├── requirements.txt        # Lista de dependências
├── Makefile               # Comandos úteis
└── README.md              # Este arquivo aqui 😊
```

## Como usar

1. Ative o ambiente virtual:
```bash
# No Windows
.venv\Scripts\activate

# No Linux/Mac
source .venv/bin/activate
```

2. Execute o programa:
```bash
python -m src.main
```

## O que você vai precisar

- pandas: Para trabalhar com os dados
- requests: Para fazer as chamadas à API
- sqlalchemy: Para lidar com o banco de dados
- python-dotenv: Para gerenciar as configurações

## O que esta ferramenta faz

- Consulta dados básicos de CNPJ na ReceitaWS
- Enriquece os dados com informações complementares
- Salva tudo em um banco de dados SQLite (bem mais simples que PostgreSQL!)
- Processa vários CNPJs de uma vez
- Exporta os resultados para um arquivo CSV
- Cuida automaticamente de CNPJs duplicados

---

Construído com muito esforço por [Caio André](https://github.com/caio-andres) 😼