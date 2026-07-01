WATER_PER_KG = 30  # константа
MILLILITERS_PER_LITER = 1000  # константа


def bmi(user_weight, user_height):
    """расчёт индекса массы тела"""
    return round((user_weight / (user_height ** 2)), 1)


def water_l(user_weight):
    """расчет нормы воды"""
    return user_weight * WATER_PER_KG / MILLILITERS_PER_LITER


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

bmi_value = bmi(user_weight, user_height)
water_value = water_l(user_weight)

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi_value}")
print(f"Рекомендуемая норма воды: {water_value} л. в день")

print("-" * 30)
print("Расчет окончен. Будьте здоровы!")
