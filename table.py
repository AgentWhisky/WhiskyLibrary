# i = rows
# j = columns


class Table:
    def __init__(self, rows=1, cols=1):
        # Default rows and cols >= 1
        rows = max(1, rows)
        cols = max(1, cols)
        self._table = [[0] * rows for _ in range(cols)]


    def numRows(self):
        return len(self._table)

    def numCols(self):
        return len(self._table[0])

    def set(self, index, val):
        self._table[index[0]][index[1]] = val

    def get(self, index):
        return self._table[index[0]][index[1]]

    def reset(self, index):
        self._table[index[0]][index[1]] = 0

    def printTable(self):
        for j in self._table:
            print(j)

