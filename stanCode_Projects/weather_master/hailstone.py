"""
File: hailstone.py
Name: Howard
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Build a Hailstone Sequence system
    """
    print('This program computes Hailstone Sequence.')
    print('')
    n = int(input('Enter a number: '))
    c = 0
    # Count for times
    while n > 1:
        o = n
        c += 1
        if o % 2 == 1:
            n = 3 * o + 1
            print(str(int(o)) + ' is odd, so I make 3n+1: ' + str(int(n)))
        elif o % 2 == 0:
            n = o / 2
            print(str(int(o)) + ' is even, so I take half ' + str(int(n)))
    print('It took ' + str(c) + ' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
