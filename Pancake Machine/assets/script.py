# If you do not have Python installed, you can get it at https://www.python.org/downloads/
# Python is needed to run the program...

# intro
print("Welcome to pancake machine 2.0")
name = input("Enter name: ")
print("Hello " + name)

# ingredients amount
flour = int(input("How much flour do you have in grams?: "))
if flour > 0:
    pass
else:
    print("That is not enough flour")
    exit()
    pass

milk = int(input("How much milk do you have in deciliters?: "))
if milk > 0:
    pass
else:
    print("That is not enough milk")
    exit()
    pass

eggs = int(input("How many eggs do you have?: "))
if eggs > 0:
    pass
else:
    print("That is not enough eggs")
    exit()
    pass

sugar = int(input("How much sugar do you have in grams?: "))
if sugar > 0:
    pass
else:
    print("That is not enough sugar")
    exit()
    pass

# calculations
# The numbers are the amounts you will need to make 8 pancakes (a portion)
flourratio = flour / 200 
milkratio = milk / 3.5
eggratio = eggs / 2
sugarratio = sugar / 20

smallestratio = flourratio

if smallestratio > milkratio:
    smallestratio = milkratio
    pass

if smallestratio > eggratio:
    smallestratio = eggratio
    pass

if smallestratio > sugarratio:
    smallestratio = sugarratio
    pass

# output

print(" ")
print("-----------------------------------------------")
print(name, "you can make:", smallestratio * 8, "pancakes.")
print("Thanks for using pancake machine 2.0")
print("-----------------------------------------------")
print(" ")

from msvcrt import getch

print("Press any key to exit...")
junk = getch()