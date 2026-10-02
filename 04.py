estudante = input("você é estudante? (sim/não) ")
semana = input("qual o dia da semana? ")
sala = input("vip ou comum? ")

if  estudante == "sim" or semana == "terca" and sala == "comum":
   print ("desconto aplicado")
else:
    print ("valor integral")
   