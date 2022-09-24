def list_tuple(lis, tup):

    result = lis 
    for i in tup[:]:
        if i not in result:
            result.append(i)
        else:
            result.remove(i)

    return sum(result)

lis = [1, 2, 3, 4, 6]
tup = (1, 2, 3, 9, 10) 

print(list_tuple(lis, tup))

