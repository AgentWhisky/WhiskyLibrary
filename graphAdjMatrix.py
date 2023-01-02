class GraphAdjMatrix:
    # Constructor
    def __init__(self, n):
        self.size = n
        self.matrix = [[None] * n for _ in range(n)]

    # Return Graph Size
    def getSize(self):
        return self.size

    # Add an edge with given weight from a to b
    def addEdge(self, a, b, weight):
        self.matrix[a][b] = weight

    def removeEdge(self, a, b):
        self.matrix[a][b] = None

    # Get the weight for the edge between a and b or None if no edge exists
    def getEdge(self, a, b):
        return self.matrix[a][b]

    # Return if a and b have an edge
    def hasEdge(self, a, b):
        return bool(self.matrix[a][b])

    # Matrix ToString
    def __str__(self):
        s = ''
        for i in range(self.size):
            s += str(self.matrix[i]) + '\n'
        return s
