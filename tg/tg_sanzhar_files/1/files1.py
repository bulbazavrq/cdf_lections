# """
# 1) В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов и слов.
# """
# with open('1.txt', 'r') as f:
#     # print(f.read())
#     c_str = 0
#     c_sym = 0
#     for i in f.readlines():
#         c_str+=1
#         print(f'символов: {len(i)}, слов:{len(i.split())} в строке №{c_str} (с учетом "\\n")')



# """
# 2) Создайте файл nums.txt, содержащий несколько чисел, записанных через
# пробел. Напишите программу, которая подсчитывает и выводит на экран
# общую сумму чисел, хранящихся в этом файле.
# """
# with open('nums.txt', 'w+') as f:
#     for i in range(10):
#         f.write(f'{i} ')
#     c = 0
#     f.seek(0)
#     for i in f.read().split():
#         c+=int(i)
#     print(c)



# """
# 3) Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
# записать их произведение в файл output.txt.
# """
# with open('input.txt', 'w+') as f:
#     for i in range(1, 11):
#         f.write(f'{i} ')
#     c = 1
#     f.seek(0)
#     for i in f.read().split():
#         c*=int(i)
#     with open('output.txt', 'w+') as f:
#         f.write(str(c))
#         f.seek(0)
#         print(f.read())



# """
# 6) В файле записаны в целые числа. Найти максимальное и минимальное
# число и записать в другой файл.
# """
# with open('input1.txt', 'r') as f:
#     ls = [int(x) for x in f.read().split()]
#     ls1 = f'max: {max(ls)}\nmin: {min(ls)}'
#     with open('output1.txt', 'w+') as f:
#         f.write(ls1)
#         print(ls1)



# """
# 7) В файле записаны в столбик целые числа. Отсортировать их по
# возрастанию суммы цифр и записать в другой файл.
# """
# with open('input2.txt', 'w+') as f:
#     for i in range(10, 21):
#         if i == 20:
#             f.write(f'{i}')
#         else:
#             f.write(f'{i}\n')
#     f.seek(0)
#     print('старый:')
#     print(f.read())

# with open('input2.txt', 'r') as f:
#     ls = []
#     for line in f.readlines():
#         c = 0
#         for i in line:
#             if i.isdigit():
#                 c+=int(i)
#         ls.append(c)
#     ls.sort()
#     print()
#     print('новый:')

# with open('output2.txt', 'w+') as f:
#     for x in ls:
#         f.write(f'{x}\n')
#     f.seek(0)
#     print(f.read())