import os
import openai

api_key = os.getenv("OPENAI_API_KEY")  # Obtém a variável de ambiente

if api_key:
    print(f"Chave da API encontrada: {api_key}")
else:
    print("Erro: Variável de ambiente OPENAI_API_KEY não está definida!")

def open_integration(content):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ],
        max_tokens=50
    )
    return print(response.choices[0].message.content.strip())

def ask_stock_to_ai(stock):
    """Envia uma consulta à OpenAI para identificar a qual banco pertence um ativo."""
    try:
        content += " Esse ativo pertence a qual banco?"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": stock}],
            max_tokens=50
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Erro ao consultar OpenAI: {e}")
        return response
