def multi_num(arg):
 
    result = 1 
    result_after = 1 

    while (arg != 0): 
        result = result * (arg % 10) 
        arg = arg // 10
 
 
    while (result != 0): 
        result_after = result_after * (result % 10) 
        result = result // 10
    
    return result_after

print(multi_num(1234))
