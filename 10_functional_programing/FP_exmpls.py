def func():
    print("I am function func()!")

func()
another_name = func #Assign function() to another variable & use the current vairable as a function
another_name() #Use var as function()
print(another_name) #Output object type & memory where its placed

print("cat", func, another_name, 42) #Output the same memory cells where placed func()

objectsList = ["cat", func, another_name, 42]
print(objectsList[1])
print(objectsList[1]()) #Use function as part of list

objectsDict = {"cat" : 1, func: 2, another_name: 3, 42: 4}
print(objectsDict)
print(objectsDict[func])#Output not the funct() - value 2

animals = ["parrot", "dog", "hypo", "gecko", "vole", "ferret"]
print(sorted(animals, key=len))

print(-len('asasaassasa')) #len works with strings, minus at the begininng turn it to negative int

#--Using reversing via lambda, def, lambda()(string)--
reverse = lambda s: s[::-1] #way to reverse, -1 - in reverse way
print(reverse("reverse"))
#or in this way, using def or lambda
def rev(s):
    return s[::-1]
print(rev("asassb"))
print((lambda s: s[::-1])("I am a string"))

#--Example using lambda contruction--
print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))

#--Map examples--
nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums0 = [10, 20, 30, 40, 50, 60, 70, 80]
dblLst = [1.323, 2.422, 3.44151]
str = ["ab", "abc", "abcd", "abcde"]

doubled = map(lambda x:x*2, nums) #double each item
print(list(doubled))

str_nums = ['1', '2', '3', '4', '5', '6', '7', '8'] #converting
str_int = map(int, str_nums)
print(list(str_int))

mltpLst = map(lambda x,y: x*y, nums, nums0) #multiplying
print(list(mltpLst))

rndLst = map(round, dblLst) #rounding
print(list(rndLst))

conted = map(len, str) #counting chars
print(list(conted))


def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(5)
print(add_15(15))
print(add_15(20))