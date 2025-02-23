import time  
from selenium.webdriver.support.ui import WebDriverWait
from robot.actions.openMSN import get_stock_data, initialize_driver

# Lista de ativos bancários a serem monitorados
TICKERS = [
    "ITUB3", "ITUB4", "BBDC3", "BBDC4", "BBAS3", "SANB3", 
    "SANB4", "SANB11", "BRSR3", "BRSR5", "BRSR6", "BPAC3",
    "BPAC5", "BPAC11", "INBR31", "ROXO34", "BPAN4"
]  

# Inicializa o driver do Selenium
driver = initialize_driver()
wait = WebDriverWait(driver, 10)

try:
    while True:
        for ticker in TICKERS:
            print(f"\n[INFO] Pesquisando ações de: {ticker}")
            get_stock_data(ticker, driver, wait)
            print(f"[INFO] {ticker} processado. Aguardando antes da próxima pesquisa...\n")
            time.sleep(5)  # Pequena pausa entre as pesquisas

        print("\n[INFO] Todas as buscas foram concluídas. Aguardando 1 hora para a próxima varredura...\n")
        time.sleep(3600)  # Aguarda 1 hora antes de repetir o processo

except KeyboardInterrupt:
    print("\n[INFO] Monitoramento interrompido pelo usuário.")

finally:
    print("[INFO] Fechando o navegador...")
    driver.quit()  # Garante o encerramento do navegador
