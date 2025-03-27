import random
from timer import Timer

# Function to check if the number the user inputted is valid 
def is_power_of_2(n):
    """Check if n is greater than 0 and is a power of 2 
       (n & (n - 1)) == 0 is a bitwise operation 
       Bitwise AND (&) operator performs a bitwise AND between two numbers, comparing the binary of both numbers. 
       For each bit, it results in 1 if both bits are 1, and 0 otherwise. 
       Ex. For n = 8 (binary 1000), n - 1 = 7 (binary 0111), so 8 & 7 equals 0000 (which is 0 and valid). 
       Ex. For n = 6 (binary 0110), n - 1 = 5 (binary 0101), so 6 & 5 equals 0100 (which is not 0 and invalid)."""
    return n > 0 and (n & (n - 1)) == 0

# Function to create an n x n matrix 
def create_matrix(n):
    # Create an n x n matrix initialized with zeros
    return [[0 for i in range(n)] for i in range(n)]

# Function to do Classic matrix multiplication 
def classic_matrix_multiplication(matrixA, matrixB, n): 
    matrixC = create_matrix(n)
    for i in range(n): 
        for j in range(n): 
            # temp variable to hold the value that will be assigned to C[i][j]
            tempVal = 0
            for l in range(n):
                tempVal += matrixA[i][l] * matrixB[l][j]
            matrixC[i][j] = tempVal
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

        # Printing out Matrix A and Matrix B to ensure their size
        # print("Matrix A: ")
        # for row in matrixA:
        #     print(row)
        
        # print("Matrix B: ")
        # for row in matrixB:
        #     print(row)
        
        # Start the timer
        timer.start()

        # Perform matrix multiplication to get Matrix C
        matrixC = classic_matrix_multiplication(matrixA, matrixB, n)

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