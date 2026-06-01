def matrix_addition():
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[5,6,7],[9,8,7],[4,5,6]]

    result = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]

        print("Resultant Matrix:")
        for row in result:
            print(row)

    matrix_addition()