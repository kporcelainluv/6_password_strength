import re
import sys


def enter_password(filepath):
    password = filepath
    return password


# check the length of password
def password_length(password):
    return len(password) >= 8


# check for numbers
def password_has_numbers(password):
    return any(char.isdigit() for char in password)


# check for letters
def password_has_letters(password):
    return any(char.isalpha() for char in password)


# check if password has upper and lower case
def case_sensitivity(password):
    lower = re.compile(r'.*[a-z]+')
    upper = re.compile(r'.*[A-Z]+')
    if lower.match(password) and upper.match(password):
        return True
    else:
        return False


# check if password has special charactes
def has_special_chars(password):
    list_of_special_symbols = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
    for char in password:
        if list_of_special_symbols.find(char) >= 1:
            return True
        else:
            return False


def get_password_strength(password):
    level_of_strength = 2
    if password_length(password):
        level_of_strength += 2
    if password_has_numbers(password):
        level_of_strength += 1
    if password_has_letters(password):
        level_of_strength += 1
    if case_sensitivity(password):
        level_of_strength += 2
    if has_special_chars(password):
        level_of_strength += 2
    return level_of_strength


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]

print(get_password_strength(enter_password(filepath)))
