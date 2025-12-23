def Sub(first, second):
    # Проверяем, что оба аргумента имеют одинаковый тип
    assert type(first) is type(second)

    # Если аргументы являются последовательностями (список или кортеж)
    if isinstance(first, (list, tuple)):
        # Преобразуем второй аргумент в множество для быстрого поиска
        second_set = set(second)
        # Оставляем только элементы, которых нет во втором аргументе
        filtered_result = [item for item in first if item not in second_set]
        # Возвращаем результат в том же типе, что и первый аргумент
        return type(first)(filtered_result)

    # Для других типов (например, числа) используем обычное вычитание
    return first - second


# Читаем и преобразуем входные данные в кортеж аргументов
args = eval(f"({input()})")
# Вызываем функцию с распакованными аргументами
print(Sub(*args))

import sys
exec(sys.stdin.read())
