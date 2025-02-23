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

def open_integration(content):
    """Envia um pedido de análise para a OpenAI e retorna a resposta."""
    try:
        print(f"{Fore.GREEN}[IA] Enviando solicitação de análise para OpenAI...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": content}],
            max_tokens=50
        )
        resposta = response.choices[0].message.content.strip()
        print(f"{Fore.GREEN}[IA] Resposta recebida com sucesso.")
        return resposta

    except Exception as e:
        print(f"{Fore.RED}[ERRO] Falha ao consultar a OpenAI: {e}")
        return None

def ask_stock_name_ai(ticker_name):
    """Consulta a OpenAI para identificar a qual banco pertence um ativo."""
    try:
        print(f"{Fore.GREEN}[IA] Consultando OpenAI para identificar o banco do ativo: {ticker_name}...")
        prompt = f"A qual banco pertence o ativo {ticker_name}? Responda apenas com o nome do banco, sem nenhuma informação adicional."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )

        banco = response.choices[0].message.content.strip()
        print(f"{Fore.GREEN}[IA] Resposta recebida: {banco}")
        return banco

    except Exception as e:
        print(f"{Fore.RED}[ERRO] Falha ao consultar OpenAI para {ticker_name}: {e}")
        return None

def ask_stock_description_ai(ticker_name):
    """Consulta a OpenAI para obter uma descrição detalhada sobre um ativo e sua relevância no mercado."""
    try:
        print(f"{Fore.GREEN}[IA] Consultando OpenAI para obter a descrição do ativo: {ticker_name}...")
        prompt = (
            f"Faça uma descrição precisa sobre o ativo {ticker_name}, incluindo sua relevância no mercado financeiro. "
            "Explique seus principais aspectos, histórico de valorização e importância para investidores, "
            "mas seja direto e objetivo na resposta."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150  # Ajustei para permitir respostas mais completas
        )

        descricao = response.choices[0].message.content.strip()
        print(f"{Fore.GREEN}[IA] Descrição recebida com sucesso.")
        return descricao

    except Exception as e:
        print(f"{Fore.RED}[ERRO] Falha ao consultar OpenAI para {ticker_name}: {e}")
        return None
    
def ask_sector_ai(ticker_name):
    """Consulta a OpenAI para obter o setor do ativo."""
    try:
        print(f"{Fore.GREEN}[IA] Consultando OpenAI para obter o setor do ativo: {ticker_name}...")
        prompt = f"Qual é o setor do ativo {ticker_name}? Responda apenas com o nome do setor, sem nenhuma informação adicional."

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=50
        )

        setor = response.choices[0].message.content.strip()
        print(f"{Fore.GREEN}[IA] Resposta recebida com sucesso: {setor}")
        return setor

    except Exception as e:
        print(f"{Fore.RED}[ERRO] Falha ao consultar OpenAI para {ticker_name}: {e}")
        return None
