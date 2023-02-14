conta_normal = False
conta_universitario = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não é possível realizar o saque.")
elif conta_universitario:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficeinte!")
else:
    print("Sistema não reconheceu o tipo de conta, favor entrar em contato com o Gerente!")