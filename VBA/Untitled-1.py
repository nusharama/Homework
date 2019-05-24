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