def mat_mul(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result