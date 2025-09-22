import random
import string

def generate_login(cohort_number='1999'):
    # email формата: имяфамилия_номер_трёхцифры@домен
    digits = ''.join(random.choices(string.digits, k=3))
    email = f"testuser_{cohort_number}_{digits}@yandex.ru"
    return email

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))