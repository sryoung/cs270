# System for obesity management for CS270 project
# Lennon Chimbumu Stephanie Young 

from awesome_print import ap
import sys
import csv
from patient import Patient
from solution_probabilities import SolutionProbabilities

patients = []
def read_patient_data(filename):
  with open(filename, "rb") as in_file:
    reader = csv.reader(in_file)
    next(reader, None)
    for row in reader:
      patient = Patient(name=row[0], age=row[1], weight=row[2], height=row[3], sex=row[4], target_weight=row[5], id=row[6], economic_class=row[7])
      patients.append(patient)


if __name__ == "__main__":
  read_patient_data('data/patient_data.csv')
  probability_rules = SolutionProbabilities('data/solution_probabilities.txt')

  print patients[1].getPatientRecommendetion(probability_rules.getStrategyProbabilities())
  print '######################'
  print patients[2].getPatientRecommendetion(probability_rules.getStrategyProbabilities())
