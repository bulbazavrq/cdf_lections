# #1
# from random import choice
# unique_ls = [f'0{i}id' for i in range(1,100)]
# fncs_id = {}

# def dec(f):
#     def wrapper(*args, **kwargs):
#         print()
#         print(f'{f.__name__}({wrapper.id}):')
#         f(*args, **kwargs)
#         wrapper.count+=1
#         fncs_id[f'Функция {f.__name__} была запущена успешно'] = [wrapper.id, f'Кол-во запусков: {wrapper.count}']
#     wrapper.id = choice(unique_ls)
#     wrapper.count = 0
#     return wrapper

# @dec
# def fnc1():
#     a = 'rabota_fnc1'
#     print(a)
# @dec
# def fnc2():
#     a = 'rabota_fnc2'
#     print(a)

# fnc1()
# fnc2()
# fnc1()
# fnc2()

# print()
# print(fncs_id)


# #2
# # def fnc1(a:str):return ''.join([i[0] for i in a.split()]).upper()
# # print(fnc1('Кыргызская Республика'))
# # print(fnc1('Ruby on Rails'))


# # #3
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