import pandas as pd
import requests
import time
import os
from src.database import insert_company

API_BASE_URL = os.getenv("API_BASE_URL")


def consult_cnpj(cnpj: str) -> dict | None:
    try:
        response = requests.get(
            f"{API_BASE_URL}{cnpj}", headers={"User-Agent": "Mozilla/5.0"}
        )
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "OK":
                return {
                    "cnpj": data.get("cnpj", ""),
                    "nome": data.get("nome", ""),
                    "bairro": data.get("bairro", ""),
                    "municipio": data.get("municipio", ""),
                    "uf": data.get("uf", ""),
                    "situacao": data.get("situacao", ""),
                }
            else:
                print(f"API Error to CNPJ {cnpj}: {data.get('message')}")
        else:
            print(f"Status code {response.status_code} for CNPJ {cnpj}")
    except Exception as e:
        print(f"Exception trying consult CNPJ {cnpj}: {e}")
    return None
  
def enrich_all(input_path: str):
  df = pd.read_csv(input_path)
  enriched_data = []
  
  for index, row in df.iterrows():
    cnpj = str(row["cnpj"]).zfill(14)
    print(f"Consulting CNPJ: {cnpj}")
    datas = consult_cnpj(cnpj)
    if datas:
      enriched_data.append(datas)
      insert_company(datas)
    time.sleep(1.5) # It's limited to 1.5 to avoid the rate limit from API
    