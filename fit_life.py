WATER_PER_KG = 30  # константа
MILLILITERS_PER_LITER = 1000  # константа


def bmi(user_weight, user_height):  # расчёт индекса массы тела
    bmi = round((user_weight / (user_height ** 2)), 1)
    return bmi


def water_l(user_weight):  # расчет нормы воды
    water_littrs = user_weight * WATER_PER_KG / MILLILITERS_PER_LITER
    return water_littrs


user_name = input("Введите, пожалуйста, ваше имя: ")
while True:
    try:
        user_age = int(input("Введите, пожалуйста, ваш возраст: "))
        break
    except ValueError:
        print("Ох! Думаю вы не туда нажали. Попробуйте еще раз:")
while True:
    try:
        user_weight = float(input("Введите, пожалуйста, ваш вес(в кг): "))
        break
    except ValueError:
        print("Ох! Думаю вы не туда нажали. Попробуйте еще раз:")
while True:
    try:
        user_height = float(input("Введите ваш рост, например, 2.00: "))
        break  # избавились от "пожалуйста", тк не умещались в кол-во символов
    except ValueError:
        print("Ох! Думаю вы не туда нажали. Введите еще раз, используйте '.':")

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi(user_weight, user_height)}")
print(f"Рекомендуемая норма воды: {water_l(user_weight)} л. в день")
print("-" * 30)
print("Расчет окончен. Будьте здоровы!")