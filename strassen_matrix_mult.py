import random
from timer import Timer

# Function to check if the number the user inputted is valid 
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Function to create an n x n matrix 
def create_matrix(n):
    return [[0 for i in range(n)] for i in range(n)]

# Function to do Strassen matrix multiplication 
def strassen_matrix_mult(matrixA, matrixB): 
    n = len(matrixA) 
    matrixC = create_matrix(n) 
    
    # Base case: If the matrix size is 1x1, multiply 
    if n == 1: 
        matrixC[0][0] = matrixA[0][0] * matrixB[0][0] 
        return matrixC 
    
    # Step 1a: Divide Matrix A into 4 submatrices: A11, A12, A21, A22 
    A11, A12, A21, A22 = divide_matrix(matrixA) 
    
    # Step 1b: Divide Matrix B into 4 submatrices: B11, B12, B21, B22 
    B11, B12, B21, B22 = divide_matrix(matrixB) 
    
    # Step 2: Calculate using Strassen’s method 
    S1 = sub_matrices(B12, B22) 
    S2 = add_matrices(A11, A12) 
    S3 = add_matrices(A21, A22) 
    S4 = sub_matrices(B21, B11) 
    S5 = add_matrices(A11, A22) 
    S6 = add_matrices(B11, B22)
    S7 = sub_matrices(A12, A22) 
    S8 = add_matrices(B21, B22) 
    S9 = sub_matrices(A11, A21) 
    S10 = add_matrices(B11, B12) 

    P1 = strassen_matrix_mult(A11, S1) 
    P2 = strassen_matrix_mult(S2, B22) 
    P3 = strassen_matrix_mult(S3, B11) 
    P4 = strassen_matrix_mult(A22, S4) 
    P5 = strassen_matrix_mult(S5, S6) 
    P6 = strassen_matrix_mult(S7 , S8) 
    P7 = strassen_matrix_mult(S9, S10) 

    # Step 3: Compute the submatrices of the result matrixC
    matrixC11 = add_matrices(sub_matrices(add_matrices(P5, P4), P2), P6)
    matrixC12 = add_matrices(P1, P2)
    matrixC21 = add_matrices(P3, P4) 
    matrixC22 = sub_matrices(sub_matrices(add_matrices(P5, P1), P3), P7)

	# Step 4: Combine the results into the final matrix C 
    matrixC = combine_matrices(matrixC11, matrixC12, matrixC21, matrixC22) 
    
    return matrixC

# Helper function to divide a matrix into 4 submatrices
def divide_matrix(matrix): 
    n = len(matrix) 
    mid = n // 2 # Middle index, since n = 2^k 
    
    # Dividing the matrix into 4 submatrices 
    matrix11 = [] # Create top-left submatrix 
    for i in range(mid): 
        row = [] 
        for j in range(mid): 
            row.append(matrix[i][j]) 
        matrix11.append(row) 

    matrix12 = [] # Create top-right submatrix
    for i in range(mid): 
        row = [] 
        for j in range(mid, len(matrix[i])): 
            row.append(matrix[i][j]) 
        matrix12.append(row) 
    
    matrix21 = [] # Create bottom-left submatrix 
    for i in range(mid, len(matrix)): 
        row = [] 
        for j in range(mid): 
            row.append(matrix[i][j]) 
        matrix21.append(row) 

    matrix22 = [] # Create bottom-right submatrix 
    for i in range(mid, len(matrix)): 
        row = [] 
        for j in range(mid, len(matrix[i])): 
            row.append(matrix[i][j]) 
        matrix22.append(row) 

    return matrix11, matrix12, matrix21, matrix22 

# Function to add two matrices
def add_matrices(matrixA, matrixB):
    n = len(matrixA)
    result = []  # An empty list to store the result
    
    for i in range(n): # Loop over rows
        row = []  # Create a new row for each row in the result matrix
        for j in range(n):  # Loop over columns
            row.append(matrixA[i][j] + matrixB[i][j])  # Add the corresponding elements from matrixA and matrixB
        result.append(row)  # Append the row to the result matrix
    
    return result

# Function to subtract matrices
def sub_matrices(matrixA, matrixB):
    n = len(matrixA)
    result = []  # An empty list to store the result
    
    for i in range(n): # Loop over rows
        row = []  # Create a new row for each row in the result matrix
        for j in range(n):  # Loop over columns
            row.append(matrixA[i][j] - matrixB[i][j])  # Add the corresponding elements from matrixA and matrixB
        result.append(row)  # Append the row to the result matrix
    
    return result

