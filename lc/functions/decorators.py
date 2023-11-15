# # # Декораторы - это функция, которая позволяет без изменений кода функции расширить ее функционал


# # # def decorator(func):
# # #     print(f'{func.__name__} была вызвана!')
# # #     func()

# # # def printsPetNames(owner:str='John', **pets: str):
# # #     print(f'Owner name {owner}!')
# # #     print(pets, type(pets), '!!!!!')
# # #     for pet, name in pets.items():
# # #         if type(name) == list:
# # #             print(f'{pet}:', *name)
# # #         else:
# # #             print(f'{pet}: {name}')

# # # decorator(printsPetNames)


# # # pythonic way - @

# # # def decorator(func):
# # #     def wrapper():
# # #         print('decorator worked!')
# # #         print(f'{func.__name__} была вызвана!')
# # #         func()
# # #     return wrapper

# # # @decorator
# # # def get_name():
# # #     print(f'Owner name John Snow!')

# # # get_name()
# # import time

# # def benchmark(func):
# #     def wrapper(*args, **kwargs):
# #         start = time.time() #10:27
# #         func(*args, **kwargs)
# #         finish = time.time() #10:29
# #         print(f'Время выполнения функции: {func.__name__}, заняло: {finish - start}')
# #     return wrapper

# # @benchmark
# # def loop():
# #     i = 0
# #     num = 100_000_000
# #     while i <= num:
# #         i += 1

# # # loop()

# # @benchmark
# # def add(number):
# #     i = 0
# #     ls = []
# #     while i <= number:
# #         ls.append(i)
# #         i += 1


# # @benchmark
# # def printsPetNames(owner: str, **pets: str):
# #     print(f'Owner name {owner}!')
# #     print(pets, type(pets), '!!!!!')
# #     for pet, name in pets.items():
# #         if type(name) == list:
# #             print(f'{pet}:', *name)
# #         else:
# #             print(f'{pet}: {name}')

# # printsPetNames('John Snow', dog='Pluto', cat='Garfild', fish=['Nemo', 'Dori', 'Golden'], turtle='Leonardo')
# # loop()
# # add(100_000_000)

# def bold(func):
#     def wrapper(*args, **kwargs):
#         res = '<bold>' + func(*args, **kwargs) + '</bold>'
#         return res
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         res = '<div>' + func(*args, **kwargs) + '</div>'
#         return res
#     return wrapper

# @div
# @bold
# @div
# def get_name():
#     name = input('Введите свое имя: ')
#     return name

# res = get_name()
# print(res)

# ----------------------------------------------

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'Trace: вызвала {func.__name__}() \nона приняла args: {args}, kwargs: {kwargs}')
        res = func(*args, **kwargs)
        print(f'Trace: вызвала {func.__name__}() \nона  вернула: {res}')
        return res
    return wrapper

@trace
def say(name, address):
    return f'{name} --> {address}'

@trace
def hello(name, last_name, country):
    return f'Hello {name} {last_name} from {country}'

say('Sherlock Holms', 'Bakery Street 221B')
print()
hello(name='Homer', last_name='Simpson', country='Canada')
