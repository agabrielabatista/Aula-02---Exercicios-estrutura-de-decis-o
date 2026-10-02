idade = int(input("digite sua idade "))
altura = int(input("digite sua altura "))
autorização = input("possui autorização? (sim/não) ")


if idade >= 12 and altura >= 140 and autorização == "sim":
    print ("acesso liberado")
else:
    print ("acesso negado")
    