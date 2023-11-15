#1
# password = input('''
# Введите пароль подходящий следующим требованиям:
# 1. Длина пароля должна быть не менее 8 символов.
# 2. Пароль должен содержать хотя бы одну заглавную букву (A-Z).
# 3. Пароль должен содержать хотя бы одну строчную букву (a-z).
# 4. Пароль должен содержать хотя бы одну цифру (0-9).
# 5. Пароль должен содержать хотя бы один специальный символ из множества:\n!@#$%^&*()_-+=<>?/
#                                         ''')
# ls = '!@#$%^&*()_-+=<>?/1234567890'
# check = {'Длина': False, 'Специальный символ': False, 'Верхний регистр': False, 'Нижний регистр': False, 'Цифра': False}

# try:
#     for c in password:
#         if len(password) >= 8:
#             check['Длина'] = True

#         if c.isupper():
#             check['Верхний регистр'] = True
        
#         if c.islower():
#             check['Нижний регистр'] = True

#         for c in ls:
#             if c in password:
#                 check['Специальный символ'] = True
#             if c in password:
#                 check['Цифра'] = True
#     raise

# except:
#     for k, v in check.items():
#         if v == False:
#             print(k, 'x')
#         else:
#             print(k, '✓')



#2
# a = [1, 'two', 3, 0]

# try:
#     print(a[4] + 1)
# except IndexError:
#     print('IndexError')

# try:
#     print(int(a[1]))
# except ValueError:
#     print('ValueError')

# try:
#     print(a[2] / a[3])
# except ZeroDivisionError:
#     print('ZeroDivisionError')



#3
# a = {'Igor': 11, 'Igor2': 22, 'Igor3': 33}
# b = input('Igor? ')

# try:
#     print(a[b])
# except KeyError:
#     print('Ne Igor!')