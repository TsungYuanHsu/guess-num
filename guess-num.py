# Generate a random integer from 1 to 100(do not print out)
# Let users guess the number repeatedly
# If the guess is correct, print 'You guess it right'
# If the guess is wrong, print 'Higher or lower than the answer'

import random

r = random.randint(1, 100)

while True:
	num = int(input('Please guess a number: '))
	if num == r:
		print('You guess it right')
		break
	elif num > r:
		print('It is higher than the answer')
	elif num < r:
		print('It is lower than the answer')