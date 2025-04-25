from faker import Faker
from random import random
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


def generate_registration_data_without_a_dot_in_an_email():
    # Генерация имени: ровно 8 латинских букв
    name = faker.lexify(text='????????', letters='abcdefghijklmnopqrstuvwxyz').capitalize()

    # Генерация email с гарантированным отсутствием точек в домене
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-'
    local_part = faker.lexify(text='??????????', letters=allowed_chars)

    # Генерируем домен без точек
    domain_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    domain = faker.lexify(text='??????????', letters=domain_chars).lower()

    invalid_email = f"{local_part}@{domain}"

    # Генерация сложного пароля
    password = faker.password(
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    return name, invalid_email, password

def generate_registration_data_with_invalid_email_missing_at():
    name = faker.lexify(text='????????', letters='abcdefghijklmnopqrstuvwxyz').capitalize()

    # Генерация email с гарантированным отсутствием точек в домене
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-'
    local_part = faker.lexify(text='??????????', letters=allowed_chars)

    # Генерируем домен без точек
    domain_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    domain = faker.lexify(text='??????????', letters=domain_chars).lower()

    invalid_email = f"{local_part}.{domain}"

    # Генерация сложного пароля
    password = faker.password(
        length=12,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    return name, invalid_email, password

def generate_registration_data_with_an_invalid_password():
    # Генерация имени: ровно 8 латинских букв
    name = faker.lexify(text='????????', letters='abcdefghijklmnopqrstuvwxyz').capitalize()

    # Генерация email с гарантированным наличием точки в домене
    email = faker.email()
    while '.' not in email.split('@')[1]:
        email = faker.email()

    # Генерация сложного пароля
    password = faker.password(
        length=5,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    return name, email, password