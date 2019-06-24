class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def len(self):
        l = 0
        for i in matrix:
            l += len(matrix[i])
        return l
