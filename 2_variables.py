#
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# # re-declaring the variable works
f="despacito"
print(f)

# # ERROR: variables of different types cannot be combined
# print("soy string" + 666)
# python is strongly typed
# but this works:
print("soy string" + "666")

# Global vs. local variables in functions
def myFunction():
  global f # now that this is global, global f gets reassigned below
  f="rapidito"
  print(f)

myFunction() # prints f from myFunction scope
print(f) # prints f from global scope

del f # deletes f
# print(f) ## throws error, name f is not defined
