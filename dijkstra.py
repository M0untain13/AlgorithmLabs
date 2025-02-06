import heapq

def FindPathWithMinLength(graph, start, end):
    start -= 1
    end -= 1
    n = len(graph)
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    visited = {i: False for i in range(n)}

    for _ in range(n):
        # Находим вершину с минимальным расстоянием
        min_distance = float('inf')
        min_index = -1
        for v in range(n):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        # Помечаем выбранную вершину как посещенную
        visited[min_index] = True

        # Обновляем расстояния до соседних вершин
        for v in range(n):
            if graph[min_index][v] > 0 and not visited[v]:  # Если есть ребро и вершина не посещена
                new_distance = distances[min_index] + graph[min_index][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    return distances[end]


if __name__ == "__main__":
    n = float('inf')
    matrix = [
        [0, 5, n, 6, n, n, 19, 3, n],
        [n, 0, 5, n, 4, n, n,  3, n],
        [n, n, 0, n, n, n, 2,  n, n],
        [n, n, n, 0, 1, n, n,  n, 6],
        [n, n, n, n, 0, 9, 6,  n, n],
        [4, n, n, n, n, 0, 4,  n, n],
        [n, n, n, n, n, n, 0,  4, 1],
        [n, n, n, n, 4, n, n,  0, n],
        [n, n, n, n, n, n, n,  n, 0]
    ]
    d = FindPathWithMinLength(matrix, 1, 7)
    print(f"length: {d}.")