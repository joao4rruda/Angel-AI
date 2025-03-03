import os
import openai
from colorama import init, Fore

# Inicializa o colorama para compatibilidade com Windows
init(autoreset=True)

# Obtém a chave da API do ambiente
api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print(f"{Fore.GREEN}[INFO] Chave da API OpenAI encontrada e carregada com sucesso.")
else:
    print(f"{Fore.RED}[ERRO] Variável de ambiente OPENAI_API_KEY não está definida!")

def ask_openai(prompt, max_tokens=50):
    """Consulta a OpenAI com um prompt e retorna a resposta."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"{Fore.RED}[ERRO] Falha ao consultar OpenAI: {e}")
        return None

def ask_stock_name_ai(ticker_name):
    """Obtém o nome do banco ao qual pertence um ativo."""
    print(f"{Fore.GREEN}[IA] Identificando o banco do ativo: {ticker_name}...")
    prompt = f"A qual banco pertence o ativo {ticker_name}? Responda apenas com o nome do banco."
    return ask_openai(prompt)

def ask_stock_description_ai(ticker_name):
    """Obtém uma análise do ativo no mercado financeiro."""
    print(f"{Fore.GREEN}[IA] Obtendo análise do ativo: {ticker_name}...")
    prompt = (
        f"Forneça uma análise objetiva sobre o status atual do ativo {ticker_name} no mercado financeiro. "
        f"Explique sua relevância para investidores, considerando desempenho recente, volatilidade e tendências."
    )
    return ask_openai(prompt, max_tokens=150)

def ask_sector_ai(ticker_name):
    """Obtém o setor do ativo."""
    print(f"{Fore.GREEN}[IA] Identificando o setor do ativo: {ticker_name}...")
    prompt = f"Qual é o setor do ativo {ticker_name}? Responda apenas com o nome do setor."
    return ask_openai(prompt)
