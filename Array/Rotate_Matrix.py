def rotateMatrix(matrix, N):

	for i in range(0, N // 2):

		j = i

    	for j in range(j, N - i - 1):
    
            temp = matrix[i][j]

            matrix[i][j] = matrix[N - 1 - j][i]
            matrix[N - 1 - j][i] = matrix[N - 1 - i][N - 1 - j] 
            matrix[N - 1 - i][N - 1 - j] = matrix[j][N - 1 - i]
            matrix[j][N - 1 - i] = temp

    return matrix