# Helper function to combine the 4 submatrices into one result matrix
def combine_matrices(matrixC11, matrixC12, matrixC21, matrixC22): 
    n = len(matrixC11) 
    matrixC = create_matrix(n * 2)

	# Combine submatrices into a single matrixC 
    for i in range(n): 
        for j in range(n): 
            matrixC[i][j] = matrixC11[i][j] 
            matrixC[i][j + n] = matrixC12[i][j] 
            matrixC[i + n][j] = matrixC21[i][j] 
            matrixC[i + n][j + n] = matrixC22[i][j] 
    
    return matrixC

# Create an instance of the Timer
timer = Timer()

print("Let the matrix size be n x n.")

# boolean to control the Main Loop 
testing_n = True 

# Start of the main loop
while testing_n:
    # Get the user input for n
    n = int(input("Give n as a power of 2 where 2^k = n: "))

    # Check if the input is a valid power of 2
    if is_power_of_2(n):
        # Create Matrix A and Matrix B that will be multiplied to get Matrix C
        matrixA = create_matrix(n)
        for i in range(len(matrixA)):
            for j in range(len(matrixA)): 
                matrixA[i][j] = random.randint(0, 10)

        matrixB = create_matrix(n)
        for i in range(len(matrixB)):
            for j in range(len(matrixB)): 
                matrixB[i][j] = random.randint(0, 10) 

        # Test cases: 
        # matrixA=[[1]] 
        # matrixB=[[2]]  

        # matrixA=[[10, 5], [1, 3]] 
        # matrixB=[[2, 1], [10, 10]]

        # matrixA=[[2, 5, 2, 3], [2, 0, 6, 3], [3, 8, 4, 3], [5, 9, 4, 1]] 
        # matrixB=[[10, 3, 7, 0], [9, 9, 1, 10], [4, 2, 4, 10], [10, 9, 0, 2]]

        # matrixA=[[8, 10, 3, 2, 6, 6, 6, 2], [3, 6, 7, 8, 5, 8, 8, 9], [0, 1, 10, 1, 8, 4, 3, 9], [0, 3, 1, 1, 7, 8, 3, 6], 
        #          [3, 0, 6, 4, 8, 6, 3, 8], [8, 1, 6, 0, 0, 2, 3, 4], [4, 7, 6, 2, 0, 9, 7, 10], [10, 3, 4, 7, 7, 7, 5, 0]] 
        # matrixB=[[2, 8, 0, 5, 8, 4, 5, 10], [5, 6, 10, 6, 5, 8, 3, 1], [10, 3, 1, 10, 5, 10, 10, 10], [10, 10, 2, 6, 5, 6, 2, 0], 
        #          [3, 1, 0, 2, 6, 3, 2, 4], [8, 9, 3, 4, 8, 9, 6, 1], [3, 7, 3, 4, 4, 3, 10, 8], [0, 7, 5, 5, 1, 10, 8, 7]] 

        # matrixA=[[3, 9, 7, 1, 7, 10, 7, 4, 6, 10, 0, 10, 5, 10, 6, 5], 
        #          [5, 1, 7, 5, 0, 1, 0, 6, 10, 0, 2, 4, 8, 7, 5, 4], 
        #          [1, 0, 0, 0, 7, 6, 10, 10, 10, 0, 10, 4, 6, 6, 9, 6], 
        #          [5, 6, 0, 2, 0, 5, 3, 2, 8, 5, 3, 1, 4, 7, 2, 4], 
        #          [7, 0, 6, 5, 6, 5, 1, 4, 9, 5, 7, 2, 1, 10, 6, 7], 
        #          [8, 10, 7, 8, 2, 3, 9, 8, 2, 2, 5, 3, 7, 3, 2, 4], 
        #          [3, 7, 4, 4, 10, 10, 1, 6, 9, 1, 4, 2, 8, 8, 7, 6], 
        #          [7, 6, 9, 7, 4, 1, 9, 2, 0, 0, 6, 3, 0, 4, 8, 7], 
        #          [6, 5, 2, 8, 7, 1, 8, 1, 10, 8, 1, 7, 4, 7, 0, 3], 
        #          [10, 6, 2, 2, 4, 0, 8, 2, 3, 6, 1, 4, 9, 4, 6, 4], 
        #          [7, 5, 10, 9, 6, 5, 2, 0, 5, 8, 7, 4, 3, 5, 0, 8], 
        #          [2, 5, 4, 1, 2, 7, 9, 10, 3, 10, 10, 4, 5, 6, 10, 1], 
        #          [9, 1, 7, 7, 0, 3, 8, 5, 8, 10, 2, 4, 7, 1, 8, 7], 
        #          [8, 6, 3, 4, 7, 4, 3, 7, 9, 4, 8, 6, 5, 3, 0, 2], 
        #          [6, 8, 3, 1, 9, 5, 4, 9, 9, 0, 10, 3, 0, 3, 7, 6], 
        #          [4, 7, 0, 0, 3, 7, 2, 7, 3, 8, 2, 6, 4, 7, 3, 2]] 
        # matrixB=[[9, 2, 5, 2, 6, 8, 5, 5, 3, 5, 5, 3, 7, 8, 3, 3], 
        #          [2, 4, 7, 1, 6, 10, 3, 1, 2, 6, 2, 9, 0, 7, 9, 3], 
        #          [6, 4, 1, 10, 0, 10, 7, 1, 8, 2, 4, 7, 10, 1, 0, 0], 
        #          [9, 3, 5, 6, 7, 1, 8, 8, 6, 2, 0, 8, 9, 6, 6, 4], 
        #          [6, 0, 7, 1, 9, 4, 0, 6, 8, 3, 3, 0, 2, 10, 1, 3], 
        #          [10, 7, 0, 9, 0, 2, 10, 10, 4, 10, 8, 9, 9, 5, 9, 1], 
        #          [7, 7, 5, 0, 3, 10, 2, 3, 0, 9, 2, 0, 1, 6, 3, 1], 
        #          [2, 4, 3, 9, 0, 6, 7, 10, 10, 5, 7, 10, 3, 5, 7, 6], 
        #          [2, 3, 8, 8, 2, 5, 5, 3, 0, 6, 2, 5, 8, 7, 7, 5], 
        #          [5, 5, 1, 7, 1, 7, 9, 9, 10, 4, 1, 7, 4, 7, 9, 0], 
        #          [5, 4, 1, 6, 5, 3, 5, 7, 5, 4, 3, 1, 2, 2, 7, 9], 
        #          [9, 4, 6, 9, 3, 0, 1, 3, 4, 10, 10, 8, 3, 0, 0, 0], 
        #          [0, 1, 2, 10, 4, 2, 7, 10, 2, 8, 2, 6, 3, 4, 9, 7], 
        #          [0, 0, 9, 6, 8, 2, 4, 5, 10, 2, 3, 7, 7, 4, 7, 2], 
        #          [0, 7, 6, 5, 9, 6, 7, 4, 0, 4, 5, 10, 7, 9, 8, 7], 
        #          [5, 6, 9, 9, 0, 6, 8, 8, 7, 1, 5, 6, 9, 7, 5, 9]]

        # matrixA=[[8, 0, 2, 10, 8, 9, 10, 2], [9, 0, 9, 4, 7, 2, 0, 7], [2, 6, 5, 8, 1, 2, 2, 0], [6, 6, 1, 5, 9, 2, 10, 5], 
        #          [8, 5, 4, 1, 0, 2, 6, 4], [1, 2, 3, 9, 0, 6, 4, 3], [0, 9, 3, 10, 5, 9, 4, 4], [3, 6, 9, 7, 2, 10, 8, 7]] 
        # matrixB=[[6, 4, 10, 2, 2, 1, 9, 10], [9, 1, 1, 6, 0, 0, 1, 1], [4, 10, 7, 3, 4, 1, 2, 5], [1, 3, 6, 10, 1, 7, 2, 3], 
        #          [1, 9, 3, 6, 9, 8, 7, 5], [8, 1, 9, 4, 7, 8, 4, 3], [2, 7, 10, 7, 3, 10, 9, 7], [10, 0, 3, 0, 3, 1, 2, 1]]

        # matrixA=[[6, 10, 2, 9], [2, 10, 1, 1], [9, 9, 8, 2], [5, 1, 2, 10]] 
        # matrixB=[[8, 8, 7, 10], [6, 7, 3, 3], [8, 8, 1, 5], [0, 0, 7, 8]]

        # matrixA=[[6, 3], [2, 4]] 
        # matrixB=[[3, 3], [0, 6]]

        # matrixA=[[6]] 
        # matrixB=[[4]] 
        
        # matrixA=[[9, 4, 8, 7], [9, 1, 5, 2], [9, 8, 8, 7], [3, 5, 2, 0]] 
        # matrixB=[[0, 6, 3, 9], [7, 2, 8, 3], [6, 9, 8, 9], [10, 6, 0, 10]] 

        # # Printing out Matrix A and Matrix B to ensure their size
        # print("Matrix A: ")
        # for row in matrixA:
        #     print(row)
        
        # print("Matrix B: ")
        # for row in matrixB:
        #     print(row)

        # Start the timer
        timer.start()

        # Perform matrix multiplication to get Matrix C
        matrixC = strassen_matrix_mult(matrixA, matrixB)

        # Stop the timer and print the elapsed time 
        timer.stop()

        # print("Matrix C: ")
        # for row in matrixC:
        #     print(row)
        
        tryMoreValues = input("Continue trying values of n (yes or no)? ") 
        if tryMoreValues.lower() == "no" or tryMoreValues.lower() == "n": 
            testing_n = False
    else:
        print("Not a valid value of n, try again.")