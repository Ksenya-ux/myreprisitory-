match a := eval(input()):
	case (int(a),*args):
		print(a)
	case (*args, str(a)):
		print(a)
	case _:
		print("UNKNOWN")
