"""Implementação do algoritmo Counting Sort.

Exemplos
--------
>>> counting_sort([1, 4, 1, 2, 7, 5, 2])
[1, 1, 2, 2, 4, 5, 7]

"""


def counting_sort(l: list) -> list:
    """Retorna a lista l ordenada: O(n).

    Exemplos
    --------
    >>> counting_sort([102, 85, 94])
    [85, 94, 102]

    """
    # cria uma lista aux de comprimento max(l)+1
    aux = [0] * (max(l)+1)
    # guarda o número de repetições de elementos da lista em aux
    for i in l:
        aux[i] += 1
    # soma cada elemento de aux com seu antecessor
    for i in range(1, len(aux)):
        aux[i] += aux[i-1]
    # preenche a lista res com os elementos de l na ordem correta
    res = [None] * len(l)
    for i in l:
        res[aux[i]-1] = i
        aux[i] -= 1
    return res


if __name__ == "__main__":
    vec = list(map(int, input().split()))
    print(counting_sort(vec))
