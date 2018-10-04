import random 
import time
import scipy
import scipy.stats
from scipy.stats import chisquare

random.seed = (420)
def rollingDelay():
	for x in range (0,3):
		
		print ('Rolling...')
		time.sleep(.75)

def randResponse():
	responses = ['Huzzah, a', 'You rolled a', 'By Bahamut\'s beard, a', 'I say, a']
	response = responses[random.randint(0,len(responses))-1]
	return response



def getRolling():
	
	die = input('d:?')

	while (die != "done"):
		rollingDelay()
		out,lucky = rollDice(die)
		resp = randResponse()
		if (lucky and lucky != 'Nothing'):
			resp = 'Luck smiles upon you with a,'
		if (not lucky):
			resp = 'Luck frowns upon you with a,'

		print (resp, out, '!')
		die = input('d:?')
	if (die == 'done'):
		print ('Thanks for playing!')
		listener()

def rollDice(num):
	
	num = int(num)
	roll = random.randint(1,num)
	if (num == roll):
		luck = True
	elif(roll == 1):
		luck = False
	else:
		luck = 'Nothing'	
	return str(roll),luck

def tester():
	#get input for the type of die and number of rolls
	faces = input ('Sides? ')
	rolls = input ('Number of Rolls? ')
	print ('Testing randomness for d',faces, 'by rolling', rolls, 'times.')
	#cast faces and rolls as integers
	faces = int(faces)
	rolls = int (rolls)
	#initialize counter and outcomes
	counter = [0] * faces
	outcomes = [0] * rolls
	observed_values=scipy.array([0] * faces)
	expected_values=scipy.array([0] * faces)

	
	#print ('counter length',len(counter))
	#print ('outcomes length', len(outcomes))
	#set counter list (each elemement is a possible outcome) to zero
	for i in range (0,faces):
		counter[i] = 0
		expected_values[i] = (int(rolls/faces))
	
		#print (counter[i])
	#roll inputted number of 'rolls'
	for j in range (0,rolls):
		outcomes[j] = rollDice(faces)[0]
		
		#print (outcomes[j])
	#for each outcome, add an instance of it in the counter list
	for k in range (0, len(outcomes)):
		out = outcomes[k]
		out = int(out)

		#print ('out',out)
		#print ('type of out', type(out))
		#print ('counter at out', counter[out])
		counter[out-1] = counter[out-1] + 1
		observed_values[out-1] = counter [out-1]
	#print the number of each outcome
	diff = 0
	lar = 0
	for l in range (0,len(counter)):
		if (abs(observed_values[l] - expected_values[l])>diff):
			diff = abs(observed_values[l] - expected_values[l])
			lar = l+1
		print (l+1,'expected', expected_values[l],'times and rolled',observed_values[l],'times')
	

	chisquareval,pval = scipy.stats.chisquare(observed_values, f_exp=expected_values)
	print ('Chi-square value =', chisquareval)
	print ('P-value =', pval)
	print ('Degrees of freedom =', (faces-1))
	print ('Largest difference at', lar, 'with a discrepency of', diff)
	if (pval >.05):
		print ('''There is insufficient evidence to reject the null hypothesis
		that the observed values are consistent with the expected values. Observed values are
		properly random.''')
	if (pval <= .05):
		print ('Test is significant at a 5 percent significance level')
		print ('''There is sufficient evidence to reject the null hypothesis and 
		support the alternative hypothesis that the observed values are not consistent with
		the expected values. Try a bigger sample size.''')
		
	listener()
			 

def listener():
	action = input ("""Type \'roll\' to roll dice, \'test\' to test the'
	 roller, and \'add\' to add a response: """)
	if (action.find('roll') != -1):
		getRolling()
	elif(action.find('test') != -1):
		tester()
	'''elif(action.find('add', beg = 0, end = len(action)) != -1):
		tester()'''
	print ('Thanks for playing!')


listener()
#getRolling()