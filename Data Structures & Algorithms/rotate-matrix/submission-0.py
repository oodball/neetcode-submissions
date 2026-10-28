class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                #swap function, can make cleaner later
                saved = matrix[i][j]
                matrix[i][j] =  matrix[j][i]
                matrix[j][i] = saved

        # reverse in place
        for i in range(len(matrix)):
            k = 0
            j = len(matrix[i]) - 1

            print(matrix[i], matrix[i][k], matrix[i][j])

            while k < j:
                matrix[i][k], matrix[i][j] = matrix[i][j], matrix[i][k]
                k += 1
                j -= 1
                print(matrix[i], matrix[i][k], matrix[i][j])
            