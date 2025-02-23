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

from integration.OpenAI import open_integration
from database.supabase_client import insert_stocks

# Lista de bancos suportados
BANKS = ["Bradesco", "Itaú", "Vale"]

def initialize_driver():
    """ Configura e retorna um WebDriver do Edge. """
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--no-sandbox")

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
    return driver

def get_stock_data(bank_name, driver, wait):
    """ Obtém os dados da ação de um banco específico. """
    print(f"\nBuscando ações do {bank_name}...\n")

    driver.get("https://www.msn.com/pt-br/dinheiro/?id=avylgh")

    try:
        # Aceitar cookies (se necessário)
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_button.click()
        except Exception:
            print("Nenhum botão de cookies encontrado.")

        # Localizar a barra de pesquisa e pesquisar pelo banco
        search = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='searchBox']/input")))
        search.send_keys(bank_name)
        search.send_keys(Keys.RETURN)

        # Nome da ação
        action_name = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='fdc_header']//span")))
        action_text = action_name.text.strip()
        print(f"NOME DA AÇÃO: {action_text}")

        # Preço da ação no fechamento
        try:
            closing_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price_display-DS-EntryPoint1-1")))
        except Exception:
            closing_price = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "priceInfo-DS-EntryPoint1-1")))

        closing_price_text = closing_price.text.strip()
        print(f"PREÇO NO FECHAMENTO: {closing_price_text}")

        # Data de fechamento do pregão
        today = date.today().strftime("%Y-%m-%d")
        print(f"DATA DE FECHAMENTO DO PREGÃO: {today}")

        # Criar conteúdo para análise
        content = f"{action_text}, {closing_price_text}, {today}, Com base nos dados históricos, qual a tendência para essa ação nos próximos meses?"

        # Criar JSON para preços para análise
        prices_for_analysis = f'{{"{today}": "{closing_price_text}"}}'

        # Inserir dados no Supabase
        insert_stocks(bank_name, action_text, action_text, "Financeiro", prices_for_analysis)

        # Enviar para análise da OpenAI
        open_integration(content)

        # Selecionar período de 3 meses (se disponível)
        try:
            period = wait.until(EC.element_to_be_clickable((By.ID, "3MTimeFrameButton")))
            driver.execute_script("arguments[0].scrollIntoView();", period)
            period.click()
            print("Período de 3 meses selecionado.")
        except Exception:
            print("Botão do período de 3 meses não encontrado.")

    except Exception as e:
        print(f"Erro ao coletar dados para {bank_name}: {e}")
