from collections import UserString

class DivStr(UserString):
    def __init__(self, seq=None):
        if seq is None:
            super().__init__("")
        else:
            super().__init__(seq)
    
    def __floordiv__(self, n):
        if n <= 0:
            return iter([])
        length = len(self.data)
        if length == 0:
            return iter([DivStr()] * n)
        
        part_len = length // n
        if part_len == 0:
            return iter([])
        
        result = []
        for i in range(n):
            start = i * part_len
            end = start + part_len
            result.append(DivStr(self.data[start:end]))
        return iter(result)
    
    def __mod__(self, n):
        if n <= 0:
            return DivStr(self.data)
        length = len(self.data)
        remainder_len = length % n
        if remainder_len == 0:
            return DivStr()
        return DivStr(self.data[-remainder_len:])
    
    def __getitem__(self, key):
        result = super().__getitem__(key)
        if isinstance(result, str):
            return DivStr(result)
        return result
    
    def lower(self):
        return DivStr(self.data.lower())

if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
