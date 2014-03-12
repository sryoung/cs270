import math
import collections
from awesome_print import ap
class SolutionProbabilities:
  
  def __init__(self, filename):
    self.probabilities = {}
    f = open(filename, 'rb')
    key = ''
    for line in f:
      if line[0] == '#':
        key = line[1:-1]
      else:
        data = line.split(':')

        if key not in self.probabilities:
          self.probabilities[key] = []
        else:
          self.probabilities[key].append(data)

  def getStrategyProbabilities(self):
    return self.probabilities


  # @staticmethod
  # def __getPatientPobabilityData(patient):
  #   print patient


