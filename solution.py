def diagonal_difference(input_square_matrix):
    # Initializing the left to right diagonal summation
    l_r_diag_summation = 0
    # Initializing the right to left diagonal summation
    r_l_diag_summation = 0
    matrix_row_size = len(input_square_matrix)
    
    # The diagonal elements are summed together by iterating through
    # the matrix elements which correspond to the digonal element positions [][]

    for item in range(0, matrix_row_size):
        l_r_diag_summation = l_r_diag_summation + input_square_matrix[item][item]
        r_l_diag_summation = r_l_diag_summation + input_square_matrix[item][matrix_row_size - item - 1]
    # The abs() function return the absolute value of a given number
    abs_diff = abs(l_r_diag_summation - r_l_diag_summation)
    return abs_diff

if __name__=="__main__":
    input_square_matrix = [ [1, 2, 3],
                            [4, 5, 6],
                            [9, 8, 9]]

    print(diagonal_difference(input_square_matrix))