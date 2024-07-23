from random import randint

name = input("What is your name? ")
dob = input("What year were you born in? ")

dob2 = int(dob)
minimum = dob2
maximum = dob2 + 70
year = randint(minimum, maximum)

print(f"Hello {name}, your lucky year is {year}")