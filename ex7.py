
#LETRA B
lista_filmes = ["Missão Impossível" , "Frozen" , "Rei Leão" , "Infiltrado"]
#LETRA A
lista_filmes.insert(3 , "Homen Aranha 3")
lista_filmes.insert(4 , "Indiana Jones")
#LETRA A
print("LISTA DE FILMES")
print(lista_filmes)

#LETRA B
lista_jogos = ["Fortnite" , "Free Fire" , "Valorant" , "Red dead Redemption"]
#LETRA A 
lista_jogos.insert(1 , "Forza")
lista_jogos.insert(4 , "CS:GO")
#LETRA A
print("LISTA DE JOGOS")
print(lista_jogos)

#LETRA B
lista_livros = ["Anie Frank" , "O alienita" , "O filho de Netuno" , "Dom Casmurro"]
#LETRA A 
lista_livros.insert(3, "O estrangeiro")
lista_livros.insert(2, "Diario de um Banana vol.1")
#LETRA A
#LETRA C
print("LISTA DE LIVROS")
print(lista_livros[1])

#LETRA B
lista_esportes = ["Futebol" , "Volêi" , "Basket" , "Frisby"]
#LETRA A
lista_esportes.insert(1, "atletismo")
lista_esportes.insert(3, "Natação")
#LETRA A

#LETRA D
del lista_esportes[2]
#LETRA D
print("LISTA DE ESPORTES")
print(lista_esportes)

#LETRA C
print("LISTA GERAL")
lista_nova = [ lista_esportes ,lista_filmes , lista_jogos , lista_livros ]
lista_nova.insert(4, "disciplina[]")

print(lista_nova)
#LETRA C