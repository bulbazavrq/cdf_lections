# # # # # # # # # # # # # # # # # # # zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает итератор

# # # # # # # # # # # # # # # # # # ls = [1,2,3]
# # # # # # # # # # # # # # # # # # ls2 = [100, 200, 300, 123]

# # # # # # # # # # # # # # # # # # # res = list(zip(ls, ls2))
# # # # # # # # # # # # # # # # # # # print(res)
# # # # # # # # # # # # # # # # # # res = dict(zip(ls, ls2))
# # # # # # # # # # # # # # # # # # print(res)
# # # # # # # # # # # # # # # # # #-----------------------------
# # # # # # # # # # # # # # # # # # all(), any()

# # # # # # # # # # # # # # # # # # all(Iterable) - Возвращает True, если все элементы итерируемого объекта истина, иначе False


# # # # # # # # # # # # # # # # # # ls = [[1,2], 5, 'stroka', True, 1, '']
# # # # # # # # # # # # # # # # # # print(all(ls))

# # # # # # # # # # # # # # # # # ip = '10.255.12.155'
# # # # # # # # # # # # # # # # # ip2 = '10.255.1y.155'

# # # # # # # # # # # # # # # # # result = all(x.isdigit() for x in ip2.split('.'))
# # # # # # # # # # # # # # # # # print(result)

# # # # # # # # # # # # # # # # # any - Возвращает True, если хотябы один элемент истинна

# # # # # # # # # # # # # # # # ls = [0, 0, 0, 0, '.']
# # # # # # # # # # # # # # # # print(any(ls))

# # # # # # # # # # # # # # # ingore = ['rm - rf', 'sudo', 'reset', 'poweroff']
# # # # # # # # # # # # # # # command = input('Vvedite commandu: ')
# # # # # # # # # # # # # # # if any(x in command for x in ingore):
# # # # # # # # # # # # # # #     raise Exception('You dont have permissions!')

# # # # # # # # # # # # # # # print('OK!')

# # # # # # # # # # # # # # # Анонимные функции - lambda(такие же функции только беЗ наЗвания)
# # # # # # # # # # # # # # # lambda функции могут принимать сколько угодно аргументов, но всегда возвращают одно выражение

# # # # # # # # # # # # # # # def sum_of_args(a, b):
# # # # # # # # # # # # # # #     res = a + b
# # # # # # # # # # # # # # #     return res

# # # # # # # # # # # # # # # print(sum_of_args(5,15))

# # # # # # # # # # # # # # func = lambda a, b: a + b
# # # # # # # # # # # # # # print(func(5, 15))
# # # # # # # # # # # # # # print((lambda a, b: a + b)(5,15))

# # # # # # # # # # # # # def myFunc(n):
# # # # # # # # # # # # #     return lambda a: a * n

# # # # # # # # # # # # # myDoubler = myFunc(2)
# # # # # # # # # # # # # myTripler = myFunc(3)

# # # # # # # # # # # # # print(myDoubler(50))
# # # # # # # # # # # # # print(myDoubler(123))
# # # # # # # # # # # # # print(myDoubler(7))
# # # # # # # # # # # # # print(myTripler(55))

# # # # # # # # # # # # dict_ = {'John': 50_000_000, 'Jamie': 100_000, 'Aibek': 1_000_000, 'Aigerim': 15}

# # # # # # # # # # # # res = sorted(dict_.items(), key=lambda x:x[1])
# # # # # # # # # # # # print(res)

# # # # # # # # # # # #---------------------------------------------
# # # # # # # # # # # # map(function, iterable) -> применяет ко всем элементам iterable функцию которую мы передаем

# # # # # # # # # # # ls = ['one', 'two', 'three', 'four', 'five']
# # # # # # # # # # # res = list(map(str.upper, ls))
# # # # # # # # # # # print(res)

# # # # # # # # # # # for i in range(len(ls)):
# # # # # # # # # # #     ls[i] = ls[i].upper()
# # # # # # # # # # # print(ls)

# # # # # # # # # # names = ['John', 'Sultan', 'Jamie', 'Raychel', 'Aibek']

# # # # # # # # # # # def func(name):
# # # # # # # # # # #     return f'Hello mr/mrs {name}!'

