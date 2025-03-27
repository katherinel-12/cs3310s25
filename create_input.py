def create_input_file():
    filename = "n_input.txt"
    
    # Open the file in write mode
    with open(filename, 'w') as file:
        # Write the numbers from 0 to 9 with newlines
        for i in range(10):
            file.write(str(i) + "\n")
    
    print(f"File '{filename}' created successfully.")

create_input_file()

# # Read the value of n from the file
# def read_n_from_file(filename="n_input.txt"):
#     try:
#         with open(filename, 'r') as file:
#             n = int(file.read().strip())  # Read and convert to integer
#             return n
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#         return None
#     except ValueError:
#         print("Error: The file content is not a valid integer.")
#         return None

# def write_matrix_to_file(matrixC, filename):
#     with open(filename, 'w') as file:
#         file.write("Matrix C \n")
#         for row in matrixC:
#             # Write each row on a new line
#             file.write(' '.join(map(str, row)) + '\n')  
#     print(f"Matrix C has been written to '{filename}'.")