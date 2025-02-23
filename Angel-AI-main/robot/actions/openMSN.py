import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from integration.OpenAI import open_integration, ask_stock_name_ai, ask_stock_description_ai
from database.supabase_client import insert_stocks

def initialize_driver():
    """Configura e retorna um WebDriver do Edge."""
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    return driver

def get_stock_data(ticker_name, driver, wait):
    """Obtém os dados da ação de um banco específico."""
    print(f"\nBuscando ações de {ticker_name}...\n")

    driver.get("https://www.msn.com/pt-br/dinheiro/?id=avylgh")

    try:
        # Aceitar cookies (se necessário)
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_button.click()
        except Exception:
            pass  # Ignora se o botão não estiver presente

        # Localizar a barra de pesquisa e pesquisar pelo ativo
        search = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchBox']/input")))
        search.send_keys(ticker_name)
        time.sleep(2)
        search.send_keys(Keys.RETURN)

        # Nome da ação
        action_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='fdc_header']//span")))
        action_text = action_name.text.strip()

        # Preço da ação
        try:
            price_info = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "priceInfo-DS-EntryPoint1-1")))
            prices_info_text = price_info.text.strip()
        except Exception:
            print(f"[ERRO] Não foi possível encontrar a precificação de {ticker_name}.")
            return

        # Data de fechamento do pregão
        today = date.today().strftime("%Y-%m-%d")

        # Criar JSON para preços para análise
        prices_for_analysis = f'{{"{today}": "{prices_info_text}"}}'

        # Descobrir o nome do banco associado ao ativo usando OpenAI
        bank_name_text = ask_stock_name_ai(ticker_name)
        print(f"{bank_name_text}")
        
        stock_description = ask_stock_description_ai(ticker_name)

        # Inserir dados no Supabase
        insert_stocks(ticker_name, bank_name_text, action_text, action_text, "Financeiro", prices_for_analysis)

        # Apenas imprime quando os dados são inseridos com sucesso
        print(f"[SUCESSO] Dados inseridos para {ticker_name}: Nome: {action_text}, Preço: {prices_info_text}, Data: {today}")

        # Selecionar período de 3 meses (se disponível)
        try:
            period = wait.until(EC.element_to_be_clickable((By.ID, "3MTimeFrameButton")))
            driver.execute_script("arguments[0].scrollIntoView();", period)
            period.click()
        except Exception:
            pass  # Ignora se o botão não for encontrado

        time.sleep(5)  # Pequena pausa antes de ir para o próximo ativo

    except Exception as e:
        print(f"[ERRO] Falha ao coletar dados para {ticker_name}: {e}")
