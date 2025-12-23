def Subtr(obj1, obj2):
    if isinstance(obj1, (list, tuple)) and isinstance(obj2, (list, tuple)):
        set2 = set(obj2)
        result = []
        
        for item in obj1:
            if item not in set2:
                result.append(item)
            else:
                set2.remove(item)
        return type(obj1)(result)
    
    else:
        return obj1 - obj2
    
data = eval(input())
result = Subtr(*data)
print(result)
