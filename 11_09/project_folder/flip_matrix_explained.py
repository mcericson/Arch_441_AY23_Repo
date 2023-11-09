
matrix = [[0,1,2,4,5],
          [6,7,8,9,10]]

print (matrix)
print (*matrix)


a = list(zip(*matrix[::-1]))
print (a)


flipped_matrix = []
for i in a:
    flipped_matrix.append(list(i))

print (flipped_matrix)
    
    
def flip_matrix(matrix):
    n_list_a = list(zip(*matrix[::-1]))
    n_list_b= []
    for i in n_list_a:
        n_list_b.append(list(i))
    return(n_list_b)





