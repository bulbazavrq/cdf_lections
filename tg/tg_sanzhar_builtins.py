"""
1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
"""
# list_ = [1, 2, 3, 4]
# print(sum(list_))
"""
2) Дан списка из чисел. Проверьте, что все числа больше трёх.
"""
# list_ = [1, 2, 3, 4]
# print(all(x > 3 for x in list_))
"""
3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.
"""
# list_ = [1,2,3,-4]
# print(any(x < 0 for x in list_))
"""
4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
"""
# list_ = [1,2,3,-4]
# print([x*x for x in list_])
# print(list(map(lambda x: x*x, list_)))
"""
5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
"""
# list_ = [1,2,3,-4]
# print( list( filter( lambda x: x if x%2==0 else None, list_) ) )
"""
6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
"""
# list_ = ['1','fghjkfghj2','3','-4']
# print( list( filter( lambda x: len(x) > 7, list_) ) )
"""
7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
"""
# from functools import reduce
# list_ = [5, 6, 7, 8]
# print(reduce(lambda a,b: a*b, list_))
"""
😍 Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
"""
# ls = [1,2,3,4,5]
# print( 'even:', (list(map((lambda x: 'even' if x % 2 == 0 else 'odd'), ls))).count('even'), '\nodd:', (list(map((lambda x: 'even' if x % 2 == 0 else 'odd'), ls))).count('odd') )
"""
9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True .
"""
# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# print(list(map(lambda a: True if a>0 else False if a < 0 else 'hahaha 0', list_)))
"""
10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
"""
# from functools import reduce
# list_ = ['Andew', 'Alishonktoni', 'Herobrine', 'Sanya']
# print(reduce(lambda a,b: a if len(a) > len(b) else b, list_))