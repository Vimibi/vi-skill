# Алгоритм проверки длинны числа
a = int(input('Введите число: '))
cikl = 0
while True:
    if a <= 0:
        break
    elif a > 0:
        a = a // 10
        cikl += 1
        print(a)

print('cikl =', cikl)
b = int(input('Введите второе число: ))
c = a + b
print('Сумма равна: ', c)
# Конец проверки числа
