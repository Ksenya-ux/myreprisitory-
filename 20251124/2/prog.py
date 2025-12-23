import sys

def main():
    
    input_text = input()
    
    if not input_text:
        print("Ошибка: нет входных данных")
        return
    
    input_bytes = input_text.encode('latin-1', errors='replace')
    
    try:
        latin1_decoded = input_bytes.decode('latin-1')
        
        cp1251_bytes = latin1_decoded.encode('latin-1')
        
        result = cp1251_bytes.decode('cp1251', errors='replace')
        
        print(result)
        
    except Exception as e:
        print(f"Ошибка: {e}")
        
        result_chars = []
        for byte in input_bytes:
            try:
                char = bytes([byte]).decode('latin-1')
                cp1251_byte = char.encode('latin-1')
                result_char = cp1251_byte.decode('cp1251')
                result_chars.append(result_char)
            except:
                result_chars.append('?')
        
        print("\nРезультат (с заменой ошибок):")
        print(''.join(result_chars))

if __name__ == "__main__":
    main()

exec(sys.stdin.read())

