def mat_mul(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for k in range(len(Y)):
            if X[i][k]:
                for j in range(len(Y[0])):
                    result[i][j] += X[i][k] * Y[k][j]
    return result