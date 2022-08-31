"""
File: anagram.py
Name: Howard
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print(' Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        if s == EXIT:
            break
        start = time.time()
        ####################
        find_anagrams(s)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    lst = {}
    with open(FILE, 'r') as f:
        for word in f:
            v = word.strip()
            if len(v) == len(s):
                lst[v] = 0
    return lst


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    letters = []
    for v in s:
        letters.append(v)

    lst = read_dictionary(s)
    dictionary = []
    for word in lst:
        if len(s) > 1:
            if letters[0] in word and letters[1] in word:
                dictionary.append(word)
        else:
            dictionary.append(word)
    print('Searching...')
    anagram = find_anagrams_helper(letters, len(s), [], [], [], dictionary, [])
    print(anagram)


def find_anagrams_helper(letters, n, words, anagram, used_position, dictionary, new_d):
    vocabulary = ''
    first_v = ''
    if len(words) == n:
        for v in words:
            vocabulary += v
        print('Found: ' + vocabulary)
        anagram.append(vocabulary)

        print('Searching...')
        return
    else:
        for i in range(n):
            if i in used_position:
                pass
            else:
                # choose
                words.append(letters[i])
                used_position.append(i)
                # explore
                for v in words:
                    vocabulary += v

                if vocabulary not in anagram:
                    if len(vocabulary) == 1:
                        new_d.clear()
                        for word in dictionary:
                            if word[0] == vocabulary[0] and word[(len(word)-1)//2] in letters and word[len(word)-1] in letters:
                                new_d.append(word)
                    if has_prefix(vocabulary, new_d):
                        find_anagrams_helper(letters, n, words, anagram, used_position, dictionary, new_d)
                vocabulary = ''
                # un-choose
                words.pop()
                used_position.pop()
    return anagram


def has_prefix(sub_s, dictionary):
    """
    :param sub_s:
    :param dictionary: dictionary txt
    :return: True or False
    """
    true = 0

    for word in dictionary:
        if word.startswith(sub_s):
            true += 1
            break
    if true == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    main()
