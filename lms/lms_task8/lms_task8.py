# # list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]

# # # def fn1(a:list):
# # #     b = []
# # #     for i in a:
# # #         if type(i) == str:
# # #             i = i.title()
# # #             b.append(i)
# # #     b.sort()
# # #     return b

# # # def fn1(a:list):
# # #     b = []
# # #     for i in a:
# # #         if type(i) == int:
# # #             b.append(i)
# # #     b.sort()
# # #     b.reverse()
# # #     return b

# # def fn1(a:list):
# #     b = []
# #     for i in a:
# #         if type(i) == float:
# #             b.append(i)
# #     return sum(b)


# # print(fn1(list_1))


# ######2
# # sh = ['огурец', 'колбаса']
# # sh1 = ['огурец', 'колбаса', 'хлеб']
# # sh2 = ['огурец', 'колбаса', 'хлеб', 'кетчуп']
# # def sandwich(a:str, b:list):
# #     print(f'{('Большой' if a == 'Большой' else 'Маленький' if a == 'Маленький' else 'Средний')}, {', '.join(b)}')

# # sandwich('Средний', sh)
# # sandwich('Большой', sh2)
# # sandwich('Маленький', sh1)

# ###########33

# def make_car(maker:str, model:str, **kwargs):
#     b = ''
#     for k, y in kwargs.items():
#         c = ''.join(k + ' is ' + y + ', ')
#         b += c
#     ls = f'{maker.title()} {model.title()}, {b}'
#     print(f'{ls[0:-2]}')

# car = make_car('subaru', 'outback', color='blue', engine='V8', horses='200')


#------------44444
# def count_letters():
#     string = input('Введите текст: ')
#     while True:
#         letter = (lambda letter: f'Количество букв {letter}: {string.count(letter)}' if letter in string else f'{letter}: {string.count(letter)}')(input('Какую букву ищем? '))
#         # digit = input('Какую цифру ищем? ')
#         print(letter)
#         # if letter or digit == 'выход':
#         #     break
#         # print(lambda l: '', letter)
#         # print(f'Количество букв {letter}: {string.count(letter)}' if letter in string else f'{letter}: {string.count(letter)}')
#         # print(f'Количество цифр {digit}: {string.count(digit)}' if digit in string else f'{digit}: {string.count(digit)}')
#     # return
# count_letters()
       
# letter = (lambda letter, string: f'Количество букв {letter}: {string.count(letter)}' if letter in string else f'{letter}: {string.count(letter)}')(input('Какую букву ищем? '),input('Введите текст: '))
# while True:print(letter)

########################раб4###########################
# def count_letters():
#     string = input('Введите текст: ')
#     if string == 'выход':
#         return
#     while True:
#         letter = input('Какую букву ищем? ')
#         if letter == 'выход':
#             break
#         digit = input('Какую цифру ищем? ')
#         if digit == 'выход':
#             break
#         print((f'\nКоличество букв {letter}: {string.count(letter)}' if letter in string else f'\nБуква {letter}: не найдена') if letter.isalpha() and len(letter) == 1 else '\nЭто не буква')
#         print((f'Количество цифр {digit}: {string.count(digit)}\n' if digit in string else f'Цифра {digit}: не найдена') if digit.isdigit() and len(digit) == 1 else 'Это не цифра\n')
# count_letters()
########################раб4###########################



############55555
# a = {'Асан': 'Директор', 'Асан1': 'Директор1'}
# def fn1(d:dict):
#     b = ''
#     for k, v in d.items():
#         b += f'Работник {k}, занимает должность {v}\n'
#     return b[0:-1]
# print(fn1(a))

################6666666666
# def calc1():
#     while True:
#         a = input('Число a: ')
#         if 'q' in a:
#             break
#         elif a == '':
#             print('Нет ничего приятнее, чем знание о твоих знаниях!')
#             continue
#         b = input('Число b: ')
#         if 'q' in b:
#             break
#         elif b == '':
#             print('Нет ничего приятнее, чем знание о твоих знаниях!')
#             continue
#         math = input('Тип операции (+, -, /, *): ')
#         if 'q' in math:
#             break
#         elif math == '':
#             print('Нет ничего приятнее, чем знание о твоих знаниях!')
#             continue
#         try:
#             a = float(a)
#             b = float(b)
#             if math=='+':
#                 print(a+b)
#             elif math=='-':
#                 print(a-b)
#             elif math=='/':
#                 if b != 0:
#                     print(a/b)
#                 else:
#                     print('!')
#             elif math=='*':
#                 print(a*b)
#             else:
#                 print('Ошибка')
#         except ValueError:
#             print('calc_ValueError')
#             continue
# def chat_bot1():
#     while True:
#         a = input('message: ')
#         if a == 'q':
#             break
#         elif a == 'calc':
#             calc1()
#         elif len(a) > 1:
#             if a[-1]=='?':
#                 print('Конечно!')
#             elif a.isupper() and a[-1]=='!':
#                 print('Успокойся')
#             else:
#                 print('ну и что')
#         elif a=='':
#             print('Как классно, когда ты молчишь. Продолжай в том же духе!')
#         else:
#             print('ну и что')
# chat_bot1()


########################777777777777
# o = 0
# while True:
#     a = input('Введите число: ')
#     if a == '':
#         break
#     if '.' in a and a.count('.') < 2:
#         a = float(a)
#         o += a
#         print(o)
#     elif a.isdigit():
#         a = int(a)
#         o += a
#         print(o)
#     else:
#         print('Введите корректное число')
#         continue    