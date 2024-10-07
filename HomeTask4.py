ship = 'Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2'
while True:
    turn    =   input("Ваш ход ")
    if turn[0] == "1" or turn[0] == "2" or turn[0] == "3" or turn[0] == "4" or turn[0] == "5" or turn[0] == "6" or turn[0] == "7" or turn[0] == "8" or turn[0] == "9" or turn[0] == "10":
        print ("Введите сначало букву, затем число")
        continue
    if len(turn) > 2 or len(turn) < 2:
        print ("Введите два символа. Пример Л2")
        continue
    if ship.lower().find(turn.lower()) > -1 :
        print ("Попали")
        break
    else:
        print ("Не попали")
        break
