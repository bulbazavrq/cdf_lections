# # # # # Работа с файлами

# # # # # Каретка - Указатель - Курсор

# # # # # open(<путь до файла>)

# # # # # file = open('files.py') # Относительный путь
# # # # # ~ working -> Desktop/bootcamp.05/files/lections/files.py
# # # # # files -> lections/files.py

# # # # # file = open('/Users/commieloliqq/Documents/cdfy/pybc05/lc/files/lections/files.py') # Абсолют
# # # # # base_dir = '/Users/commieloliqq/Documents/cdfy/pybc05/lc/files/'
# # # # # file = open(base_dir + 'lections/files.py')

# # # # # file = open('files.py')
# # # # # data = file.read()
# # # # # print(data, type(data))
# # # # # file.close()

# # # # # Режимы работы с файлами
# # # # # 1. r/r+/rb -> read - для чтения файлов
# # # # # 2. w/w+/wb -> write - для записи данных
# # # # # 3. a/a+ -> для добавления данных
# # # # # b, x -> b - бинарный, x -> создать если его нету


# # # # # file = open('test.txt')
# # # # # print(file.read())
# # # # # file.close

# # # # # file = open('test.txt')
# # # # # print(file.readlines())
# # # # # file.close

# # # # file = open('test.txt')
# # # # print(file.readline())
# # # # print(file.readline())
# # # # print('!!!!!')
# # # # print(file.read())
# # # # file.close


# # # # file.tell() - Возвращает индекс где находится курсор (указатель)
# # # # file.seek() - Перемещает курсор на индекс который вы передали


# # # file = open('test.txt', 'r')
# # # print(file.tell()) # 0
# # # data = file.read()
# # # print(data, '!!!')
# # # print(file.tell()) # 275
# # # file.seek(0)
# # # print(file.tell()) # 0
# # # print(file.read())
# # # print(file.tell())
# # # file.close()


# # # контекстный менеджер 
# # with open('test.txt', 'r') as file: # file = open()
# #     data = file.read()
# #     print(data)
# #     print(file, 'inside')

# # print(file.read(), 'outside')


# with open('test.txt', 'w') as file:
#     file.write('Pervaya stroka!\n')
#     file.write('He is bastard of Ned Stark!\n')
#     file.write('This is lection about files!\n')
#     # file.seek(0)
#     data = ['Test 1 stroka!\n', 'Test 2 stroka!']
#     file.writelines(data)

# with open('test.txt', 'a+') as f:
#     f.seek(0)
#     f.write('\nJohn Snow is King of North!')
#     f.write('\nYou know nothing John Snow!')
#     f.seek(0)
#     print(f.read())

# --------------------------------------------
from PIL import Image
import pytesseract
import re

base_url = '/Users/commieloliqq/Documents/cdfy/pybc05/lc/files/lections/'

def get_imei_code(image: str):
    string = pytesseract.image_to_string(image)
    # print(string)
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    # print(list_of_imei)

    with open('imei_codes.txt', 'w') as file:
        file.writelines(f'{x}\ngag' for x in list_of_imei)
        # for x in list_of_imei:
        #     file.write(f'{x}\n')

image = base_url + 'imei.jpg'
get_imei_code(image)