from src.enrich import enrich_all
from src.database import init_db


def main():
    init_db()
    enrich_all("csv/empresas.csv")


if __name__ == "__main__":
    main()
