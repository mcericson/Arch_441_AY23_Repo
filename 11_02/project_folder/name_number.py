def numbered_name(number, name, padding):
    num = str(number) 
    num_pad = num.zfill(padding)
    file_name = num_pad + "_" + name
    return file_name

for i in range(10):
    name = numbered_name( i, 'test',3)
    print(name)
