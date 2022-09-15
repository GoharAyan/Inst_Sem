string = input("Str: ")
lowercase = [chr(id_) for id_ in range(65, 91)]
uppercase = [chr(id_) for id_ in range(97, 123)]
low_upp = lowercase + uppercase

for letter in string:
    if letter in low_upp:
        print(letter)
    else:
        print("Invalid", letter)
        break
