#file_name/path
f_name = 'to_do_list.txt'

#add task
def n_task(f):
    try:    
        with open (f, 'r') as file:
            f2 = file.readlines()
    except FileNotFoundError:
        with open(f, 'w'): pass
        
    with open(f, 'w+') as file:
        a = input('new task: ')
        count = 1 
        for i in f2:
            if i == '\n':
                continue
            file.writelines(f'{i}')
            file.read()
            count+=1
        file.writelines(f'\n{a}')

#check tasks
def c_task(f):
    try:    
        with open (f, 'r') as file:
            f2 = file.readlines()
    except FileNotFoundError:
        with open(f, 'w'): pass
        

    with open(f, 'w+') as file:
        file.write('')
        count = 1 
        for i in f2:
            if i == '\n':
                continue
            file.writelines(f'{i}')
            file.read()
            count+=1

    with open(f, 'r') as file:
        print('tasks: ')
        c = 1
        for i in file.readlines():
            print(c, i.replace('\n', ''))
            c+=1
        print()

#del task
def d_task(f):
    try:    
        with open (f, 'r') as file:
            f2 = file.readlines()
    except FileNotFoundError:
        with open(f, 'w'): pass
        

    with open(f, 'w+') as file:
        b = int(input('del task: ')) 
        count = 1 
        for i in f2:
            if i == '\n':
                continue
            if count != b:
                file.writelines(f'{i}')
            file.read()
            count+=1

# #refresh tasks
# def r_task(a:bool, f):
#     if a == False:
#         try:    
#             with open (f, 'r') as file:
#                 f2 = file.readlines()
#         except FileNotFoundError:
#             with open(f, 'w'): pass
#         with open(f, 'w+') as file:
#             file.write('')
#             count = 1 
#             for i in f2:
#                 if i == '\n':
#                     continue
#                 file.writelines(f'{i}')
#                 file.read()
#                 count+=1

#     elif a == False:
#         try:    
#             with open (f, 'r') as file:
#                 f2 = file.readlines()
#         except FileNotFoundError:
#             with open(f, 'w'): pass
#         with open(f, 'w+') as file:
#             file.write('')
#             count = 1 
#             for i in f2:
#                 if i == '\n':
#                     continue
#                 file.writelines(f'{count} {i}')
#                 file.read()
#                 count+=1


#start code
def u_start():
    # r_task(True, f_name)
    while True:
        print()
        u_act = input('''
n - new task
c - check tasks
d - del task
                      
                    ''')
        print()


        if u_act == 'n':
            c_task(f_name)
            n_task(f_name)

        elif u_act == 'c':
            c_task(f_name)

        elif u_act == 'd':
            c_task(f_name)
            d_task(f_name)

        else:
            break
    # r_task(False, f_name)
u_start()

