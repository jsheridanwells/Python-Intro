#
# Example file for working with conditional statements
#

def main():
  x, y = 1000, 100

  # conditional flow uses if, elif, else
  if  (x < y):
    st = "x es menos de y"
  elif (x < y):
    st = "x es mas de y"
  else:
    st = "quizas x y y son iguales"

    # conditional statements let you use "a if C else b"
    # this is ternary in Python
  st = "x es menos de y" if (x<y) else "x es maior o igual a y"
  print(st)



# note: there are no switch cases in python


if __name__ == "__main__":
  main()

