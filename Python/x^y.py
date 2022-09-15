first_num = int(input("First number: "))
second_num = int(input("Second number: "))

result = 1 

while second_num != 0:
    result = result * first_num
    second_num = second_num - 1 
    
print("Answer: ", str(result))
