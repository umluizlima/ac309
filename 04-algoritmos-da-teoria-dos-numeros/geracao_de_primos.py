from teste_de_primalidade import primo_d as primo


def gerador_a(n: int) -> list:
    """Trivial com teste O(sqrt(n)): O(n * primo(n)).

    Exemplos
    --------
    >>> gerador_a(10)
    [2, 3, 5, 7]
    >>> gerador_b(13)
    [2, 3, 5, 7, 11, 13]

    """
    return [i for i in range(2, n+1) if primo(i)]


def gerador_b(n: int) -> list:
    """Crivo de Erastóstenes O(n * log(log(n))).

    Exemplos
    --------
    >>> gerador_a(10)
    [2, 3, 5, 7]
    >>> gerador_b(13)
    [2, 3, 5, 7, 11, 13]

    """
    primos = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if primos[p] is True:
            for i in range(p*2, n+1, p):
                primos[i] = False
        p += 1
    return [i for i in range(2, n+1) if primos[i]]
