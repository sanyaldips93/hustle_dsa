class Solution:

    def shortest_distance(self, matrix):

        # Code here

        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
                if i == j:
                    matrix[i][j] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k]
                            + matrix[k][j])

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1

print(Solution().shortest_distance([[0, 1, 43],[1, 0, 6], [-1, -1, 0]]))