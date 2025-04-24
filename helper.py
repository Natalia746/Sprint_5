from faker import Faker

faker = Faker()


def generate_registration_data():
    # Генерация имени: ровно 8 латинских букв
    name = faker.lexify(text='????????', letters='abcdefghijklmnopqrstuvwxyz').capitalize()

    # Генерация email с гарантированным наличием точки в домене
    email = faker.email()
    while '.' not in email.split('@')[1]:
        email = faker.email()

    # Генерация сложного пароля
    password = faker.password(
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    return name, email, password