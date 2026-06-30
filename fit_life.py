WATER_PER_KG = 30  # константа
MILLILITERS_PER_LITER = 100  # константа

user_name = input("Здравствуйте, введите, пожалуйста, ваше имя: ")
user_age = int(input("Введите, пожалуйста, ваш возраст: "))
user_weight = float(input("Введите, пожалуйста, ваш вес(в кг): "))
user_height = float(input("Введите, пожалуйста, ваш рост(например, 2.00): "))
bmi = user_weight / (user_height ** 2)  # расчёт индекса массы тела
bmi = round(bmi, 1)  # округление ИМТ до одного знака после запятой
water_ml = user_weight * WATER_PER_KG  # норма воды в миллилитрах
water_l = water_ml / MILLILITERS_PER_LITER  # переводим в литры норму воды

print(f"\nОтчет для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
