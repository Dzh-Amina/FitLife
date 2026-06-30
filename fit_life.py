WATER_PER_KG = 30  # константа
MILLILITERS_PER_LITER = 1000  # константа

user_name = input("Здравствуйте, введите, пожалуйста, ваше имя: ").strip()
while True:
    try:
        user_age = int(input("Введите, пожалуйста, ваш возраст: "))
        break
    except ValueError:
        print("Ох! Думаю вы не туда нажали. Попробуйте еще раз:")
while True:
    try:
        user_weight = int(input("Введите, пожалуйста, ваш вес(в кг): "))
        break
    except ValueError:
        print("Ох! Думаю вы не туда нажали. Попробуйте еще раз:")
while True:
    try:
        user_height = float(input("Введите ваш рост, например, 2.00: "))
        break  # избавились от "пожалуйста", тк не умещались в кол-во символов
    except ValueError:
        print("Ох! Думаю вы не туда нажали. Введите еще раз, используйте '.':")
bmi = round((user_weight / (user_height ** 2)), 1)  # расчёт индекса массы тела
water_ml = user_weight * WATER_PER_KG  # норма воды в миллилитрах
water_l = water_ml / MILLILITERS_PER_LITER  # переводим в литры норму воды

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print("-" * 30)
print("Расчет окончен. Будьте здоровы!")
