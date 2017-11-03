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
    lower = bool(re.search("[a-z]", password))
    upper = bool(re.search("[A-Z]", password))
    if lower and upper:
        return True
    return False


def has_special_chars(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def get_password_strength(password):
    return sum([password_length(password) * 2, password_has_numbers(password) * 1, password_has_letters(password) * 1,
                case_sensitivity(password) * 3, has_special_chars(password) * 3])


if __name__ == '__main__':
    users_password = getpass.getpass("Enter the Password:")

print(get_password_strength(users_password))
