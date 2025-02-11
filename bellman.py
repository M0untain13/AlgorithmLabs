n = float('inf')

def Main():
    matrix = DefaultMatrix(7)
    SetEdges(matrix)
    PrintMatrix(matrix)
    d = Bellman(matrix, 0, 6)
    print(f'\n{d}\n')

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
    SetEdge(matrix, 0, 1, -3)
    SetEdge(matrix, 0, 2, -1)
    SetEdge(matrix, 0, 5, 5)
    SetEdge(matrix, 1, 2, -2)
    SetEdge(matrix, 1, 3, 5)
    SetEdge(matrix, 1, 6, 4)
    SetEdge(matrix, 2, 1, 3)
    SetEdge(matrix, 2, 4, 7)
    SetEdge(matrix, 2, 5, -4)
    SetEdge(matrix, 3, 4, 7)
    SetEdge(matrix, 3, 6, -2)
    SetEdge(matrix, 4, 0, 4)
    SetEdge(matrix, 4, 3, -4)
    SetEdge(matrix, 4, 5, 2)
    SetEdge(matrix, 5, 6, 8)
    SetEdge(matrix, 6, 0, 1)

def SetEdge(matrix, start, end, weight):
    matrix[start][end] = weight

def Bellman(matrix, start, end):
    n, inf = len(matrix), float("inf")
    v = range(n)
    dist = [inf for _ in v]
    dist[start] = 0
    for i in range(n):
        for row in v:
            for column in v:
                w = matrix[row][column]
                # Если растояние через один узел до другого меньше, чем напрямую
                if dist[row] != inf and dist[row] + w < dist[column]:
                    # И если это не последний шаг внешнего цикла
                    if i != n - 1:
                        dist[column] = dist[row] + w
                    else:
                        return "Граф содержит цикл отрицательных весов!"

    return dist[end]

def PrintMatrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i], sep='\t')


if __name__ == "__main__":
    Main()
