import time  
from selenium.webdriver.support.ui import WebDriverWait
from robot.actions.openMSN import get_stock_data, initialize_driver

# Lista de bancos a serem monitorados
BANKS = ["AAPL", "GOOGL", "MSFT"]  # Substitua pelos ativos desejados

# Inicializa o driver do Selenium
driver = initialize_driver()
wait = WebDriverWait(driver, 10)

try:
    while True:
        for bank in BANKS:
            print(f"\n[INFO] Pesquisando ações de: {bank}")
            get_stock_data(bank, driver, wait)

            print(f"[INFO] {bank} processado. Aguardando antes da próxima pesquisa...\n")
            time.sleep(5)  # Aguarde 5 segundos antes de pesquisar o próximo (ajuste conforme necessário)

        print("\n[INFO] Todas as buscas foram concluídas. Aguardando 1 hora para a próxima varredura...\n")
        # time.sleep(3600)  # Aguarda 1 hora antes de repetir o processo

except KeyboardInterrupt:
    print("\n[INFO] Monitoramento interrompido pelo usuário.")

finally:
    driver.quit()  # Garante que o navegador será fechado corretamente
