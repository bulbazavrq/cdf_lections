# # 1) '''Напишите декоратор, который проверяет, что функция вызывается с определенными типами аргументов.'''

# # def dec(func):
# #     def wrapper(*args, **kwargs):
# #         for i in args:
# #             if type(i) == dict:
# #                 print(True)
# #             else:
# #                 print(False)
# #     return wrapper

# # @dec
# # def f(*args, **kwargs):   
# #     pass
# # f({1: 2, 4: 5}, 5, 12, {'asdasd':'asd'})

# #
# # def dec(f):
# #     def dec(*args:)





# # 2) '''Создайте декоратор, который автоматически преобразует результат функции в другой тип данных,'''

# # def dec(f):
# #     def wrapper(*args, **kwargs):
# #         a = int(f())
# #         return a
# #     return wrapper

# # @dec
# # def fnc1():
# #     return '100'

# # print(fnc1(), type(fnc1()))


# # # 3) '''Реализуйте декоратор, который ограничивает максимальное количество вызовов функции.'''
# # #1
# # from random import choice
# # unique_ls = [f'0{i}id' for i in range(1,100)]
# # fncs_id = {}

# # # print(float('inf')-float('-inf'))
# # # print(float('inf') > 999999999999999999999999999999)

# # def max_r1(max=float('inf')):

# #     def dec(f):

# #         def wrapper(*args, **kwargs):

# #             wrapper.max_r = max
# #             fncs_id[f'Функция {f.__name__} была запущена успешно'] = [wrapper.id, f'Кол-во запусков: {wrapper.count}']
# #             print()
# #             if wrapper.count < wrapper.max_r:
# #                 print(f'{f.__name__}({wrapper.id}):')
# #                 wrapper.count+=1
# #                 f(*args, **kwargs)
# #             else:
# #                 print(f'{f.__name__}({wrapper.id}): достигла максимума')
# #         wrapper.max_r = 0
# #         wrapper.id = choice(unique_ls)
# #         wrapper.count = 0
# #         return wrapper
# #     return dec


# # @max_r1(0)
# # def fnc1():
# #     a = 'rabota_fnc1'
# #     print(a)

# # @max_r1(2)
# # def fnc2():
# #     a = 'rabota_fnc2'
# #     print(a)

# # fnc1() #1
# # fnc2() #1

# # fnc1() #2
# # fnc2() #2

# # fnc2() #3
# # fnc2() #4

# # fnc1() #3
# # fnc1() #4

# # print()
# # print(fncs_id)



# # 4) '''Напишите декоратор, который автоматически логирует исключения, возникающие внутри функции.'''
# # log1 = []
# # def dec(f):
# #     def wrapper(*args, **kwargs):
# #         try:
# #             f()
# #         except TypeError:
# #             print('Что-то пошло не так...')
# #             log1.append('TypeError')
# #     return wrapper
# # @dec
# # def func1(a):
# #     print(a + 1)
# # func1('1')
# # print(log1)

# # 5) '''Создайте декоратор, который выполняет аутентификацию пользователя перед вызовом функции.'''

# # def dec(f):
# #     def wrapper(*args, **kwargs):
# #         a = input('name: ')
# #         print(f'Пользователь {a} выполнил:')
# #         f()
# #     return wrapper
# # @dec
# # def fnc1():
# #     print('chto-to...')
# # fnc1()

# # 6) '''Реализуйте декоратор, который изменяет значение возвращаемого результата функции, например, умножая его на определенный коэффициент.'''

# # def dec(f):
# #     def wrapper(*args, **kwargs):
# #         return f() * 1.5
# #     return wrapper

# # @dec
# # def fnc1():
# #     return 100

# # print(fnc1(), type(fnc1()))

# # 7) '''Напишите декоратор, который ограничивает доступ к функции только определенным пользователям или ролям.'''


# # def dec(f):
# #     def wrapper(*args, **kwargs):
# #         sudo_ls = {'users': ['leo1', 'leo2', 'mega_leo'], 'roles': ['admin1', 'admin2']}
# #         a = 0
# #         for i in args:
# #             for k, v in sudo_ls.items():
# #                 if i in v:
# #                     a += 1
# #         if a > 0:
# #             f(*args, **kwargs)

# #     return wrapper

# # @dec
# # def fnc1(user, role):
# #     print('go')

# # fnc1('admin1', 'leo1')

# # 8) '''Создайте декоратор, который преобразует аргументы функции в определенный формат перед её выполнением, например, в строку в верхнем регистре.'''

# # def dec(f):
# #     def wrapper(*args, **kwargs):
# #         list(args)
# #         args = [i.upper() for i in args]
# #         print(args)
# #         f(*args, **kwargs)
# #     return wrapper

# # @dec
# # def fnc1(a:str):
# #     print(a)
# # fnc1('chelovek')



# ##################################hzhzhzhz####################################
# ##################################hzhzhzhz####################################
# ##################################hzhzhzhz####################################
# # -9) '''Напишите декоратор, который устанавливает максимальное время выполнения функции и завершает её, если оно превышено.'''
# import time
# import signal
# def benchmark(func):
#     def wrapper(*args, **kwargs):
        
