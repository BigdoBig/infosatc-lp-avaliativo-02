valor1 = float(input("Digite o seu primeiro valor : "))
valor2 = float(input("Digite o seu segundo valor : "))
valor3 = float(input("Digite o seu terceiro valor : "))
valor4 = float(input("Digite o seu quarto valor : "))

lista_soma = [valor1, valor2 , valor3 , valor4]
soma = sum(lista_soma)

print("A soma de todos os valores da sua lista é : {} ".format(soma))