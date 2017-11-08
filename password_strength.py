import re
import string
import getpass


def password_length(password):
    min_length_of_password = 8
    return len(password) >= min_length_of_password


def password_has_numbers(password):
    return any(char.isdigit() for char in password)


def password_has_letters(password):
    return any(char.isalpha() for char in password)


def case_sensitivity(password):
    has_lower = bool(re.search("[a-z]", password))
    has_upper = bool(re.search("[A-Z]", password))
    return bool(has_lower and has_upper)


def has_special_chars(password):
    chars_in_password = set(password)
    return bool(chars_in_password.intersection(string.punctuation))


def get_password_strength(password):
    return sum([
        password_length(password) * 2,
        password_has_numbers(password) * 1,
        password_has_letters(password) * 1,
        case_sensitivity(password) * 3,
        has_special_chars(password) * 3
    ])


if __name__ == '__main__':
    users_password = getpass.getpass("Enter the Password:")
    print(get_password_strength(users_password))
