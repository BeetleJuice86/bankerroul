import random

print("Welcome to the Banker Roulette!")
names_string = input("Please enter all names separated by a comma (,): ")
# split strings in order to calculate the number of names given, not the characters
names = names_string.split(", ")
# num_items is how many names is in the input
num_items = len(names)
# minus 1 because of the computer count starting with zero
choice = random.randint(0, num_items - 1)
# f string it
print(f"{names[choice]} is going to buy the meal today.")
