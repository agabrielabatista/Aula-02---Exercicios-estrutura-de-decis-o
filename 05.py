renda = float(input("informe a sua renda mensal: "))
score =int(input("informe seu score "))
bens = input("possui bens como garantia?(sim/não) ")
historico = input("possui histórico de inadimplência? (sim/não)" )

if renda >= 3000 and score >= 600 and historico == "nao":
  print ("aprovado")
elif bens == "sim" and historico == "nao":
  print ("aprovado")
else:
    print ("reprovado")

