# Дано пятизначное целое число. Напишите алгоритм, который возведёт количество десятков в степень количества единиц. Затем умножит это число на количество сотен. И делит получившееся число 
# на разность количества десятков тысяч и количества тысяч
# Например, есть число 46275
# Необходимо возвести 7 (десятки) в степень 5 (единицы), умножить получившееся число на 2 (сотни), и разделить на разность между 4 (десятки тысяч) и 6 (тысячи) то есть (4-6)
# В результате необходимо получить вещественное число. В нашем примере это будет: -16807.0

num = int(input("Введите пятизначное число: "))

# Необходимо это число разделить на разряды
ten_thousandth = num // 10000 # десятки тысяч
thousands = (num % 10000) // 1000 # тысячи
hundreds = (num % 1000) // 100 # сотни
tens = (num % 100) // 10 # десятки
ones = num % 10 # единицы

a = tens ** ones * hundreds / (ten_thousandth - thousands)
print("Результат:")
print(a)