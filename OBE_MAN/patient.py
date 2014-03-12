import math
from solution_probabilities import SolutionProbabilities
class Patient:

  def __init__(self,
              name=None,
              age=None,
              weight=None,
              height=None,
              sex=None,
              target_weight=None,
              id=None):

    self.name = name
    self.age = int(age)
    self.weight = float(weight)
    self.height = float(height)
    self.sex = sex
    self.target_weight = float(target_weight)
    self.BMI = self.calculateBMI()
    self.id = id
    self.tried_solutions = None
    self.current_solution = None

  def getPatientRecommendetion(self):
    pass
    

  def calculateBMI(self):
    height = float(self.height/100)
    return float(self.weight / math.pow(height,2))
    

  def __repr__(self):
    return '[Patient #%s:\n\t Name \t\t: %s\n\t Age \t\t: %s\n\t Weight(kg) \t: %s\n\t Height(cm) \t: %s\n\t Sex \t\t: %s\n\t Target_weight \t: %s\n\t BMI \t\t: %s]' % (self.id, self.name, self.age, self.weight, self.height, self.sex, self.target_weight, self.BMI)

