from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import date

from integration.OpenAI import open_integration

import time

def get_actions_menu():
    while True:
        print("\nMENU |")
        print("1 º  | Ações do Bradesco")
        print("2 º  | Ações do Itaú")
        print("3 º  | Ações da Vale")
        print("0 º  | Sair")

        option = input("Escolha uma opção: ").strip()
        
        if option == "0":
            print("Saindo do programa...")
            break
        elif option == "1":
            get_bradesco_stock()
        else:
            print("Opção inválida. Tente novamente.")

def get_bradesco_stock():
    print("\nBuscando ações do Bradesco...\n")

    # Configuração do Edge
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")

    # Inicializa o Edge WebDriver
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    driver.get("https://www.msn.com/pt-br/dinheiro/?id=avylgh")

    try:
        wait = WebDriverWait(driver, 10)  # Tempo máximo de espera para encontrar elementos

        # Aceitar cookies
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_button.click()
        except Exception:
            print("Nenhum botão de cookies encontrado.")

        # Localizar a barra de pesquisa e pesquisar por "Bradesco"
        search = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchBox']/input")))
        search.send_keys("Bradesco")
        time.sleep(2)
        search.send_keys(Keys.RETURN)
        
        # Action name
        action_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='fdc_header']/div/div/div/div[1]/div/div[2]/span")))
        print(f"NOME DA AÇÃO : {action_name.text}")
        
        # Esperar o preço da ação ser carregado
        in_closing_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price_display-DS-EntryPoint1-1")))
        print(f"NO FECHAMENTO : {in_closing_price.text}")
        
        today = date.today()
        print(f"DATA DE FECHAMENTO DO PREGÃO : {today}")    
        
        content = f"{action_name.text}, {in_closing_price.text}, {today}, Com base nos dados históricos, qual a tendência para essa ação nos próximos meses? Há projeções de alta ou queda, e quais fatores podem influenciar esse movimento?"
        
        open_integration(content)
        
        # Selecionar o período de 3 meses (se disponível)
        try:
            period = wait.until(EC.element_to_be_clickable((By.ID, "3MTimeFrameButton")))
            driver.execute_script("arguments[0].scrollIntoView();", period)  # Rola até o elemento
            period.click()
            print("Período de 1 mes selecionado.")
        except Exception:
            print("Botão do período de 3 meses não encontrado.")

        # Aguardar para ver o resultado
        time.sleep(100)

    except Exception as e:
        print(f"Erro ao coletar dados: {e}")

    finally:
        driver.quit()
