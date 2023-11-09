def chunk_list(items, size):
    return [items[i:i + size] for i in range(0 ,len(items), size)]

list = [1,2,3,4,5,6,7,8]

new_list = (chunk_list(list, 2))

print new_list


