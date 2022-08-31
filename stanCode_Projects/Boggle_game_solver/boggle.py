"""
File: boggle.py
Name: Howard
----------------------------------------
This program can find all words in a 4x4 square grid which input by the user.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	letters = in_data()
	start = time.time()
	####################
	if len(letters) == 16:
		find_word(letters)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(letters):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	lst = []
	with open(FILE, 'r') as f:
		for w in f:
			word = w.strip()
			if len(word) >= 4 and word[0] in letters:
				lst.append(word)
	return lst


def in_data():
	letters = ''
	for i in range(4):
		letter = input(str(i+1) + ' row of letters: ')
		if letter[1] == ' ' and letter[3] == ' ' and letter[5] == ' ' and len(letter) == 7:
			for v in letter:
				if v != ' ':
					letters += v
		else:
			print('Illegal input')
			break
	return letters


def find_word(letters):
	dictionary = read_dictionary(letters)

	xy_lst = [letters[0:4], letters[4:8], letters[8:12], letters[12:16]]
	used = []
	total = 0
	for x in range(4):
		for y in range(4):
			used.append((x, y))
			found = find_word_helper(xy_lst, x, y, used, dictionary, [])
			total += found
			used.clear()
	print('There are ' + str(total) + ' words in total')


def find_word_helper(xy_lst, x, y, used, dictionary, found):
	words = ''
	for v in used:
		words += xy_lst[v[0]][v[1]]
	if len(words) >= 4 and words in dictionary and words not in found:
		print("Found " + words)
		found.append(words)
		return
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= x + i < 4:
					if 0 <= y + j < 4:
						if (x + i, y + j) not in used:
							# choose
							used.append((x + i, y + j))

							# explore
							if has_prefix(used, dictionary, xy_lst):
								x = x + i
								y = y + j
								find_word_helper(xy_lst, x, y, used, dictionary, found)
								if len(used) >= 4:
									find_word_helper(xy_lst, x, y, used, dictionary, found)
							# un -choose
							used.pop()
							y = used[-1][1]
							x = used[-1][0]
	return len(found)


def has_prefix(sub_s, dictionary, xy_lst):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary:
	:param xy_lst:
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	sub = ''
	for v in sub_s:
		sub += xy_lst[v[0]][v[1]]

	for word in dictionary:
		if word.startswith(sub):
			return True
	return False


if __name__ == '__main__':
	main()
