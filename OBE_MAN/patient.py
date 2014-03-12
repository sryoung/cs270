import math
from solution_probabilities import SolutionProbabilities
from awesome_print import ap

#What to do when rule doesn't exist?
#Have default value? Or don't include at all? (Don't include probably better)...
#Normalize by number of rules? Count number of unique rules...

class Patient:

  def __init__(self, name=None, age=None, weight=None, height=None, sex=None, target_weight=None, id=None, economic_class=None):

    self.name = name
    self.age = int(age)
    self.weight = float(weight)
    self.height = float(height)
    self.sex = sex
    self.target_weight = float(target_weight)
    self.bmi = self.calculateBMI()
    self.economic_class = economic_class
    self.id = id
    self.tried_solutions = None
    self.current_solution = None
    self.probabilities = {}

  def getPatientRecommendetion(self, probabilities):
    
    self.determine_probability_vectors(probabilities)
    return self.getRecommendedSolutions()

  # def getRecommendedSolutions(self):
  #   return []

  def determine_probability_vectors(self, probabilities):
    solution_probability_matrix = {}
    for strategy in probabilities:
      individual_probabilities = {}
      for probs in probabilities[strategy]:
        attribute = probs[0]
        if attribute == 'age':
          age_prob = self.__getAgeProbability(probs)
          individual_probabilities['age_prob'] = age_prob
        if attribute == 'bmi':
          bmi_prob = self.__getBMIProbability(probs)
          individual_probabilities['bmi_prob'] = bmi_prob
        if attribute == 'sex':
          sex_prob = self.__getSexProbability(probs)
          individual_probabilities['sex_prob'] = sex_prob
        if attribute == 'econ_status':
          econ_prob = self.__getEconProbability(probs)
          individual_probabilities['econ_prob'] = econ_prob
      self.probabilities[strategy] = individual_probabilities

  def __getEconProbability(self, probs):
    if probs[1] == self.economic_class:
      return probs[2]
    else:
      return float(probs[2])

  def __getAgeProbability(self, probs):
    if probs[1] == 'greater_than 13' and (self.age > 13):
      return float(probs[2])

  def __getBMIProbability(self, probs):
    if probs[1] == 'greater_than 25' and (self.bmi > 25 and self.bmi < 30):
      return float(probs[2])
    if probs[1] == 'greater_than 30' and (self.bmi > 30 and self.bmi < 35):
      return float(probs[2])
    if probs[1] == 'greater_than 35' and (self.bmi > 35):
      return float(probs[2])
    return 0.01

  def __getSexProbability(self, probs):    
    if probs[1] == 'm' and self.sex.lower() == 'm':
      return float(probs[2])
    else:
      return float(probs[2])
    

  def calculateBMI(self):
    height = float(self.height/100)
    return float(self.weight / math.pow(height,2))
    

  def __repr__(self):
    return '[Patient #%s:\n\t Name \t\t: %s\n\t Age \t\t: %s\n\t Weight(kg) \t: %s\n\t Height(cm) \t: %s\n\t Sex \t\t: %s\n\t Target_weight \t: %s\n\t BMI \t\t: %s]' % (self.id, self.name, self.age, self.weight, self.height, self.sex, self.target_weight, self.bmi)

