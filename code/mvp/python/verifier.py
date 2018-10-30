
from console import Console

class Verifier(object):
  def __init__(self):
    self.__name = "Verifier"
    Console.write(self.__name, "Initialising")
  
  def __del__(self):
    pass

  def verify(self):
    Console.write(self.__name, "verifying x")
