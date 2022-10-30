import json

data = []
def load_students():
    with open('students.json') as file:
        data.append(json.load(file))
        return data


def num_stud(data):
    ask = input('Введите номер пк студента: ')
    count_ask = 1
    for st_dict in data:
        if int(ask) == st_dict['pk'] and ask.isdigit():
            print(f"Студент {st_dict['full_name']}\nЗнает {', '.join(st_dict['skills'])}")
            set_stud = set(st_dict['skills'])
            return set_stud
        elif ask != st_dict['pk'] and count_ask < len(data):
            count_ask += 1
            continue
        else:
            print("У нас нет такого студента")
            break
num_stud(data)

# def load_professions():
#     with open('professions.json') as file:
#         list_prof = json.load(file)
#         return list_prof
#
#
# def get_profession_by_title():
#     ask = input(f'Выберите специальность для оценки студента: ')
#     count_ask = 1
#     for prof_dict in list_prof:
#         if ask == prof_dict['title']:
#             print(f"\n {', '.join(prof_dict['skills'])}")
#             set_prof = set(prof_dict['skills'])
#             intersec = set_stud.intersection(set_prof)
#             diff = set_prof.difference(set_stud)
#             print(intersec)
#             percent = 100 // len(set_prof) * len(intersec)
#             print(f'Уровень готовности: {percent}%')
#             print(f'Знает {intersec}')
#             print(f'Не знает {diff}')
#             break
#         elif ask != prof_dict['title'] and count_ask < len(list_prof):
#             count_ask += 1
#             continue
#         else:
#             print("У нас нет такой специальности")
#             break



# if __name__ == '__main__':
#     set_stud = set()
#     set_prof = set()
#     data = load_students()
#     list_prof = load_professions()
#     num_stud()
#     get_profession_by_title()



