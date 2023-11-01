import random

from string import digits, ascii_letters, punctuation


def generate_password(length: int) -> str:
    numbers = ''.join(random.choice(digits) for _ in range(length))
    numbers_letters = ''.join(random.choice(digits + ascii_letters) for _ in range(length))
    numbers_letters_punctuation = ''.join(random.choice(digits + ascii_letters + punctuation) for _ in range(length))
    return (f'Пароль из цифр: {numbers}\n'
            f'Пароль из букв и цифр: {numbers_letters}\n'
            f'Пароль из букв, цифр и знаков: {numbers_letters_punctuation}')


get_password = generate_password(int(input('Введите количество символов: ')))

if __name__ == '__main__':
    print(get_password)