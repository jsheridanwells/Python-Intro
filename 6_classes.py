#
# Example file for working with classes
#

class myClass():
  def myMethod1(self):
    print("myClass method number one")

  def myMethod2(self, str):
    print("myClass method number two ", str)

class otroClasse(myClass): # inherits methods from myClass
  def myMethod1(self):
    print("otro classe, metodo uno")

def main():
  c = myClass() # this is an object instance of myClass
  c.myMethod1()
  c.myMethod2('es string')

  c2 = otroClasse()
  c2.myMethod1()
  c2.myMethod2('amazing string') # actually calls myClass#myMethod2

if __name__ == "__main__":
  main()
