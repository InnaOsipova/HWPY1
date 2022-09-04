#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
#четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

print('Введите координаты точки Х и Y')
x = int(input(' X =  '))
y = int(input(' Y =  '))

if x > 0 and y > 0:
    print(f'Точка с координатами X = {x}, Y = {y} лежит в первой четверти')
elif x < 0 and y > 0:
    print(f'Точка с координатами X = {x}, Y = {y} лежит во второй четверти')
elif x < 0 and y < 0:
    print(f'Точка с координатами X = {x}, Y = {y} лежит в третьей четверти')
elif x > 0 and y < 0:
    print(f'Точка с координатами X = {x}, Y = {y} лежит в четвертой четверти')