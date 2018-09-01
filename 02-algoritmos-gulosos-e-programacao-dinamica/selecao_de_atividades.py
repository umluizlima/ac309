"""Algoritmo de Seleção de atividades (guloso).

Exemplos
--------
>>> atividades = [(10, 20), (12, 25), (20, 30)]
>>> selecao_de_atividades(atividades)
[(10, 20), (20, 30)]

"""


def ordena_por_sub_indice(iteravel: list, indice: int) -> list:
    """Ordena uma lista baseado em um subíndice.

    Exemplos
    --------
    >>> iteravel = [(0, 6), (3, 4), (1, 2), (5, 9), (5, 7), (8, 9)]
    >>> ordena_por_sub_indice(iteravel, 0)
    [(0, 6), (1, 2), (3, 4), (5, 9), (5, 7), (8, 9)]
    >>> ordena_por_sub_indice(iteravel, 1)
    [(1, 2), (3, 4), (0, 6), (5, 7), (5, 9), (8, 9)]

    """
    return sorted(iteravel, key=lambda x: x[indice])


def selecao_de_atividades(atividades: list) -> list:
    """Seleciona a melhor combinação de atividades não sobrepostas.

    Parâmetros
    ----------
    atividades: [(começo, fim), (começo, fim), ...]

    Exemplos
    --------
    >>> atividades = [(0, 6), (3, 4), (1, 2), (5, 9), (5, 7), (8, 9)]
    >>> selecao_de_atividades(atividades)
    [(1, 2), (3, 4), (5, 7), (8, 9)]

    """
    atividades = ordena_por_sub_indice(atividades, 1)
    res = [atividades.pop(0)]
    for atividade in atividades:
        if atividade[0] >= res[-1][1]:
            res.append(atividade)
    return res


if __name__ == "__main__":
    n = int(input("Número de atividades: "))
    print(f"Entre com {n} atividades no formato: começo fim")
    atividades = [
        tuple(map(int, input().split()))
        for i in range(n)
    ]
    print(selecao_de_atividades(atividades))
