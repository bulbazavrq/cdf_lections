hidden_number = 100
black_list = ['Нурсултан', 'Вероника', 'Айкена']
user_name = input('Введите свое имя: ').title()

if user_name in black_list:
    raise  NameError(f"{user_name}, ты не являешься студентом, тебе данной програмой - игрой пользоваться нельзя!")
else:
    print('Угадай число!')
while True:
    user_number = int(input('Введите число: '))
    difference = abs(hidden_number - user_number)

    if difference == 0:
        print('Ура, ты угадал!')
        break

    elif difference < 10:
        print('Ты был очень близок')

    elif difference >= 10:
        if difference < 50:
            print("Ты был не совсем далек")
        else:
            print('Ты очень далеко')

        