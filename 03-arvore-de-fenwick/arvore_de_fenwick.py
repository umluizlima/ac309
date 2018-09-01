"""Árvore de indexação binária.

Exemplos
--------
>>> freq = [3, 2, -1, 6, 5, 4, -3]
>>> t = Fenwick(freq)
>>> t.soma(4)
15
>>> t.soma(2)
4
>>> t.soma(5)
19

"""


class Fenwick:
    """Implementação da árvore de Fenwick.

    Aplicada normalmente em compressões aritméticas, é
    composta de três operações:
    - Construção:
        Cria uma árvore a partir de um vetor.
    - Atualiza:
        Atualiza um nó da árvore no índice.
    - Soma:
        Retorna a soma cumulativa dos elementos até o índice.

    """

    def __init__(self, arr: list):
        """Inicializa a árvore a partir de um vetor.

        Exemplos
        --------
        >>> freq = [3, 2, -1, 6, 5, 4, -3]
        >>> Fenwick(freq)
        Fenwick([3, 2, -1, 6, 5, 4, -3])

        """
        self.arr = arr
        self.n = len(self.arr)
        self.tree = [0] * (self.n+1)
        for i in range(self.n):
            self._atualiza(i, arr[i])

    def __repr__(self):
        """Representação de uma instância.

        Exemplos
        --------
        >>> freq = [3, 2, -1, 6, 5, 4, -3]
        >>> t = Fenwick(freq)
        >>> t
        Fenwick([3, 2, -1, 6, 5, 4, -3])

        """
        return f"Fenwick({self.arr})"

    def _atualiza(self, i: int, v: int):
        i += 1
        while i <= self.n:
            self.tree[i] += v
            i += i & (-i)

    def soma(self, i: int):
        """Retorna a soma cumulativa até o índice i.

        Exemplos
        --------
        >>> freq = [3, 2, -1, 6, 5, 4, -3]
        >>> t = Fenwick(freq)
        >>> t.soma(4)
        15

        """
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
