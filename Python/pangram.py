def pangram(string):
    a_z = 'abcdefghijklmnopqrstuvwxyz'
    flag = 0 
    for i in a_z:
        if i not in string:
            flag = 1 
    if flag == 1:
        return ("This is not a pangram text")
    else:
        return ("This is a pangram text")

print(pangram("The quick brown fox jumps over the lazy dog"))
