start, end = map(int, input().split(','))
print([num for num in range(start, end) if all(num % divisor != 0 for divisor in range(2, int(num**0.5) + 1)) and num > 1] if start <= end else [])
