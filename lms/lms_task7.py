# def summa_n():
#     while True:
#         n= input('n ')
#         if n == 'exit':
#             break
#         r = 0; n = int(n)
#         for i in range(n+1):
#             r = r + i
#         print(f'Я знаю, что сумма чисел от 1 до {n} равна {r}')
# summa_n()


#2
# def test(a:int): print('Положительное' if a > 0 else 'Отрицательное')
# test(-10)

# def positive(): 
#     print('Положительное')
# def negative():
#     print('Отрицательное')
# def test(a: int):
#     return positive() if a > 0 else negative()
# test(11)


#3
# a = {'circle': 4, 'rectangle': [3, 4], 'triangle': (5, 6)}

# def s_circle(a: int=a['circle']):return 3.14 * a**2
# def s_rectangle(a: list=a['rectangle']):return a[0] * a[1]
# def s_triangle(a: tuple=a['triangle']):return (a[0]*a[1])/2

# b = {'circle': s_circle(), 'rectangle': s_rectangle(), 'triangle': s_triangle()}
# c = input('circle(r=4), rectangle(a=3,b=4), triangle(b=5,h=6)? ')

# print(b[c] if c in a.keys() else '?')


#4
# def rev_n(a:int):return int(str(a)[::-1])
# print(rev_n(12345))

# def rev_n():
#     while True:
#         a = input('chislo: ')
#         if a == '0':
#             break
#         print(a[::-1])
# rev_n()


#5
# kucha = {'1': 3, '5': 6, '10': 7, '50': 2, }
# def spec_ustroistvo(a:dict):
#     r = 0
#     for k, v in a.items():
#         print(f'Монет по {k} копейке: {v}')
#         r += (int(k)*v)
#     print(f'Всего у нас {r/100} рубля')
# spec_ustroistvo(kucha)


#6
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

#         a = float(a)
#         b = float(b)
        
#         if math=='+':
#             print(a+b)

#         elif math=='-':
#             print(a-b)

#         elif math=='/':
#             if b != 0:
#                 print(a/b)
#             else:
#                 print('!')

#         elif math=='*':
#             print(a*b)

#         else:
#             print('Ошибка')
# calc1()