import heapq

n = float('inf')

def Main():
    matrix = DefaultMatrix(12)
    SetEdges(matrix)
    PrintMatrix(matrix)

    primMst = Prim(matrix)
    PrintMethod(primMst, 'Прима')

    kruskalMst = Kruskal(matrix)
    PrintMethod(kruskalMst, 'Краскала')

    boruvkaMst, boruvkaWeight = Boruvka(matrix)
    print(f'\nМетод Буровки')
    print(f'{boruvkaMst}')
    print(f'Вес {boruvkaWeight}\n')


def PrintMethod(mst, method):
    w = 0
    for(_, _, pw) in mst:
        w += pw
    print(f'\nМетод {method}')
    print(f'{mst}')
    print(f'Вес {w}')

def DefaultMatrix(v):
    matrix = []
    for i in range(v):
        row = []
        for j in range(v):
            if i == j :
                row.append(0)
            else:
                row.append(n)
        matrix.append(row)
    return matrix

def SetEdges(matrix):
    SetEdge(matrix, 1, 2, 5)
    SetEdge(matrix, 1, 4, 7)
    SetEdge(matrix, 1, 5, 1)
    SetEdge(matrix, 1, 6, 3)
    SetEdge(matrix, 2, 3, 1)
    SetEdge(matrix, 2, 4, 1)
    SetEdge(matrix, 2, 5, 4)
    SetEdge(matrix, 2, 6, 3)
    SetEdge(matrix, 2, 7, 8)
    SetEdge(matrix, 3, 5, 2)
    SetEdge(matrix, 3, 7, 11)
    SetEdge(matrix, 4, 5, 3)
    SetEdge(matrix, 4, 6, 4)
    SetEdge(matrix, 4, 7, 1)
    SetEdge(matrix, 5, 6, 2)
    SetEdge(matrix, 5, 7, 6)
    SetEdge(matrix, 6, 7, 2)
    SetEdge(matrix, 6, 8, 2)
    SetEdge(matrix, 6, 9, 4)
    SetEdge(matrix, 6, 10, 7)
    SetEdge(matrix, 6, 11, 1)
    SetEdge(matrix, 7, 8, 9)
    SetEdge(matrix, 7, 9, 3)
    SetEdge(matrix, 7, 11, 2)
    SetEdge(matrix, 7, 12, 2)
    SetEdge(matrix, 8, 9, 9)
    SetEdge(matrix, 8, 10, 3)
    SetEdge(matrix, 8, 11, 4)
    SetEdge(matrix, 8, 12, 8)
    SetEdge(matrix, 9, 11, 6)
    SetEdge(matrix, 9, 12, 1)
    SetEdge(matrix, 10, 11, 5)
    SetEdge(matrix, 11, 12, 2)

def SetEdge(matrix, start, end, weight):
    matrix[start-1][end-1] = weight
    matrix[end-1][start-1] = weight

def Prim(matrix):
    n = len(matrix)
    visited = [False] * n
    min_heap = [(2, 3, 1)]  # (from_node, to_node, weight)
    visited[3] = True
    mst = []
    while len(mst) < n - 1:
        weight, from_node, to_node = heapq.heappop(min_heap)
        if visited[to_node]:
            continue
        visited[to_node] = True
        mst.append((from_node, to_node, weight))
        for neighbor, weight in enumerate(matrix[to_node]):
            if not visited[neighbor] and weight != 0:
                heapq.heappush(min_heap, (weight, to_node, neighbor))
    return mst


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def Kruskal(matrix):
    n = len(matrix)
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != 0:
                edges.append((matrix[i][j], i, j))
    edges.sort()
    parent = [i for i in range(n)]
    rank = [0] * n
    mst = []
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)
    return mst


def Boruvka(adj_matrix):
    V = len(adj_matrix)
    parent = [i for i in range(V)]
    rank = [0] * V
    mst_edges = []
    mst_weight = 0

    num_trees = V
    while num_trees > 1:
        # Массив для хранения минимальных рёбер для каждой компоненты
        cheapest = [-1] * V

        # Проходим по всем рёбрам графа
        for u in range(V):
            for v in range(V):
                if adj_matrix[u][v] != 0:  # Если ребро существует
                    set1 = find(parent, u)
                    set2 = find(parent, v)

                    # Если вершины в разных компонентах
                    if set1 != set2:
                        # Обновляем минимальное ребро для компоненты
                        if cheapest[set1] == -1 or adj_matrix[cheapest[set1][0]][cheapest[set1][1]] > adj_matrix[u][v]:
                            cheapest[set1] = [u, v, adj_matrix[u][v]]
                        if cheapest[set2] == -1 or adj_matrix[cheapest[set2][0]][cheapest[set2][1]] > adj_matrix[u][v]:
                            cheapest[set2] = [u, v, adj_matrix[u][v]]

        # Добавляем найденные минимальные рёбра в MST
        for node in range(V):
            if cheapest[node] != -1:
                u, v, w = cheapest[node]
                set1 = find(parent, u)
                set2 = find(parent, v)

                if set1 != set2:
                    mst_weight += w
                    mst_edges.append([u, v, w])
                    union(parent, rank, set1, set2)
                    num_trees -= 1

        # Очищаем массив cheapest для следующей итерации
        cheapest = [-1] * V

    return mst_edges, mst_weight



def PrintMatrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i], sep=' \t')


if __name__ == "__main__":
    Main()
