#list operation examples
#https://docs.python.org/3/tutorial/datastructures.html

list_a = [x for x in range(1,11,1)]

print list_a

list_b = list_a[int(len(list_a)/2):]

print list_b

index = list_a.index(5)

print index

list_a.pop(index)

print list_a

list_a.remove(4)

print list_a

list_a.insert(3,4)
list_a.insert(4,5)

print list_a

list_a.reverse()

print list_a

list_a.sort()

print list_a

lists = [list_a[i:i+1] for i in list_a]

print  lists

size = 2
sized_lists = [list_a[i:i + size] for i in list_a]

print sized_lists


