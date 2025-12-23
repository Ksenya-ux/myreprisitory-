import sys

def main():
    user_input = sys.stdin.readline().rstrip('\n')
    
    if not user_input:
        return
    
    data = user_input.encode('latin-1')
    
    N = data[0]
    tail = data[1:]
    L = len(tail)
    
    parts = []
    
    for i in range(N):
        start = int(i * L / N)
        end = int((i + 1) * L / N)
        parts.append(tail[start:end])
    
    parts.sort()
    
    result = bytes([N]) + b''.join(parts)
 
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout.buffer.write(result)
    else:
        # Если нет buffer, выводим как текст
        sys.stdout.write(result.decode('latin-1'))

if __name__ == "__main__":
    main()

exec(sys.stdin.read())

