"""
File: quadratic_solver.py
Name:Howard
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Give a, b, c three numbers that distinguish discriminant >0, <0 or 0 and calculate roots and x value.
	"""
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = float(input('Enter b: '))
	c = float(input('Enter c: '))
	x = b**2-4*a*c
	if x > 0:
		y = math.sqrt(x)
		px = (-b + y) / (2 * a)
		sx = (-b - y) / (2 * a)
		print('Two roots: '+str(px)+', '+str(sx)+'')
	elif x == 0:
		print('One roots: '+str(-b/(2*a))+'')
	else:
		print('No real roots: ')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
