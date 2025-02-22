import time
from selenium import webdriver

def openPage(link: str):  # Corrigido o tipo do parâmetro
    driver = webdriver.Chrome()
    driver.get(link)
    return driver  # Retorna o driver para possível interação posterior
