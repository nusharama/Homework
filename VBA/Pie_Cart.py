pie_list = [
    "Pecan",
    "Apple Crisp",
    "Bean",
    "Banoffee",
    "Black Bun",
    "Blueberry",
    "Buko",
    "Burek",
    "Tamale"
    "Steak"
]
# (1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee,  (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek,  (9) Tamale, (10) Steak
allowance = 10

pie_Cart = []

for pie in pie_list:
    print(f'[{str(pie_list.index(pie))}] {pie}')
print(" Which pie would you like to bring home? ")
for x in range(allowance):
    selected = input (" How many pies would you like to bring home? ")

pie_Cart.append(pie_list[int(selected)])   
print("I brought home with me...")
for pie in pie_list:
    print(pie)

count = ['Pecan', 'Apple Crisp', 'Bean', 'Banoffee', 'Black Bun', 'Blueberry', 'Buko', 'Burek', 'Tamale', 'Steak']
count = count.count('i')
print('the count of i is:', count)
count = count.count('p')
print('the count of p is:', count)


# For loop for 5 times as in the example for candy 
# you dont know how many times your loop is going to run - use while loop 

# If people do not have too many questuions i get to eat - one time
# if people have too many questions I cannot eat

# Variables used outside of the If statement will be overridden with the variable used inside in the If statement if they are both called 'x'.

# array - collection of the sanme type of items - array of strings, characters, cannot have strings and numbers. They have a limit
# array structure is not mutable - but the values are mutable
# Lists are mutable - multiple items and they can grow. to find the element in a list is harder but easier in an array (because if you say give me the 
# 5th element and it will do it)

# Types of files - binary and text - mp3, jpef, word (specific program to open to interpret), not with a text file. 


# Open the file in "read" ('r') 
with open(file, 'r') as text:


    # This stores a reference to a file stream
    print(text)


    lines = text.read()
    print(lines)