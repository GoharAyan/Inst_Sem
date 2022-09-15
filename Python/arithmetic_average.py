nums = [1, -8, 2, 10, 6, -3, 4, -12, -15, 5, 6]
sum_nums = 0 
digit = 0 

for i in (nums):
    if i < 0:
        sum_nums = sum_nums + i 
        digit = digit + 1 
    else:
        i = i+1 

result = sum_nums / digit
print(result)
