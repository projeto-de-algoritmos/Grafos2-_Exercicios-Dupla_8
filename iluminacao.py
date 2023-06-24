import heapq


def prim(grafo):
    mst = set()  # armazenar as arestas da árvore
    custo_total = 0  # variável para armazenar o custo total da árvore

    # escolher um nó  como ponto de partida
    no_inicial = list(grafo.keys())[0]
    visitados = set([no_inicial])  # armazena nós visitados

    # criar uma lista de arestas candidatas
    arestas = [(custo, no_inicial, vizinho) for vizinho, custo in grafo[no_inicial]]
    heapq.heapify(arestas)  # transformar a lista em uma fila de prioridade

    while arestas:
        # remover a aresta de menor custo
        custo, u, v = heapq.heappop(arestas)

        if v not in visitados:
            visitados.add(v)
            mst.add((u, v))
            custo_total += custo

            # adicionar as arestas adjacentes ao nó destino à fila de prioridade
            for vizinho, custo_vizinho in grafo[v]:
                if vizinho not in visitados:
                    heapq.heappush(arestas, (custo_vizinho, v, vizinho))

    # retornar o custo total da árvore geradora mínima
    return custo_total


def otimizar_iluminacao(m, n, estradas):
    grafo = {i: [] for i in range(m)}  # criar um dicionário para representar o grafo das cidades e estradas

    for x, y, z in estradas:
        # adicionar as cidades e o custo da estrada ao grafo
        grafo[x].append((y, z))
        grafo[y].append((x, z))

    # encontrar o custo total da árvore geradora mínima do grafo
    custo_total = prim(grafo)
    # calcular o custo restante das estradas que não fazem parte da árvore
    custo_restante = sum(custo for _, _, custo in estradas) - custo_total

    # retornar o custo restante como a economia de iluminação
    return custo_restante


# ler os dados de entrada até encontrar dois zeros
while True:
    m, n = map(int, input().split())  # ler o número de cidades e estradas
    if m == n == 0:  # se ambos forem zero, encerrar o programa
        break

    estradas = []  # criar uma lista para armazenar as estradas
    for _ in range(n):  # para cada estrada
        x, y, z = map(int, input().split())  # ler as cidades e o custo da estrada
        estradas.append((x, y, z))  # adicionar à lista

    # chamar a função de otimização e imprimir o resultado
    resultado = otimizar_iluminacao(m, n, estradas)
    print(resultado)
