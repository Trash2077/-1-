while True:
  try:
      a = 0
      s = input()
      if s =='exit':
         break
      i = int(s)
      i = abs(i)
      if i == 0 :
         print ('длина числа - 1')
         continue
      while i > 0:
         i = i // 10
         a = a+1
      print ('Длина числа - ',a)  
  except ValueError:
    print('Ошибка! Вы ввели нецелое число')
    