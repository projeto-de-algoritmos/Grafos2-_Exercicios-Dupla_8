import heapq


def adicionarArestasDoInicio(sx, sy, X, Y, no):
    for i in range(len(X)):
        # calcular o peso da aresta como o mínimo entre as distâncias horizontais e verticais
        w = min(abs(sx - X[i][0]), abs(sy - Y[i][0]))
        no[0].append((X[i][1], w))


def adicionarArestasDoFim(ex, ey, X, Y, no, m):
    for i in range(len(X)):
        # calcular o peso da aresta como a soma das distâncias horizontais e verticais
        w = abs(ex - X[i][0]) + abs(ey - Y[i][0])
        no[X[i][1]].append((m + 1, w))
        w = abs(ex - sx) + abs(ey - sy)
        no[0].append((m + 1, w))


def adicionarArestas(coordenada, no):
    # para cada par de pontos consecutivos na lista ordenada de coordenadas
    for i in range(1, len(coordenada)):
        # obter os identificadores dos pontos
        id1 = coordenada[i - 1][1]
        id2 = coordenada[i][1]
        # calcular o peso da aresta
        w = coordenada[i][0] - coordenada[i - 1][0]
        no[id1].append((id2, w))
        no[id2].append((id1, w))


def dijkstra(n, m, sx, sy, ex, ey, coordX, coordY):
    # criar uma lista de listas para representar o grafo das arestas
    no = [[] for _ in range(m + 2)]
    adicionarArestasDoInicio(sx, sy, coordX, coordY, no)
    adicionarArestasDoFim(ex, ey, coordX, coordY, no, m)
    coordX.sort()
    coordY.sort()
    # chamar a função auxiliar para adicionar as arestas entre os pontos intermediários
    adicionarArestas(coordX, no)
    adicionarArestas(coordY, no)
    # fila de prioridade
    fila_prioridade = [(0, 0)]
    # lista de distâncias
    distancia = [float('inf')] * (m + 2)
    feito = [False] * (m + 2)
    distancia[0] = 0
    while fila_prioridade:
        # remover o par com menor distância da fila
        atual = heapq.heappop(fila_prioridade)
        # se o nó é o ponto de fim encerra
        if atual[1] == m + 1:
            distancia[m + 1] = atual[0]
            break
        if feito[atual[1]]:
            continue
        id = atual[1]
        w = atual[0]
        feito[id] = True
        distancia[id] = w
        for aresta in no[id]:
            if distancia[aresta[0]] > w + aresta[1]:
                # inserir o par na fila de prioridade
                heapq.heappush(fila_prioridade, (w + aresta[1], aresta[0]))
    # retornar a distância mínima do ponto de fim
    return distancia[m + 1]


# Leitura de entrada
n, m = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())
coordX = []
coordY = []
for _ in range(m):
    a, b = map(int, input().split())
    coordX.append((a, len(coordX) + 1))
    coordY.append((b, len(coordY) + 1))

# Chamada da função para obter a menor distância
resultado = dijkstra(n, m, sx, sy, ex, ey, coordX, coordY)
print(resultado)