#         for _ in range(1):
#             start = time.time() #10:27
#             print()
#             print('loop start')
#             try:
#                 # a = signal.alarm(0)
#                 # print(signal.alarm(9))
#                 # signal.default_int_handler(9,1)
#                 # signal.getsignal('sd')
#                 # print(signal.ITIMER_REAL())
#                 # signal
#                 # signal.pause()
#                 # signal.
#                 # signal.alarm(1)
#                 # signal.getitimer()
#                 # signal.getsignal(_)
#                 # a = signal.alarm(10)
#                 # signal.alarm(10)
#                 # print(a)
#                 # signal.alarm(5)
#                 # signal.signal(2)
#                 # signal.alarm(5)
#                 # print(signal.ITIMER_REAL)
#                 signal.
#                 func(*args, **kwargs)
#                 # print(signal.ITIMER_REAL)
#                 # signal.alarm(0)
#                 # print(signal.alarm(0))
#                 # signal.alarm(3)
#                 # signal.alarm(0)
#                 # print(a, 'a')
#             except:
#                 print( 'except rab')
#             # while func():
#             #     print(1)
#             print('loop end')
#             finish = time.time() #10:29
#             res = finish - start
#         if res > 1:
#             print()
#             print('bolshe 1 sek')
#         print(f'Время выполнения функции: {func.__name__}, заняло: {finish - start}')
        
#     return wrapper

# @benchmark
# def loop():
#     i = []
#     while len(i) < 30_000_000:
#         i.append('*')
# loop()

# # for i in range(3):
# #     loop()




# # #1
# # from random import choice
# # unique_ls = [f'0{i}id' for i in range(1,100)]
# # fncs_id = {}

# # # print(float('inf')-float('-inf'))
# # # print(float('inf') > 999999999999999999999999999999)

# # def max_r1(max=float('inf')):

# #     def dec(f):

# #         def wrapper(*args, **kwargs):

# #             wrapper.max_r = max
# #             fncs_id[f'Функция {f.__name__} была запущена успешно'] = [wrapper.id, f'Кол-во запусков: {wrapper.count}']
# #             print()
# #             if wrapper.count < wrapper.max_r:
# #                 print(f'{f.__name__}({wrapper.id}):')
# #                 wrapper.count+=1
# #                 f(*args, **kwargs)
# #             else:
# #                 print(f'{f.__name__}({wrapper.id}): достигла максимума')
# #         wrapper.max_r = 0
# #         wrapper.id = choice(unique_ls)
# #         wrapper.count = 0
# #         return wrapper
# #     return dec


# # @max_r1(0)
# # def fnc1():
# #     a = 'rabota_fnc1'
# #     print(a)

# # @max_r1(2)
# # def fnc2():
# #     a = 'rabota_fnc2'
# #     print(a)

# # fnc1() #1
# # fnc2() #1

# # fnc1() #2
# # fnc2() #2

# # fnc2() #3
# # fnc2() #4

# # fnc1() #3
# # fnc1() #4

# # print()
# # print(fncs_id)

# ##################################hzhzhzhz####################################
# ##################################hzhzhzhz####################################
# ##################################hzhzhzhz####################################



# # 10) '''Напишите декоратор, который ограничивает доступ к функции только в определенное время суток.'''

# # from datetime import datetime
# # # print(datetime.now().hour)
# # def dec(func):
# #     def wrapper(*args, **kwargs):
# #         print('asdfghfklfdjgfd')
# #         func()
# #         func()
# #         func()
# #         if datetime.now().hour > 10 and datetime.now().hour < 19:
# #             print('decor srabotal', func())
# #         else:
# #             print('ne rab')
# #     return(wrapper)

# # @dec
# # def fn1():
# #     print('rab')

# # fn1()

# # #UDDDUDUU
# # # shagi2 = [-1, 1, -1, -1, -1, 1, 1, -1, 1, 1]
# # # d = 0
# # # g = 0

# # # c = shagi2[0]
# # # for i in shagi2:

# # # # c = shagi1[0]
# # # # for i in shagi1:

# # #     if c > 0:
# # #         g += 1
# # #         # d -= 1
# # #     elif c < 0:
# # #         d += 1
# # #         # g += 1
# # #     c += i
# # # print(d, 'dol')
# # # print(g, 'gor')
# # # dol = 0
# # # print(sum(shagi2))
# # # while True:
# # shagi1 = [1, -1, -1, -1, 1, -1, 1, 1]
# # shagi2 = [-1, 1, -1, -1, -1, 1, 1, -1, 1, 1]
# # tochki = 0
# # c = 0
# # for i in shagi1:
# #     c = c + i
# #     if i == -1:
# #         continue
# #     if c == 0:
# #         tochki +=1
    
        
# # print(tochki)
# # # # c = 0
# # # t = 1
# # # # a = sum([i for i in shagi2 if i == 0 t+1 else t + 0 ])
# # # a = 0
# # # for i in shagi2:
# # #     print(a, 'a')
# # #     if a > 0:
# # #         t = t + 1
# # #     else:
# # #         t = t + 0
# # #     a = a + (i)
# # #     print(a, 'a')
# # # print(t, 't')





# ######4390586uierkfdjnbv


# # def benchmark(func):
# #     def wrapper(*args, **kwargs):
        
# #         for _ in range(1):
# #             start = time.time() #10:27
# #             func(*args, **kwargs)
# #             finish = time.time() #10:29
# #             res = finish - start
# #         if res > 1:
# #             print('12345')
# #         print(f'Время выполнения функции: {func.__name__}, заняло: {finish - start}')
# #     return wrapper

# # @benchmark
# # def loop():
# #     i = 0
# #     num = 100_000_000
# #     while i <= num:
# #         i += 1
# #         print(i)

# # loop()