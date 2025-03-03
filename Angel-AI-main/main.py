from robot.process.FinancialMarket import monitor_stocks

def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Executar Financial Market")
        print("2. Executar WhatsApp Messager")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Executando Financial Market...")
            monitor_stocks()
        elif opcao == "2":
            print("Executando WhatsApp Messager...")
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
