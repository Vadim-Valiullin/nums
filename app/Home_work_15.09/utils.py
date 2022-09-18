import json

def load_students():
    with open('students.json') as file:
        data = json.load(file)
        return data

def num_stud():

    count_ask = 1
    for st_dict in data:
        if int(ask) == st_dict['pk']:
            print(f"Студент {st_dict['full_name']}\nЗнает {', '.join(st_dict['skills'])}")
            set_stud = set(st_dict['skills'])
            return set_stud
        elif ask != st_dict['pk'] and count_ask < len(data):
            count_ask += 1
            continue
        else:
            print("У нас нет такого студента")
            break


def load_professions():
    with open('professions.json') as file:
        list_prof = json.load(file)
        return list_prof


def get_profession_by_title(set_stud):

    count_ask = 1
    for prof_dict in list_prof:
        if answer == prof_dict['title']:
            # print(f"\n {', '.join(prof_dict['skills'])}")
            set_prof = set(prof_dict['skills'])
            intersec = set_stud.intersection(set_prof)
            diff = set_prof.difference(set_stud)
            percent = 100 // len(set_prof) * len(intersec)
            print(f'Уровень готовности: {percent} %')
            print(f"Знает: {', '.join(intersec)}")
            print(f"Не знает: {', '.join(diff)}")
            break
        elif answer != prof_dict['title'] and count_ask < len(list_prof):
            count_ask += 1
            continue
        else:
            print("У нас нет такой специальности")
            break



if __name__ == '__main__':
    set_stud = set()
    set_prof = set()
    data = load_students()
    list_prof = load_professions()
    ask = input('Введите номер пк студента: ')
    num_stud()
    answer = input(f'Выберите специальность для оценки студента: ')
    get_profession_by_title(num_stud())





