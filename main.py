automato = open("automato.txt", "r")

estados = automato.readline().split()

alfabeto = automato.readline().split()

estadoInicial = automato.readline().split()

estadosFinais = automato.readline().split()

trilha = []

for i in range(len(estados)):
    trilhaAutomato = automato.readline().split()
    if len(trilhaAutomato) == len(alfabeto):
        trilha.append(trilhaAutomato)
    else:
        raise Exception("Automato inválido")


entrada = open("entrada.txt", "r")

entradas = []
linha = entrada.readline().rstrip()
while len(linha) > 0:
    entradas.append(linha)
    linha = entrada.readline().rstrip()
print("Entradas:")
for i in entradas:
    print(i)

saida = open("saida.txt", "w+")

for entradaLinha in entradas:
    atual = estadoInicial[0]
    for i in entradaLinha:

        # achar o prox atual.
        for x in range(len(estados)):
            if atual == str(estados[x]):
                coluna = x

        for x in range(len(alfabeto)):
            if i == alfabeto[x]:
                linha = x

        atual = trilha[coluna][linha]

    aceita = False
    for final in estadosFinais:
        if final == atual:
            aceita = True
            saida.write("ACEITO\n")
    if aceita == False:
        saida.write("NEGADO\n")

automato.close()
entrada.close()
saida.close()

