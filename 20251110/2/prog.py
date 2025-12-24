import math

class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput
    
    try:
        x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)
    except (ValueError, TypeError):
        raise BadTriangle
    
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    
    if a + b <= c or a + c <= b or b + c <= a or max(a, b, c) <= 0:
        raise BadTriangle
    
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    
    return area

if __name__ == "__main__":
    import sys
    lines = sys.stdin.read().strip().splitlines()
    for line in lines:
        if not line.strip():
            continue
        try:
            area = triangleSquare(line.strip())
            print(f"{area:.2f}")
        except InvalidInput:
            print("Invalid input")
        except BadTriangle:
            print("Not a triangle")
