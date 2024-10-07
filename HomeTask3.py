wow = 0
c = 0
i = 0
l = input('Введите трёхзначнео число с разныеми цифрами ')
q = int(l)
if q > 999 or q < 100:
    print("Число не трёхзначное")
    exit()
while i < 1:
    i = i+1
    a = q // 100
    b = q // 10 % 10
    c = q %10
    if a == b or a == c or b == c:
        print("Одинаковые цифры")
        exit()
while wow < 6:
    num = 0
    wow = wow + 1
    while num < 1:
     num = num  +   1
     a = str(q // 100)
     b = str(q // 10 % 10)
     c = str(q %10)
     print(c+b+a,' ',wow,' число')
