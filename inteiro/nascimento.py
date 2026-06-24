ano_nascimento = int(input("digite o ano"))
ano_atual = 2026
idade = ano_atual - ano_nascimento
if idade>=16:
   print("você poderá votar este ano!")
else:
   print("você não poderá votar este ano.")