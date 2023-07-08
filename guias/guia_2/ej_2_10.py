def fichas_domino(n):
    for i in range(0, n + 1):
        for j in range(i, n + 1):
            print(i, j)
fichas_domino(60)