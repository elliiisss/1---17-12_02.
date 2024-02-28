import random
oshibka = 0
pravilno = 0

print ("'математика для детей.'  Решите пример")
while oshibka < 3:
    a = random.randint(0,10)
    b = random.randint(0,10)
    print (f'{a} + {b} =' , end='')
    if a + b == int( input()):
        print ("Правильно!")
        pravilno += 1
    else:
        print ("Ответ неверный")
        oshibka += 1
else:
    print ("Игра окончена. Правильных ответов:", pravilno)