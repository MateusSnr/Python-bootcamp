#numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#squared_numbers = [num * num for num in numbers]

#print(squared_numbers)

#-------------------------------------------------------

#list_of_strings = input().split(',')

#numbers = [int(x) for x in list_of_strings]

#result = [num for num in numbers if num%2 == 0]

#print(result)

#------------------------------------------------------

#numbers =[1, 2, 3]

#new_numbers = [num+1 for num in numbers]
#print(new_numbers)

#-----------------------------------------------------

#name = "Angela"

#letters_list = [letter for letter in name]
#print(letters_list)

#-----------------------------------------------------

#range_list = [num*2 for num in range(1,5)]
#print(range_list)

#-----------------------------------------------------

#names = ["Mateus", "Marcos", "Douglinhas", "Peralta", "Jake"]

#short_names = [name for name in names if len(name) < 5]
#print(short_names)

#long_names = [name.upper() for name in names if len(name) > 5]
#print(long_names)

#------------------------------------------------------

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

print(result)


