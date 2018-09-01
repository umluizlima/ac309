"""Implementação do algoritmo de Coeficiente binomial.

Exemplos
--------
>>> c(2, 1)
2
>>> c(4, 2)
6
>>> c(5, 2)
10

"""


def c(n: int, k: int):
    """Coeficiente binomial.

    Exemplos
    --------
    >>> [c(2, i) for i in range(3)]
    [1, 2, 1]

    """
    if k == 0 or n == k:
        return 1
    else:
        return c(n-1, k-1) + c(n-1, k)


def cc(n: int, k: int):
    """Coeficiente binomial com cache bottom up.

    Exemplos
    --------
    >>> [cc(2, i) for i in range(3)]
    [1, 2, 1]

    """
    cache = [[False] * (k+1)] * (n+1)
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                cache[i][j] = 1
            else:
                cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
    return cache[n][k]
