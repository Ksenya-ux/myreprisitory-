n = int(input())
if n % 2 != 0 and n % 25 == 0:
	fb = '+'
else:
	fb = '-'
if n % 2 == 0 and n % 25 == 0:
	fa = '+'
else:
	fa = '-'
if n % 8 == 0:
	fc = '+'
else:
	fc = '-'
print(f'A {fa} B {fb} C {fc}')
