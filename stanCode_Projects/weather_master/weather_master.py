"""
File: weather_master.py
Name: Howard
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -1


def main():
	"""
	Compute the average, highest, lowest, cold days among the inputs.
	"""
	print('stanCode "weather Master 4.0"!')
	t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if t == EXIT:
		print('No temperatures were entered')
	else:
		maximum = t
		minimum = t
		total = t
		n = 1
		c = 0
		if t < 16:
			c += 1
		while True:
			t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if t == EXIT:
				break
			if t > maximum:
				maximum = t
			elif t < minimum:
				minimum = t
			total += t
			n += 1
			if t < 16:
				c += 1
		print('Highest temperatures = ' + str(maximum))
		print('Lowest temperatures = ' + str(minimum))
		print('Average = ' + str(total / n))
		print(str(c) + ' cold day(S)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
