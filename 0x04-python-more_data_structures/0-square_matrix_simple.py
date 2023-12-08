<<<<<<< HEAD
#!/usr/bin/python3
def square_matrix_simple(matrix=None):
=======
quare_matrix_simple(matrix=None):
>>>>>>> c065d8bd456b6475a876a0882686e02710b80099
    if matrix is None:
        matrix = []
    changed_matrix = [row[:] for row in matrix]
    for row in range(len(changed_matrix)):
        changed_matrix[row] = list(map(lambda item: item ** 2,
                                   changed_matrix[row]))
    return changed_matrix
