preco = float(input("Digite o preço do produto: R$"))
porcentagem = (preco * 5) / 100
novo_preco = preco - porcentagem
print(f'O novo preço com 5% de desconto é de R${novo_preco:.2f} e o desconto total foi de R${porcentagem:.2f}')
