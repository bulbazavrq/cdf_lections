# # # # # #1
# # # # # def fnc1(s: str):
# # # # #     b = {'upper': 0, 'lower': 0}
# # # # #     for i in s:
# # # # #         if i.isupper():
# # # # #             b['upper'] = b['upper'] + 1
# # # # #         elif i.islower():
# # # # #             b['lower'] = b['lower'] + 1
# # # # #     # print(f'{b}')
# # # # #     # c = str(list(map(str.replace, f'{b}', ('{', '}'))))
# # # # #     # print(c)
# # # # #     # print(''.join((map(str.replace, f'{b}', ('{', '}')))))
# # # # #     print(f'{b}'.replace('{', '').replace('}', '').replace("'", ''))

# # # # # a = 'sdmaskdMKSDMAKSMDKskadkasmdk2mskf2w222DMsds2222'
# # # # # fnc1(a)

# # # # #2
# # # # def fnc1(n):
# # # #     a = {}
# # # #     for i in range(1, n):
# # # #         a[i] = i**3
# # # #     return a
# # # # print(fnc1(5))

# # # #3
# # # def sum_range(start, end):
# # #     c = 0
# # #     if start > end:
# # #         start1 = start
# # #         start = end
# # #         end = start1
# # #     for i in range(start, end):
# # #         c += i
# # #     print(c)

# # # sum_range(11,7)

# # #4
# # def izogram1(a:str):
# #     return True if len(a) == len(set(a)) else False
# # print(izogram1('helo'))

# #5
# str = 'Money, money, money, it’s always sunny, in the richmen’s world'.lower()
# def func1(a:str):
#     a = a.split()
#     a = [i.replace(',', '') for i in a]
#     b = {}
#     for i in a:
#         if i not in b.keys():
#             b[i] = a.count(i)
#     print(f'{b}'.replace('{', '').replace('}', '').replace("'", ''))
# func1(str)