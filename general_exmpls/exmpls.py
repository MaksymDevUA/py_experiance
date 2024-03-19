- The line f = open("output.txt", "w") is used to open a file named "output.txt" in write mode ("w") and assign a file object to the variable f


my_list = [i ** 2 for i in range(1, 11)] # Generates a list of squares of the numbers 1 - 10














# Guess a number
from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
while guesses_left != 0:
  guess = int(raw_input("Your guess: "))
  guesses_left -= 1
  if guess == random_number:
    print "You win!"
    break
else:
  print "You lose."
for i in range(10):
  print i




FOR
Enumerate - build in funct
choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices): #u can add start=1 - it means that index should start from 1
print index + 1, item


Zip - build in funct. zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b): # Add your code here!
print max(a, b) # show max


list1 = ['a', 'b', 'c'] list2 = [10, 20, 30] # Use enumerate and zip together to get both index and zipped values
for index, (value1, value2) in enumerate(zip(list1, list2)):
	print(f"Index: {index}, Value from list1: {value1}, Value from list2: {value2}")




def is_int(x):
absolute = abs(x)
rounded = round(absolute)
return absolute - rounded == 0
print is_int(10)
print is_int(10.5)




def factorial(n): su = 1 while n != 0: su *= n n -= 1 return su


def is_prime(x): iters = x-1 for i in range(iters, 1, -1): if x%i == 0: print(f"X={x} and X/{i} == 0 - it's not prime") return False print(f"{x} is prime") """for i in range(3, 1, -1): print(i)""" is_prime(26)




    if isinstance(length, (int, float)) and isinstance(width, (int, float)):




import random
a_list = []
for i in range(1,12):
   rn = random.randrange(1, 100)
   a_list.append(rn)
print(a_list)
a_list = [elem * 2 for elem in a_list]
print(a_list)


REVERSING DICT
dct = {'a': 1, 'b': 2, 'c': 3}
sort_dct = {}


print(sort_dct)
for key in dct:
  j = key
  i = dct[key]
  sort_dct[i] = j
  print(key)
  print(dct[key])


print(sort_dct)