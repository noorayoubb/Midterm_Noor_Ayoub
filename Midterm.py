a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

print((3+10**2/2) or 70.0)

import datetime
a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year
print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

numbers = [
    "5485839837501070045005400701057389385845",
    "8025833559061079503003059701609553385208",
    "7489617719749244646336564429479177169847",
    "6593036601359343374664733439531066303956"
]

for number in numbers:
    if palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is not a palindrome.")

from urllib.request import urlopen, URLError
url = input('Enter your URL: ')
def validation_url(url):
    try:
        urlopen(url)
        return True
    except URLError:
        return False

my_list = [1, 2, 3, 4]
print("Original List:", my_list)

# Modifying the list
my_list[2] = 10
print("Modified List:", my_list)

# Immutable String
my_string = "Noor"
print("Original String:", my_string)

my_string[2]= 'L'

import random

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(1, 100))

for j in range(len(random_numbers)):
    if random_numbers[j] >= 80:
        random_numbers[j] = -random_numbers[j]

print(random_numbers)



