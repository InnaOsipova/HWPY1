#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number_chet = int(input('Введите номер четверти :  '))
if number_chet == 1:
    print('В данной четверти координаты X (0; + бесконечность), Y (0; + бесконечность)')
elif number_chet == 2:
    print('В данной четверти координаты X (- бесконечнось; 0), Y (0; + бесконечность)')
elif number_chet == 3:
    print('В данной четверти координаты X (- бесконечнось; 0), Y (- бесконечнось; 0)')
elif number_chet == 4:
    print('В данной четверти координаты X (0; + бесконечность), Y (- бесконечнось; 0)')
else:
    print('Такой четверти нет')