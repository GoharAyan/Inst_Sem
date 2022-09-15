a = 0 
for i in range(100):
    if (i % 2) == 0:
        i += 1
    else:
        print(i)
        a += 1
    if (a == 20):
        break
