def exp_a(x: int, n: int) -> int:
    """Trivial O(n).

    Exemplos
    --------
    >>> exp_a(2, 10)
    1024

    """
    res = x
    for _ in range(1, n):
        res *= x
    return res


def exp_b(x: int, n: int) -> int:
    """Por quadratura O((n * log(x))^k).

    Exemplos
    --------
    >>> exp_b(2, 10)
    1024

    """
    if n < 0:
        return exp_b(1/x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_b(x*x, n/2)
    else:
        return x * exp_b(x*x, (n-1)/2)
