from math import sqrt


def primo_a(n: int):
    """Complexidade O(n).

    Exemplos
    --------
    >>> primo_a(7)
    True
    >>> primo_a(25)
    False

    """
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primo_b(n: int):
    """Complexidade O(n/2).

    Exemplos
    --------
    >>> primo_b(7)
    True
    >>> primo_b(25)
    False

    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True


def primo_c(n: int):
    """Complexidade O(n/4).

    Exemplos
    --------
    >>> primo_c(7)
    True
    >>> primo_c(25)
    False

    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n//2, 2):
        if n % i == 0:
            return False
    return True


def primo_d(n: int):
    """Complexidade O(sqrt(n)).

    Exemplos
    --------
    >>> primo_a(7)
    True
    >>> primo_a(25)
    False

    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, round(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True
