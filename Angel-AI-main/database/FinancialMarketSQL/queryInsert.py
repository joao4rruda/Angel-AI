from database.supabase_client import get_supabase_client  # Importando a função da outra classe

# Criando a variável global supabase
supabase = get_supabase_client()

def insert_stocks(ticker: str, company_name: str, sector: str, description: str, prices_for_analysis: str):
    """
    Insere informações de ações no banco de dados do Supabase.

    Parâmetros:
    - ticker (str): Código da ação.
    - company_name (str): Nome da empresa.
    - sector (str): Setor da empresa.
    - description (str): Descrição da ação.
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

        if hasattr(response, 'data') and response.data:
            print(f"[SUCESSO] Dados inseridos com sucesso: {response.data}")
        elif hasattr(response, 'error') and response.error:
            print(f"[ERRO] Falha ao inserir dados: {response.error}")
        else:
            print("[ERRO] Resposta inesperada do Supabase.")
    except Exception as e:
        print(f"[EXCEÇÃO] Ocorreu um erro inesperado: {e}")