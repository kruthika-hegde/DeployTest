import re

def is_valid_email(email):

    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.fullmatch(pattern, email))


print(is_valid_email("user@domain.com"))  # True
print(is_valid_email("user@domain"))      # False
print(is_valid_email("user.name@domain.com"))  # True
print(is_valid_email("user@domain.co.uk"))     # True
print(is_valid_email("user@domain."))          # False
print(is_valid_email("@domain.com"))           # False