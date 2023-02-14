menu = f"""
       MENU

[0] - Deposito
[1] - Sacar
[2] - Extrato
[3] - Sair
"""
saldo = 0
quantidade_saques = 0
d = 0
s = 0
extract = ""

while True:

    escolha = input(menu)

    if escolha == "0":
        d = int(input("Quanto você deseja depositar? "))
        if d > 0:
            saldo = saldo + d
            extract += f" R$ {d:.2f}\n" 
        else:
            print("Valor inválido para deposito.")     
    
    elif escolha == "1":
        if quantidade_saques < 3:
            if saldo > 0:
                s = int(input("Quanto você deseja sacar? "))
                if s < 0:
                    print("Valor de saque inválido.")
                elif s > 500:
                   print("Limite permitido para saque é de R$500,00.")
                else:
                    saldo = saldo - s
                    extract += f"-R$ {s:.2f}\n" 
                    quantidade_saques += 1
            else:
                print("Saldo insuficiente")   
        else:
            print("Limite de saques diário atingido.")
   
    elif escolha == "2":
         print("\n-------------- Extrato --------------")
         if d == 0 | d <= 0  & s == 0 | s <= 0:
             print("Não foram realizadas movimentações.")
         else:
             print(f"\n{extract}")
         print(f"\nSaldo atual é: R$ {saldo:.2f}")
         print("-------------------------------------")

    elif escolha == "3":
         print("Obrigado por utilizar nosso banco!")
         break
    
    else:
        print("Opção inválida")