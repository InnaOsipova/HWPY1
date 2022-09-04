#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

from turtle import distance


print('Введите координаты первой точки')
x1 = int(input('X1= '))
y1 = int(input('Y1= '))
print('Введите координаты второй точки')
x2 = int(input('X2= '))
y2 = int(input('Y2= '))
distance_points = round (((x2-x1)**2 + (y2-y1)**2)**(1/2), 3)
print(f'Расстояние между точками координатами ({x1}, {y1}); ({x2}, {y2}) = {distance_points}')