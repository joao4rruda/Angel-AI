from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_actions_menu():
    openPage("https://www.msn.com/pt-br/dinheiro/?id=avylgh")

    print("MENU|")
    print("1 º | Ações da bradesco")
    print("2 º | Ações do Itau")
    print("3 º | Ações da Vale")

    option = input(" Escolha uma opção : ")
    
def options_started():
    # Paramos aqui
    
def get_bradesco_stock():
    # Configura o driver do Chrome
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.msn.com/pt-br/dinheiro/?id=avylgh")
    
    time.sleep(5) # Espera para carregar a pagina
    
    try:
        # Exemplo de como localizar os dados das ações (ajuste conforme necessário)
        stock_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'finance-symbol')]")
        
        for stock in stock_elements:
            name = stock.find_element(By.XPATH, ".//span[contains(@class, 'finance-symbol-name')]").text
            price = stock.find_element(By.XPATH, ".//span[contains(@class, 'finance-symbol-price')]").text
            variation = stock.find_element(By.XPATH, ".//span[contains(@class, 'finance-symbol-change')]").text
            
            if "Bradesco" in name:
                print(f"Ação: {name}")
                print(f"Preço: {price}")
                print(f"Variação: {variation}")
                print("-" * 30)
                break
    except Exception as e:
        print(f"Erro ao coletar dados: {e}")
    
    driver.quit()
    