# # # # # # # # # # res = list(map(lambda name: f'Hello mr/mrs {name}!', names))
# # # # # # # # # # print(res)

# # # # # # # # # # # # for i in range(len(names)):
# # # # # # # # # # # #     names[i] = func(names[i])
# # # # # # # # # # # res = []
# # # # # # # # # # # for name in names:
# # # # # # # # # # #     res.append(func(name))
# # # # # # # # # # # print(names)
# # # # # # # # # # # print(res)

# # # # # # # # # dict_ = {1:2, 3:4, 5:6}
# # # # # # # # #         # {1:'2', 3:'4', 5:'6'}

# # # # # # # # # res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# # # # # # # # # print(res)


# # # # # # # # # filter(fucntion, iterable) -> применяет ко всем элементам iterable функцию которую мы передали и возващает итератор с теми элементами для которых функция вернула True

# # # # # # # # ls = ['one', 'two', '', 'list', '100', '1', 'john']
# # # # # # # # # res = []
# # # # # # # # # for x in ls:
# # # # # # # # #     if x.isdigit():
# # # # # # # # #         res.append(x)
# # # # # # # # # print(res)
# # # # # # # # res = list(filter(str.isdigit, ls))
# # # # # # # # print(res)

# # # # # # # ls = ['john', 'codify', 'aibek', 'ono', 'bootcamp', 'Kyrgyzstan', 'mountains']
# # # # # # # print(list(filter(lambda x: len(x)>5, ls)))



# # # # # # ls = [
# # # # # #     {'name': 'Python', 'point':10},
# # # # # #     {'name': 'C++', 'point': 6},
# # # # # #     {'name': 'JS', 'point': 8},
# # # # # #     {'name': 'JAVA', 'point': 3},
# # # # # #     {'name': 'C#', 'point': 0},
# # # # # # ] # >7
# # # # # # b = list(filter(lambda x: x['point'] > 7       ,ls))
# # # # # # print(b)

# # # # # users = [

# # # # #     {'username': 'John', 'comments': ['I love you', 'Really good']},
# # # # #     {'username': 'Raychel', 'comments': []},
# # # # #     {'username': 'Steven', 'comments': ['Bishkek', 'Python']},
# # # # #     {'username': 'Hello', 'comments': []},
# # # # #     {'username': 'Kira', 'comments': ['The best post']},
# # # # # ]
# # # # # print(list(filter(lambda x: x['comments'], users)))
# # # # # print(list(filter(lambda x: not x['comments'], users)))

# # # # ######________________________________________
# # # # names = ['Raychel', 'Sultan', 'Aigerim', 'John', 'Kira', 'Bob']
# # # # new_names = list(
# # # #     map(lambda x: f'Hello Mr/Mrs {x}', filter(lambda x: len(x) > 5, names))
# # # # )
# # # # print(new_names)

# # # #####_____________________________________
# # # # enumerate - она пронумеровывает каждый элемент внутри iterable, её собственным индексом

# # # ls = ['one', 'two', 'three', 'four', 'five']
# # # # res = list(enumerate(ls, 1))
# # # # print(res)
# # # for i, x in enumerate(ls):
# # #     print(f'index: {i}, element: {x}')

# # #__________________________________________________
# # # Функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# # # 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# # # 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не появятся элементы.

# # from functools import reduce

# # ls = [1,2,3,4,5]
# # sum_ = reduce(lambda a,b: a+b, ls)
# # res = reduce(lambda a,b: a*b, ls)
# # print(sum_, res)

# #____________________________________________________________


# # # # # # # # #TODO repeat
# from itertools import repeat

# for x in repeat(lambda x: x*5, 5):
#     print(x(7))

from itertools import repeat
from random import choices
from string import ascii_letters, digits
from statistics import mean

symbols = '_()$!%+-@#'
q_pass = int(input('Vvedite kolichestvo paroley: '))
result = {
    f(choices(ascii_letters, k=10), choices(digits, k=5), choices(symbols, k=2))
    for f in repeat(lambda a,d,s: ''.join(set(a+d+s)), q_pass)
    }
print(result)
print(f'Quantity of passwords: {len(result)}')
dlina = [len(x) for x in result]
print(f'average len: {mean(dlina)}')