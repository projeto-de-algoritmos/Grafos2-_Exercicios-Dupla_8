import heapq


class No:
    def __init__(self, idioma):
        self.idioma = idioma  # língua do nó
        self.adjacentes = []  # lista de nós adjacentes
        self.visitado = False  # lndica se o nó já foi visitado durante a busca
        self.distancia = float('inf')

    def __lt__(self, outro):
        return self.distancia < outro.distancia  # comparação de distâncias para a fila de prioridade


def dijkstra(grafo, no_inicial, no_final):
    no_inicial.distancia = 0
    fila_prioridade = [(0, no_inicial)]

    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)  # remove o nó de menor distância da fila
        if no_atual.visitado:
            continue

        no_atual.visitado = True

        if no_atual == no_final:
            return distancia_atual

        for vizinho, peso in no_atual.adjacentes:  # percorre os nós adjacentes ao nó atual
            distancia = distancia_atual + peso  # calcula a distância até o nó adjacente
            if distancia < vizinho.distancia and vizinho.idioma[0] != no_atual.idioma[0]:
                # se a nova distância for menor e as línguas não forem a mesma inicial, atualiza a distância do nó
                vizinho.distancia = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))  # insere o nó na fila de prioridade

    return 'impossivel'  # se não for possível alcançar o nó final


while True:
    m = int(input())  # lê o número de relações de palavras

    if m == 0:  # se o número for 0, encerra o programa
        break

    palavras = {}  # dic para armazenar as relações de palavras
    grafo = {}  # dic para armazenar os nós do grafo

    origem, destino = input().split()  # lê a língua de origem e destino

    for _ in range(m):
        idioma1, idioma2, palavra = input().split()  # lê os idiomas e a plavra
        palavras[(idioma1, idioma2)] = palavra  # armazena no dic

        # verifica se os nós da relação já existem no grafo, senão cria
        if idioma1 not in grafo:
            grafo[idioma1] = No(idioma1)

        if idioma2 not in grafo:
            grafo[idioma2] = No(idioma2)

    for (idioma1, idioma2), palavra in palavras.items():
        no1 = grafo[idioma1]
        no2 = grafo[idioma2]  # obtém o nó correspondente à língua 2
        peso = len(palavra)  # peso da aresta é o tamanho da palavra

        # adiciona a aresta aos nós adjacentes
        no1.adjacentes.append((no2, peso))
        no2.adjacentes.append((no1, peso))

    if origem in grafo and destino in grafo:
        no_inicial = grafo[origem]  # obtém o nó inicial do grafo
        no_final = grafo[destino]  # obtém o nó final do grafo
        resultado = dijkstra(grafo, no_inicial, no_final)
        print(resultado)
    else:
        print('impossivel')

