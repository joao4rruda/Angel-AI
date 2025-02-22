import os
import openai

api_key = os.getenv("OPENAI_API_KEY")  # Obtém a variável de ambiente

if api_key:
    print(f"Chave da API encontrada: {api_key}")
else:
    print("Erro: Variável de ambiente OPENAI_API_KEY não está definida!")

def openIntegration():
    content = input("Escreva algo : ")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": content}
        ],
        max_tokens=50
    )
    return print(response.choices[0].message.content.strip())
