import random
from termcolor import colored

def bankers_formula(E, C, M):
	return 12275.30 + (0.748 * E) - (2714.74 * C) - (0.40 * M) + (.0000006986 * E^2) + (32.623 * C^2)

def inputNumber():
  while True:
    try:
       userInput = int(input("Choose what case to open!"))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 

class game:
	def __init__(self):
		self.case_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 
			   400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 
			   100000, 200000, 300000, 400000, 500000, 750000, 1000000]
		random.shuffle(self.case_values)
		self.round = 0
		self.round_cases_to_open = [6,6,5,4,3,1]
		self.cases = []
		for c in range(26):
			self.cases.append(case(c+1, self.case_values[c]))
		self.case_picked = case(27,0)

	def pick_case(self, nr):
		self.case_picked = self.cases.pop(nr)


	def start_round(self):
		for pick in range(self.round_cases_to_open[self.round]):
			while True:
				chosen_nr = inputNumber()
				if self.cases[chosen_nr].opened == True:
					print("Case has already been opened.")
					continue
				self.cases[chosen_nr].opened = True
				print("Case #{} had a value of {}".format(chosen_nr, self.cases[chosen_nr]))
				break

		self.round += 1

	def print_cases(self):
		print("{:7d}{:5d}{:5d}{:5d}{:5d}{:5d}".format(*[i.index for i in self.cases[0:6]]))
		print("{:5d}{:5d}{:5d}{:5d}{:5d}{:5d}{:5d}".format(*[i.index for i in self.cases[6:13]]))
		print("{:5d}{:5d}{:5d}{:5d}{:5d}{:5d}{:5d}".format(*[i.index for i in self.cases[13:20]]))
		print("{: >7}{: >5}{:5d}{:5d}{:5d}{:5d}".format(*[1000 if i.opened else i.index for i in self.cases[20:26] ]))
class case:
	def __init__(self, index, value):
		self.index = index
		self.value = value
		self.opened = False
	def open(self):
		self.opened = True
		print(self.value)

game1 = game()
game1.print_cases()
game1.start_round()
game1.print_cases()

