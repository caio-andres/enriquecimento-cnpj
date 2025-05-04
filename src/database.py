from sqlalchemy import create_engine, Table, Column, String, MetaData
from sqlalchemy.exc import IntegrityError

engine = create_engine("sqlite:///empresas.db")
metadata = MetaData()

companies = Table(
    "empresas",
    metadata,
    Column("cnpj", String, primary_key=True),
    Column("nome", String),
    Column("bairro", String),
    Column("municipio", String),
    Column("uf", String),
    Column("situacao", String),
)


def init_db():
    metadata.create_all(engine)
    print("Database initialized: empresas.db")


def insert_company(data: dict):
    with engine.begin() as conn:
        try:
            insert_stmt = companies.insert().values(
                cnpj=data.get("cnpj", ""),
                nome=data.get("nome", ""),
                bairro=data.get("bairro", ""),
                municipio=data.get("municipio", ""),
                uf=data.get("uf", ""),
                situacao=data.get("situacao", ""),
            )
            conn.execute(insert_stmt)
            print("Inserted: {data.get('cnpj')}")
        except IntegrityError:
            print("CNPJ duplicated ignored: {data.get('cnpj')}")
