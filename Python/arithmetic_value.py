def numbers(*args):
    sum_args = sum(args)
    result = sum_args / len(args)
    return result

print(numbers(1, 2, 3, 4, 5, 6, 7, 8))  
