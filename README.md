# Ferramenta de Enriquecimento de CNPJ

Uma ferramenta Python para enriquecer dados de CNPJ (Cadastro Nacional da Pessoa Jurídica) com informações adicionais.

## Começando

### Pré-requisitos

- Python 3.x
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone este repositório:
```bash
git clone <url-do-repositorio>
cd enriquecimento-cnpj
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Unix ou MacOS:
source .venv/bin/activate
```

3. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

### Estrutura do Projeto

- `main.py`: Ponto de entrada principal da aplicação
- `enrich.py`: Contém a lógica de enriquecimento de CNPJ
- `database.py`: Conexão e operações com banco de dados
- `requirements.txt`: Dependências do projeto

### Configuração do Ambiente

Crie um arquivo `.env` no diretório raiz com as seguintes variáveis:
```
DATABASE_URL=sua_string_de_conexao_com_banco_de_dados
```

### Executando a Aplicação

1. Certifique-se de que seu ambiente virtual está ativado
2. Execute o script principal:
```bash
python main.py
```

## Dependências

- pandas: Para manipulação e análise de dados
- requests: Para fazer requisições HTTP
- sqlalchemy: Para operações com banco de dados
- python-dotenv: Para gerenciamento de variáveis de ambiente 