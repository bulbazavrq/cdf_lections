# # # # # 1) '''Напишите функцию, принимающую на вход длины двух катетов прямо-
# # # # # угольного треугольника и возвращающую длину гипотенузы, рассчитан-
# # # # # ную по теореме Пифагора. В главной программе должен осуществляться
# # # # # запрос длин сторон у пользователя, вызов функции и вывод на экран
# # # # # полученного результата.'''

# # # # def fnc1(a, b):
# # # #     return a**2 + b**2
# # # # a = int(input('a: '))
# # # # b = int(input('b: '))
# # # # print(fnc1(a,b))

# # # # # 2) '''Представьте, что сумма за пользование услугами такси складывается из
# # # # # базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
# # # # # Напишите функцию, принимающую в качестве единственного параметра
# # # # # расстояние поездки в километрах и возвращающую итоговую сумму опла-
# # # # # ты такси. В основной программе должен демонстрироваться результат
# # # # # вызова функции.'''

# # # def fnc1(a):
# # #     return str(4+((a//140)*0.25))+'$'
# # # print(fnc1(1000))

# # # # # 3) '''Интернет-магазин предоставляет услугу экспресс-доставки для части
# # # # # своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
# # # # # последующие. Напишите функцию, принимающую в качестве единствен-
# # # # # ного параметра количество товаров в заказе и возвращающую общую
# # # # # сумму доставки. В основной программе должны производиться запрос
# # # # # количест­ва позиций в заказе у пользователя и отображаться на экране
# # # # # сумма доставки.'''

# # def fnc1(a):
# #     return str(10.95 + ((a - 1) * 2.95))+'$'
# # a = int(input(''))
# # print(fnc1(a))

# # # # # 4) '''Напишите функцию, которая будет принимать на вход три числа в качест­
# # # # # ве параметров и возвращать их медиану. В основной программе должен
# # # # # производиться запрос к пользователю на предмет ввода трех чисел, а так-
# # # # # же вызов функции и отображение результата.'''

# def fnc1(a,b,c):
#     # return (((a**2+c**2)/2)-(b**2/4))*0.5
#     return (((2*a**2)+(2*b**2)-c**2)/4)*0.5 #mediana po "c"
# a=int(input('a: '))
# b=int(input('b: '))
# c=int(input('c: '))
# print(fnc1(a,b,c))

# # # # # 5) '''Используя решения из упражнений 100 и 102, напишите программу, ге-
# # # # # нерирующую случайный надежный пароль и выводящую его на экран.
# # # # # Посчитайте, с какого раза удастся создать пароль, отвечающий нашим
# # # # # требованиям надежности, и выведите на экран количество попыток. Им-
# # # # # портируйте функции из предыдущих упражнений и вызывайте их при
# # # # # необходимости для решения этой задачи.'''

# import random
# import string

# def fnc1():
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for i in range(random.randint(5, 10)))
#     return password

# popykti = 0
# suc = 0 #5

# while suc != 5:

#     suc = 0
#     password = fnc1()
#     ls = '!@#$%^&*()_-+=<>?/1234567890'
#     check = {'Длина': False, 'Специальный символ': False, 'Верхний регистр': False, 'Нижний регистр': False, 'Цифра': False}
    
#     try:
#         for c in password:
#             if len(password) >= 8:
#                 check['Длина'] = True

#             if c.isupper():
#                 check['Верхний регистр'] = True
            
#             if c.islower():
#                 check['Нижний регистр'] = True

#             for c in ls:
#                 if c in password:
#                     check['Специальный символ'] = True
#                 if c in password:
#                     check['Цифра'] = True
#         raise


#     except:
#         print()
#         for k, v in check.items():
#             if v == False:
#                 print(k, 'x')
#             else:
#                 print(k, '✓')
#                 suc+=1
#     popykti+=1

# else:
#     print()
#     print(popykti, 'popytok')

#5.1
def dec(func):
    def wrapper(*args, **kwargs):

        popykti = 0
        suc = 0 #5

        while suc != 5:

            suc = 0
            password = func()
            ls = '!@#$%^&*()_-+=<>?/1234567890'
            check = {'Длина': False, 'Специальный символ': False, 'Верхний регистр': False, 'Нижний регистр': False, 'Цифра': False}
            
            try:
                for c in password:
                    if len(password) >= 8:
                        check['Длина'] = True

                    if c.isupper():
                        check['Верхний регистр'] = True
                    
                    if c.islower():
                        check['Нижний регистр'] = True

                    for c in ls:
                        if c in password:
                            check['Специальный символ'] = True
                        if c in password:
                            check['Цифра'] = True
                raise


            except:
                print()
                for k, v in check.items():
                    if v == False:
                        print(k, 'x')
                    else:
                        print(k, '✓')
                        suc+=1
            popykti+=1

        else:
            print()
            print(popykti, 'popytok')
            return popykti
        
    return wrapper

@dec
def fnc1():
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(random.randint(5, 10)))
    return password

fnc1()