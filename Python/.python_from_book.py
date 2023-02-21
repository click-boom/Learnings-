""" ----------------------------------------------------****Basic****----------------------------------------------------------- """
print("hello World!")
""" 1st python program """

message = " Hello World!"
print(message)
# using variable to print 1st program


# if you want to use a block comment after a print or in line with a working statement, separate the comment and statement with semi-col
# print("hello World!"); """ 1st python program """   -------------- this is also correct

message = " hello rohan"
print(message)  # ---------------->> here, since compiler works one by one, mathi ko message ko kaam sakesi mathiko value becomes garbage value ani same variable ma new vslue assign and work garx, i this case all 3 statements get printed


print("\n")

""" # -------------------------------------------------**Strings**----------------------------------------------------------------- """

# String is simply a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes around your strings

print('I told my friend, "Python is my favorite language!"')
#  since both single and double quote can be used for string, using one instide other makes inside one a printable character


print("\n")
# Method is an action that Python can perform on a piece of data,  like strlen in C. It is denoted by a dot(.) after variable name.
name = 'rohan chaulagain'
# title capitalizes 1st letter of each word
print('using title:', name.title())
print('using upper:', name.upper())  # ---> changes all letters to uppercase
name = 'ROHAN CHAULAGAIN'
print('using lower:', name.lower())  # ---> changes all letters to LOWERCASE
print("\n")

""" ---------**Concatenation/ Combining**--------------- """

first_name = 'rohan'
last_name = 'chaulagain'
# ------------- bich ma 'space' string thapeko
full_name = first_name+' '+last_name
print('using concatenation:' + full_name)
print("\n")

# Note: If needed to concatenate a sting and integer together, 1st change the integer to string, then concatenate
age = 18+1
print("concatenation of int and string:",
      first_name + ' ' + last_name+' age=' + str(age))
print("\n")
# --------------------------------------------------------
name = ' rohan '
print('without rstrip:', name)
# -----rstrip() removes the space only on right of rohan,to see actual results do in IDLE or terminal
print('remove right space:', name.rstrip())
# -----lstrip() removes the space only on left of rohan,to see actual results do in IDLE or terminal
print('remove left space:', name.lstrip())
# -----strip() removes the space only on left of rohan,to see actual results do in IDLE or terminal
print('remove both side space:', name.strip())
test = 'r c'  # --- strip cant remove space from middle

# to remove the space permanently from the variable value, reassign the same value includeing rstrip, i.e. name = name.rstrip()

print("\n")
""" ---------------------------------------*****Integers****------------------------------------------------------------------------------ """

a, b = 3, 2
print("Sum=", a+b)
print("Diff=", a-b)
print("Mul=", a*b)
print("Div=", b/a)
print("Exponent=", 3**3)

# Note: Python follows PEDMAS: Parenthesis, Exponent, DMAS --- DMAS from BODMAS

# ----------------------------------------------------
# Zen of Python/ core rules for a programmer:
# Note : ====>  to see those, use the command python3 and in terminal then enter import this
# ----------------------------------------------------
print("\n")

""" --------------------------------------****Lists****------------------------------------------------------------------------------ """

# List == collection of items in a particular order, indicated by []
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# accessing element 1, i.e. trek
print(bicycles[0])

# Using string functions in list, eg, upper
print(bicycles[0].upper())

# list jatisukai lamo vae ni last ko element access garnw, use -1
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


# doesnt require quotation mark for numerical but requires for alphabetical values, separated default by comma
print("\n")
numbers = [0, 1, 2]
print(numbers)

print("\n")
bicycles[0] = "Rohan"
print("Changing list element 1:"+bicycles[0])

# Adding new element at last, you can also start with a blank list and keep appending
bicycles.append('Chaulagain')
# Note: If needed to concatenate a sting and list together, 1st change the list to string, then concatenate
print("Adding/Appending element at last:" + str(bicycles))


bicycles.insert(3, 'Prasad')
print("Adding/Inserting element at specific place:" + str(bicycles))

del bicycles[3]
print("Removing an element at specific place:" + str(bicycles))

"""  pop() method removes the last item in a list, but it lets you work with that item after removing it. We can also pop from a position by specifing that posotion in parenthesis"""
print("\n")

bikes = ['Honda', 'yamaha', 'Sujuki']
print(bikes)

popped_bikes = bikes.pop()
print('default_popped_bikes:' + popped_bikes)

print('Remaining after popping:' + str(bikes))

bikes.insert(1, popped_bikes)
print('Inserting a popped bike:' + str(bikes))

new_pop = bikes.pop(2)
print('new pop:' + new_pop)

print('After popping yamaha:'+str(bikes))

bikes.append(new_pop)
print('Appended again:'+str(bikes))

old = 'Honda'    # assign the value to be removed earlier, if you want to use it later
bikes.remove('Honda')
print('I dont want to ride ' + old + ' because it is old fashioned.')
print('\n')

