
from console import Console

class Prover(object):
  def __init__(self):
    self.__name = "Prover"
    Console.write(self.__name, "Initialising")
  
  def __del__(self):
    pass

  def prove(self):
    Console.write(self.__name, "proving x")

