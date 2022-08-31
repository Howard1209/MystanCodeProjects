"""
File: largest_digit.py
Name: Howrad
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	return find_largest_digit_helper(n, [])


def find_largest_digit_helper(n, lst):
	if n < 0:
		n *= -1
	if n % 10 < 1:
		return
	else:
		s = n % 10
		n //= 10
		find_largest_digit_helper(n, lst)
		lst.append(s)
	return max(lst)




if __name__ == '__main__':
	main()
