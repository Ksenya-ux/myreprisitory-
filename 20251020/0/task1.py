import string
s = input()
def anti_vowels(s):
	letters = string.ascii_lowercase
	c = set(s) -  set('aeiou')
	print(c)
