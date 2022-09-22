import json
import re


def extract_data():
    with open('students') as file:
        list_dict = json.load(file)
        return list_dict


def num_stud(list_dict):
    count_ask = 1
    for st_dict in list_dict:
        if int(ask) == st_dict['pk']:
            if re.fullmatch(r"(?=.*\d)(?=.+[A-Z])(?=.*[a-z])(?=.*[\W|_])(?=^[^A-Z])(?=.+[a-zA-Z\d]$).{4,}", st_dict['login']):
                print('Логин верный!')
                print(f"Студент {st_dict['full_name']}\nЗнает {', '.join(st_dict['skills'])}")
                set_stud = set(st_dict['skills'])
                return set_stud
            else:
                print('Логин введен не верно!')
        elif ask != st_dict['pk'] and count_ask < len(data):
            count_ask += 1
            continue
        else:
            print("У нас нет такого студента")
            break


extract_data()
data = extract_data()
ask = input('Введите номер пк студента: ')
num_stud(data)
