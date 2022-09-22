import json
import random
from homework import Question


def questionary():
    with open('questionary.txt', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def mix_data(data):
    random.shuffle(data)
    return data

# def extract_lines(data):
#     return [Question(line['q'], int(line['d']), line['a']) for line in data]
#     # quest_list = []
#     # for line in data:
#     #     x = Question(line['q'], int(line['d']), line['a'])
#     #     quest_list.append(x)
#     # return quest_list

def main():
    data = questionary()
    data = mix_data(data)
    quest_list = [Question(line['q'], int(line['d']), line['a']) for line in data]
    total = 0
    correct_answers = 0
    for quest in quest_list:
        quest.build_question()
        quest.answer = input('Введите ответ: ')
        quest.score = quest.get_points()
        quest.build_feedback()
        total += quest.score
        correct_answers += quest.is_correct()

    print('Вот и все!')
    print(f'Отвечено на {correct_answers} вопроса из {len(quest_list)}')
    print(f'Набрано баллов: {total}')
main()
