# Создаем список чисел от 1 до 20
original_list = list(range(1, 21))

# Фильтруем четные числа
even_list = [x for x in original_list if x % 2 == 0]

# Выводим результаты
print("Исходный список:", original_list)
print("Список четных чисел:", even_list)