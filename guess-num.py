# Generate a random integer from 1 to 100(do not print out)
# Let users guess the number repeatedly
# If the guess is correct, print 'You guess it right'
# If the guess is wrong, print 'Higher or lower than the answer'

import random
start = int(input('Please input one number as the smallest number of the range: '))
end = int(input('Please input one number as the largest number of the range: '))
r = random.randint(start, end)
guess_num = 0 # How many times you have guessed

while True:
	num = int(input('Please guess a number: '))
	guess_num += 1
	if num == r:
		print('You guess it right')
		print('You guess', guess_num, 'time(s)')
		break
	elif num > r:
		print('It is higher than the answer')
	elif num < r:
		print('It is lower than the answer')
	print('You guess', guess_num, 'time(s)')