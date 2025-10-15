from decimal import Decimal
def multiplier(x,y,Type):
	return Type(Decimal(x*y))
print(multiplier(2,3,float))
