idade =int (input("digite a sua idade:"))
if idade >= 18 and idade < 70:
   print("voto obrigátorio.")
elif idade >=16 and idade < 18:
   print("seu voto é facultativo.")
elif idade >=70:
   print("o seu voto é facultativo.")
else:
   print("não vota")