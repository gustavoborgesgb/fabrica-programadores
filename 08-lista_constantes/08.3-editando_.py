nomes = ["joaquin","maria","ana"]
print("lista inicial: ",nomes)

nomes.append("carlos")# adicionar ao final da lista
print("apos append ",nomes)

nomes.insert(1,"fernanda") # insere fernanda no indice 1
print("apos insert ",nomes)


# modificando elemento 
nomes[2] = "paulo" # modificando o elemento no indice 2
print("apos modificaçao ",nomes)


#remover elemento
del nomes[3] # remover o elemento de indice 3 
print(" apos remover ",nomes)


nomes.remove("paulo")  # remover a primeira incidencia de maria
print("apos remover ", nomes)

removido = nomes.pop(2)
print("apos pop (removido {removido})", nomes)

nomes.clear()# esvazia a lista
print("apos cler ", nomes)