print('All managing practiced:' + str(bikes))
print('\n')
# ----------------------** Orgainzing Lists**-----------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print('before sorting:'+str(cars))
cars.sort()  # --------------> The sort() sorts the list permanently
print('after sorting:'+str(cars))

cars.sort(reverse=True)  # ---------------Descending order
print('Sort in descending:'+str(cars))
print('\n')
print(cars2)
print('Temporary sorted:' + str(sorted(cars2)))
print('printed again:' + str(cars2))

cars2.reverse()  # ---------------changes the order permanently
print('Reverse listing:' + str(cars2))

# ---------------printing the number of cars in the list with len()
print('No. of items:' + str(len(cars2)))

""" ----------------------------------****Loops****------------------------------------------ """

magicians = ['prakash', 'prabin', 'sujan']
for magician in magicians:
    print(magician.title() + ' is a great magican')
    print('THank you for coming.')
    print('\n')
print('Thank you all')
# --------------** Number loop**-----------------------
for value in range(1, 6):
    print(value)  # ------------> Last  value 1 badaerw halnuparne hunx
print('\n')


for value in range(6):  # ---------------> Here, it starts printing from 0
    print(value)  # ------------> Last o value 1 badaerw halnuparne hunx
print('\n')


print('even number:')
for value in range(0,  11, 2):  # ------------printing even number
    print(value)


print('odd number:')
for value in range(1,  11, 2):  # ------------printing odd number
    print(value)


number_list = list(range(0, 6))
print('number list:' + str(number_list))


even_list = list(range(2, 11, 2))
print('even list:' + str(even_list))


print('\n')
odd_list = list(range(1, 10, 2))
print('odd list:' + str(odd_list))

# ------------List comprehension Method
odd = [value + 2 for value in range(-1, 9, 2)]
print('odd list 2nd method:' + str(odd))

print('\n')


sq_no = []
for value in range(1, 11):
    # ---This is direct, for easy, assign a variable to the formula and put that variable instead
    sq_no.append(value**2)
print(sq_no)

# ------------List comprehension method
squares = [value**2 for value in range(1, 11)]
print('Sq_no 2nd method:' + str(list(squares)))
print('\n')


multiple_5 = []
for value in range(1, 11):
    multiple_5.append(value*5)
print(multiple_5)

print('Max value= '+str(max(multiple_5)))
print('Min value= '+str(min(multiple_5)))
print('Sum of values= '+str(sum(multiple_5)))


count = [value + 1 for value in range(0, 20)]
print('Count:' + str(count))

print('\n')


""" --------------------------**Slicing**-------------------------- """
# =========> You can also work with a specific group of items in a list, called a slice in Python.
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# last ko value 1 ghataerw halnuparx
print('Prints 3 names from 1st element:' + str(players[0:3]))
# last ko value 1 ghataerw halnuparx
print('Prints 2 names from 2nd element:' + str(players[1:3]))
print('Prints 3 names from 1st element, 2nd method:' +
      str(players[:3]))  # last ko value 1 ghataerw halnuparx

# formula: no. of items in list= end value initialization element value

print('Prints names from a postion to last element:' +
      str(players[2:]))  # last ko value 1 ghataerw halnuparx

players = ['charles', 'martina', 'michael', 'florence', 'eli']
# ------last ma - halyo vane jati value halyo, last ko tei ota name print garx, if the list is edited, edited list ko alu print garx
print('Before append:'+str(players[-3:]))


players.append('rohan')
# ------last ma - halyo vane jati value halyo, last ko tei ota name print garx, if the list is edited, edited list ko alu print garx
print('After append:'+str(players[-3:]))

print('\n')
print('List of last 3 players:')
for player in players[-3:]:
    print(player)

    my_foods = ['pizza', 'falafel', 'carrot cake']
    frend_food = my_foods[:]  # ----------------------------- list copying
    print('my food:' + str(my_foods))
    print('my friends food:' + str(frend_food))


new_food = ['pizza', 'falafel', 'carrot cake']
food_copy = new_food

print(str(new_food))
print((food_copy))

print('\n')
# -------------------**Difference between copying lists and assigning 2 lists same value

foods = ['pizza', 'burger', 'momo']
new_foods = []
equal = foods
copy = foods[:]

foods.insert(1, 'chowmein')

print('equal:' + str(equal))
print('copy:' + str(copy))

""" ------------------------Tuple-------------------------- """

good = ('rohan', 'ram')
print('ram:' + str(good[1]))

# --------------_This is how a single value in tuple is assigned
bad = ('hitler', )
print(bad)

""" # -------------------------------Styling your code------------------------------------
Intendation: 1) leave 4 spaces / 1 tab per intendation level, i.e for vitrw pasne bela 4 1 tab and vitrw ko vitrw pasnw further 1 tab
 """


