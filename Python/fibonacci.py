def number(num):
    if num <= 1:
        return num 
    else:
        sum_nums = number(num-1) + number(num-2)
        return sum_nums
 
print(number(6))  
