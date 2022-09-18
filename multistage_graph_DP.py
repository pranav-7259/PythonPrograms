def calculate_optimal_path(A):
    n = 6
    cost = [0] * len(A)
    d = [0] * len(A)
    n_stages = 4
    path = [0]*(n_stages + 1)

    cost[n] = 0

    for i in range(n - 1, 0, -1):
        minimum = 3456789
        for k in range(i + 1, n + 1, 1):
            if A[i][k] != 0 and A[i][k] + cost[k] < minimum:
                minimum = A[i][k] + cost[k]
                d[i] = k
        cost[i] = minimum

    path[n_stages] = n
    path[1] = 1

    for i in range(2,n_stages):
        path[i] = d[path[i-1]]

    return path[1:]




if __name__ == '__main__':
    A = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 2, 4, 0, 0, 0],
         [0, 0, 0, 0, 7, 5, 0],
         [0, 0, 0, 0, 6, 3, 0],
         [0, 0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]
    print(calculate_optimal_path(A))
