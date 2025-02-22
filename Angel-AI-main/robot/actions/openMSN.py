import time

from selenium import webdriver
from robot.library.WebDriver import openPage

def getActions():
    openPage("https://www.msn.com/pt-br/dinheiro/?id=avylgh")

    print("MENU|")
    print("1 º | Ações da bradesco")
    print("2 º | Ações do Itau")
    print("3 º | Ações da Vale")

    option = input(" Escolha uma opção : ")

    
