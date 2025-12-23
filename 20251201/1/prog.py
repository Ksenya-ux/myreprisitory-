class sole(type):
	def __new__(metcls, name, parents, namespace):
		for cls in parents:
			if isinstance(cls,final):
				raise TypeError(f"{cls.__name__} is final")
		return super().__new__(metcls, name, parents, namespace)

