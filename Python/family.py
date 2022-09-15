family = int(input("Number_of_family: "))

fmly_dict = {}

for i in range(family):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    fmly_dict[name] = age 

child = 0 
teenager = 0 
young = 0 
adult = 0 

print(fmly_dict, "\n")

for age in (fmly_dict.values()):
    if age <= 8:
        child = age 
        print("Child:", child)
    if age >= 9 and age <= 17: 
        teenager = age 
        print("Teenager:", teenager)
    if age >= 18 and age <= 30: 
        young = age 
        print("Young", young)
    if age >= 30 and age <= 60: 
        adult = age 
        print("Adult:", adult)
