def mdc_a(a: int, b: int) -> int:
    """Trivial O(min(a, b)).

    Exemplos
    --------
    >>> mdc_a(1071, 462)
    21
    >>> mdc_a(8, 12)
    4

    """
    return max([
        i for i in range(1, min(a, b)+1)
        if (a % i == 0) and (b % i == 0)
    ])


def mdc_b(a: int, b: int) -> int:
    """Algoritmo de Euclides O(log(min(a, b))).

    Exemplos
    --------
    >>> mdc_b(1071, 462)
    21
    >>> mdc_b(8, 12)
    4

    """
    return a if b == 0 else mdc_b(b, a % b)
