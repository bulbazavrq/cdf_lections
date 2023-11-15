# def chat_bot1(a: str=''):
#     if len(a) > 1:
#         if a[-1]=='?':
#             print('Конечно!')
#         elif a.isupper() and a[-1]=='!':
#             print('Успокойся')
#         else:
#             print('ну и что')
#     elif a=='':
#         print('Как классно, когда ты молчишь. Продолжай в том же духе!')
#     else:
#         print('ну и что')

# while True:
#     l = input('message: ')
#     if l == 'q':
#         break
#     chat_bot1(l)

##################################################################

# def izogram1(a:str):
#     return True if len(a) == len(set(a)) else False
# print(izogram1('helo'))

##################################################################

# str = 'Money, money, money, it’s always sunny, in the richmen’s world'.lower()
# def func1(a:str):
#     a = a.split()
#     a = [i.replace(',', '') for i in a]
#     b = {}
#     for i in a:
#         if i not in b.keys():
#             b[i] = a.count(i)
#     print(b)
# func1(str)
# надо вывести без {скобок}?