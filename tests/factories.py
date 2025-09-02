from faker import Faker

fake = Faker('ru-RU')


def make_random_user():
    """
    Возвращает словарь с случайно сгенерированными данными.
    """
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'address': fake.address()
    }
