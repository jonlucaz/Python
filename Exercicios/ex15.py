dia = float(input("Quantos dias você ficou com o carro? "))
km = float(input("Quantos quilometros rodados? "))
valor_dia = dia * 60
valor_km = km * 0.15
total = valor_dia + valor_km
print(f'O valor total a ser pago é de R${total:.2f} sendo R${valor_dia:.2f} por dia e R${valor_km:.2f} '
      f'pelos km rodados.')
