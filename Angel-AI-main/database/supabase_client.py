import os
from supabase import create_client, Client

# Configurações do Supabase
SUPABASE_URL = "https://hferfjctasmpesfnccwb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhmZXJmamN0YXNtcGVzZm5jY3diIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAzMTQ4MjUsImV4cCI6MjA1NTg5MDgyNX0.PQJUIhFoNhXj-oTy8YM6VCqPskW9jG6gZOLVzhJUH0w"

# Criando cliente do Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_stocks(ticker: str, company_name: str, sector: str, description: str, prices_for_analysis: str):
    """
    Insere informações de ações no banco de dados do Supabase.

    Parâmetros:
    - ticker (str): Código da ação.
    - company_name (str): Nome da empresa.
    - stock_name (str): Nome da ação.
    - description (str): Descrição da ação
    - sector (str): Setor da empresa.
    - prices_for_analysis (str): Preços históricos formatados como JSON.

    Retorna:
    - Mensagem indicando sucesso ou erro.
    """
    try:
        response = supabase.table("stocks").insert({
            "ticker": ticker,
            "company_name": company_name,
            "sector": sector,
            "description": description,
            "prices_for_analysis": prices_for_analysis
        }).execute()

        data, error = response.data, response.error  # Ajuste para pegar os valores corretos

        if error:
            print(f"[ERRO] Falha ao inserir dados: {error}")
        else:
            print(f"[SUCESSO] Dados inseridos com sucesso: {data}")

    except Exception as e:
        print(f"[EXCEÇÃO] Ocorreu um erro inesperado: {e}")
