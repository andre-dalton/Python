saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp)
print(exp_2)