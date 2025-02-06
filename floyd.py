n = float('inf')

def Main():
    matrix = DefaultMatrix(7)
    SetEdges(matrix)
    PrintMatrix(matrix)
    Floyd(matrix)
    PrintMatrix(matrix)
    print()

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
    SetEdge(matrix, 1, 2, 4)
    SetEdge(matrix, 1, 4, 5)
    SetEdge(matrix, 2, 4, 9)
    SetEdge(matrix, 2, 5, 3)
    SetEdge(matrix, 3, 2, 8)
    SetEdge(matrix, 3, 7, 11)
    SetEdge(matrix, 4, 3, 6)
    SetEdge(matrix, 4, 6, 7)
    SetEdge(matrix, 5, 3, 9)
    SetEdge(matrix, 5, 4, 10)
    SetEdge(matrix, 5, 7, 4)
    SetEdge(matrix, 6, 1, 6)
    SetEdge(matrix, 6, 2, 2)
    SetEdge(matrix, 6, 5, 5)
    SetEdge(matrix, 6, 7, 3)
    SetEdge(matrix, 7, 2, 8)
    SetEdge(matrix, 7, 4, 6)

def SetEdge(matrix, start, end, weight):
    matrix[start-1][end-1] = weight

def Floyd(matrix):
    v = len(matrix)
    for n in range(v):
        for row in range(v):
            for column in range(v):
                matrix[row][column] = min(matrix[row][column], matrix[row][n] + matrix[n][column])

def PrintMatrix(matrix):
    print()
    for i in range(len(matrix)):
        print(*matrix[i], sep='\t')


if __name__ == "__main__":
    Main()
