def sum_list_num(num):
    sum_num = 0 
    for i in num:
        sum_num = sum_num + i 
            
    if (sum_num < 0): 
        sum_num = (-1) * sum_num   
            
    return sum_num

num = [1, 2, 3, -8] 
print(sum_list_num(num)) 
