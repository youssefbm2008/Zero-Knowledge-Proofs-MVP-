'''
 MVP - Zero-Knowledge API
'''

from prover import Prover
from verifier import Verifier
from console import Console

if __name__ == '__main__':

  prover = Prover()
  verifier = Verifier()

  prover.prove()
  verifier.verify()
