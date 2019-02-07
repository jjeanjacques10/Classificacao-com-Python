from sklearn.naive_bayes import MultinomialNB

#Gordinho?, Tem perninha curta?, Faz au au?
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

#Definindo como porco ou cachorro
marcacoes = [1, 1, 1, -1, -1, -1]

#Criando um modelo
modelo = MultinomialNB()

#Treinando o modelo
modelo.fit(dados, marcacoes)

#Elementos para teste
misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
teste = [misterioso1, misterioso2, misterioso3]
marcacoes_teste = [-1, 1, -1]


resultado = modelo.predict(teste)

#Mostrando o resultado
for r in range(len(resultado)):
    if resultado[r] == 1:
        print("É um porquinho", end=" ")
    else:
        print("É um cachorrinho", end=" ")
    if resultado[r] == marcacoes_teste[r]:
        print("[acertou]")
    else:
        print("[errou]")

#Calculando a taxa de acertos
diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print(resultado)
print(diferencas)
print(taxa_de_acerto)