salario = float(input("Digite o salário total do funcionário: R$"))
porcentagem = (salario * 15) / 100
novo_sal = salario + porcentagem
print(f'O novo salário do funcionário com 15% de aumento é de R${novo_sal:.2f} e o '
      f'aumento total foi de R${porcentagem:.2f}')

