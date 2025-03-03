from robot.process import FinancialMarket, WhatsAppMessager

def main_menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Executar Financial Market")
        print("2. Executar WhatsApp Messager")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("Executando Financial Market...")
            FinancialMarket()
        elif opcao == "2":
            print("Executando WhatsApp Messager...")
            WhatsAppMessager()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main_menu()