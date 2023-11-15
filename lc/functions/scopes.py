# # Области видимости и пространство имен (scopes)
# # технология, которая определяет контекст имени, в рамках которого мы можем ее использовать

# # built_ins(Встроенная область видимости) -> print, len...
# # global(Глобальная) -> область одного файла
# # enclosed(не локальная(замкнутая), nonlocal)
# # local(локальная) -> область внутри одной функции

# # x = 200

# # def myFunc():
# #     print(x)
# #     a = 300
# #     print(a)
# #     return a

# # myFunc()
# # print(a)


# # a = 10 # global
# # print # built_in

# # def hello(): # global
# #     a = 'Hello' # local
# #     print(a, 'local inside in func')

# # hello()
# # print(a, 'global')

# # LEGB - local enclosed global built-ins

# # ----------------------------------------------
# # enclosed
# # замкнутое пространство имен - локальное пространство, у которого есть внутреннее (вложение) локальное пространство

# # x = 'global'
# # print(x, '1') # global
 
# # def enclosed(): # global
# #     x = 'enclosed'

# #     def local():
# #         x = 'local'
# #         print(x, '3') # local

# #     print(x, '2') # enclosed
# #     local()
# #     print(x, '4') # enclosed

# # enclosed()
# # print(x, '5') # global


# # global -> позволяет изменять значения глобальной переменной

# # nonlocal -> позволяет изменять значение не локальной (замкнутой) переменной находясь внутри локальной области

# # var = 0

# # def increment(): # LEGB
# #     global var
# #     var += 1 # var = var + 1
# #     print(var)

# # increment()
# # increment()
# # increment()
# # increment()
# # increment()


# # def counter():
# #     num = 0
# #     def increment():
# #         nonlocal num
# #         num += 1
# #         return num
# #     return increment

# # c_steps = counter()
# # c_squats = counter()
# # print(c_steps()) #1
# # print(c_steps()) #2
# # print(c_steps()) #3
# # print(c_steps()) #4
# # print(c_steps()) #5
# # print(c_squats()) #1
# # print(c_squats()) #2
# # print(c_steps()) #6
# # print(c_steps()) #7
# # print(c_steps()) #8

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, walkers):
#     print()
#     print(f'John Snow, ты убил: \n\tгероев: {heroes} \n\tбелых ходоков: {walkers}')
#     print()

# counter_heroes = counter()
# counter_walkers = counter()
# heroes = 0
# walkers = 0

# print('Приветствую вас, Король Севера John Snow, в Игре Престолов!')
# print('Тебе доступны следующие действия:')
# while True:
#     print()
#     print('1-убить героя, 2-убить ходака, 3-статистика, 4-выйти из игры')
#     choice = input('Введите что хотите сделать: ').strip()
#     if choice == '1':
#         heroes = counter_heroes()
#         print('Вы обезглавили Ланистера')
#     elif choice == '2':
#         walkers = counter_walkers()
#         print('Вы убили белого ходока!')
#     elif choice == '3':
#         showStats(heroes, walkers)
#     elif choice == '4':
#         print('Bye, Bye!')
#         break