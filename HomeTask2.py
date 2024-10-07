mas = []
while True:

    num = int(input("Введите число "))
    mas.append(-num)
    mas.append(num+1)
    mas.sort()
    print (mas)
    plus = 0
    minus = 0
    for element in  mas:
        if element >= 0:
            plus = element + plus
        else:
            minus = element + minus
    print("Сумма положительных чисел", plus)
    print("Сумма отрицательных чисел", minus)
                