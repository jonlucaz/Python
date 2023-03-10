altura = float(input("Quantos metros a parede tem de altura? "))
largura = float(input("Quantos metros a parede tem de largura? "))
parede = largura * altura
tinta = parede * 0.5

print(f'A sua parede tem {parede:.2f}m², você precisará de {tinta:.2f} litros de tinta para pintá-la.')
