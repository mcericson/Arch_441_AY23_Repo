def chunk_list(items, size):
    return [items[i:i + size] for i in range(0 ,len(items), size)]

def flip_matrix(matrix):
    return [ for list() in zip(*matrix)]

list = [1,2,3,4,5,6,7,8]

new_list = (chunk_list(list, 2))
nl = flip_matrix(new_list)
print new_list
print (nl)

