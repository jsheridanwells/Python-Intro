#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while(x<=5):
    print(x)
    x = x + 1 # 1,2,3,4,5

  # define a for loop
  # x is defined as the iterator
  for x in range(5,10): # range starts at 5, terminates before 10
    print(x) # 5,6,7,8,9

  # use a for loop over a collection
  days = [
    'mon',
    'tue',
    'wed',
    'thu',
    'fri',
    'sat',
    'sun'
  ]
  for day in days:
    print(day)


  # use the break and continue statements
  for n in range(5,10):
    if (n==7): break # on 7, loop will terminated, will not print
    print(n)

  for n in range(5,10):
    if (n%2==0): continue
    print(n) # prints 5, 7, 9, continue resets loops

  #using the enumerate() function to get index
  for i,day in enumerate(days):
    print(day, i) # prints day + 1, eg. mon 0

if __name__ == "__main__":
  main()

# python only has while and for loops
