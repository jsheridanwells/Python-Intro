#
# Example file for working with functions
#

# define a basic function
def func1(): # colon indicates scope, like {} in C langs
  print("soy funcion sin parametros")

# function that takes arguments
def func2(arg1, arg2):
  print(arg1, " ", arg2)

# function that returns a value
def cubed(n):
  return n*n*n

# function with default value for an argument
def power(n, x=1):
  result = 1
  for i in range(x):
    result = result * n
  return result

#function with variable number of arguments
def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result

func1() # executes function
print(func1()) # executes function, then evaluates to Py constant None
print(func1) # prints memory location of func1

func2("im", "awesome")
print(func2("im", "awesome"))

print(cubed(3))

print(power(2)) # x defaults to 1
print(power(2,3)) # x is assigned 3
print(power(x=3, n=2)) # order of arguments can be reversed

print(multi_add(10, 3, 24)) # => 37
print(multi_add(10, 3, 21)) # => 34
