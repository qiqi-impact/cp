import numpy as np
import matplotlib.pyplot as plt
 
def f(x, data):
    return np.sum(np.linalg.norm(data-x, axis=1))
 
def df(x, data):
    num = x-data
    den = np.maximum(np.linalg.norm(data-x, axis=1).reshape([-1,1]),1e-8)
    return np.sum(num/den, axis=0)
 
def gradient_descent(s, data, n_it):
    curr = s
    a = 0.3
    b = 0.7
    its = [s.copy()]
    for it in range(n_it):
        df0 = -df(curr, data)
        ndf0 = np.linalg.norm(df0)
        ndf0sq = ndf0**2
        f0 = f(curr, data)
        t = 1.0
        while f(curr+t*df0,data) > f0 - a*t*ndf0sq:
            t *= b
        curr += t*df0
        its.append(curr.copy())
        it += 1
    return its
 
def main():
    N = 1000
    n_it = 10
    data = 100*np.random.rand(N,2) + 100*np.random.rand(1,2)
    s = np.array([0.0,0.0])
    its = gradient_descent(s,data,n_it)
    plt.scatter(data[:,0],data[:,1],c='b')
    plt.plot([p[0] for p in its], [p[1] for p in its],marker='o',c='r',markerfacecolor='k')
    plt.title(f'Solution: {its[-1]}')
    plt.show()

if __name__ == '__main__':
    main()