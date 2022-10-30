import random
import sys

letters = ['а', 'а', 'а', 'а', 'а', 'а', 'а', 'а', 'б', 'б', 'в', 'в', 'в', 'в', 'г', 'г', 'д', 'д', 'д', 'д', 'е',
     'е', 'е', 'е', 'е', 'е', 'е', 'е', 'е', 'ж', 'з', 'з', 'и', 'и', 'и', 'и', 'и', 'й', 'к', 'к', 'к', 'к',
     'л', 'л', 'л', 'л', 'м', 'м', 'м', 'н', 'н', 'н', 'н', 'н', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о', 'о',
     'о', 'п', 'п', 'п', 'п', 'р', 'р', 'р', 'р', 'р', 'с', 'с', 'с', 'с', 'с', 'т', 'т', 'т', 'т', 'т', 'у',
     'у', 'у', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ы', 'ь', 'ь', 'э', 'ю', 'я', 'я']
random.shuffle(letters)

words = []
with open('words.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words.append(line.rstrip('\n'))

score_for_answer_list = [0, 0, 0, 3, 6, 7, 8, 9]
score_player_1 = []
score_player_2 = []
user_list = []
user_list_1 = []
user_list_2 = []
extra_letters_1 = []
extra_letters_2 = []
temp_list_1 = []
temp_list_2 = []
num = 0

print('\nПривет.\nМы начинаем играть в Scrabble')
print('Как зовут первого игрока?')
name_1 = input('Пользователь:\n')
print('Как зовут второго игрока?')
name_2 = input('Пользователь:\n')
print(f'Программа:\n{name_1} против {name_2}\nРаздаю случайные буквы')

user_list_1.extend(letters[0:7])
del letters[0:7]
print(f"{name_1} - буквы {', '.join(user_list_1)}")

user_list_2.extend(letters[0:7])
del letters[0:7]
print(f"{name_2} - буквы {', '.join(user_list_2)}")


while len(letters) > 0 or len(user_list_1) > 3 or len(user_list_2) > 3:
    if num == 0:
        print(f"Ходит {name_1}\nБуквы: {', '.join(user_list_1)}")
        answerr = input("Ввод: ")
        answer_1 = list(answerr)
        copy_list_1 = user_list_1.copy()
        if answerr == 'Stop' or answerr == 'stop':
           print(f'Игра окончена по инициативе {name_1}')
           sys.exit(0)
        for i in answer_1:
            if i in user_list_1:
                temp_list_1.append(i)
                copy_list_1.remove(i)
            else:
                break
        if 3 <= len(answer_1) <= 6 and answerr in words and answer_1.sort() == temp_list_1.sort():
            user_list_1 = copy_list_1
            print(f'\nТакое слово есть\n{name_1} получает {score_for_answer_list[len(answer_1)]} баллов')
            extra_letters_1.clear()
            extra_letters_1.extend(letters[0:len(answer_1)+1])
            del letters[0:len(answer_1)+1]
            print(f"Добавляю буквы: {', '.join(extra_letters_1)}")
            user_list_1.extend(extra_letters_1)
            score_player_1.append(score_for_answer_list[len(answer_1)])
            num += 1

        else:
            print(f'Такого слова нет или вы использовали букву не из списка\n{name_1} не получает баллов')
            extra_letters_1.clear()
            if len(letters) > 0:
                extra_letters_1.extend(letters[0])
            else:
                print('Буквы закончились!')
                break
            del letters[0]
            print(f"Добавляю букву: {', '.join(extra_letters_1)}")
            user_list_1.extend(extra_letters_1)
            num += 1
            print(f"Буквы: {', '.join(user_list_1)}")



    elif num == 1:
        print(f"Ходит {name_2}\nБуквы: {', '.join(user_list_2)}")
        answerrr = input("Ввод: ")
        answer = list(answerrr)
        copy_list_2 = user_list_2.copy()
        if answerrr == 'Stop' or answerrr == 'stop':
            print(f'Игра окончена по инициативе {name_2}')
            sys.exit(0)
        for i in answer:
            if i in user_list_2:
                copy_list_2.remove(i)
                temp_list_2.append(i)
            else:
                break
        if answerrr in words and 3 <= len(answer) <= 6 and answer.sort() == temp_list_2.sort():
            user_list_2 = copy_list_2
            print(f'\nТакое слово есть\n{name_2} получает {score_for_answer_list[len(answer)]} баллов')
            extra_letters_2.clear()
            extra_letters_2.extend(letters[0:len(answer) + 1])
            del letters[0:len(answer) + 1]
            print(f"Добавляю буквы: {', '.join(extra_letters_2)}")
            user_list_2.extend(extra_letters_2)
            score_player_2.append(score_for_answer_list[len(answer)])
            num -= 1
            continue
        else:
            print(f'Такого слова нет или вы использовали букву не из списка\n{name_2} не получает баллов')
            extra_letters_2.clear()
            if len(letters) > 0:
                extra_letters_2.extend(letters[0])
            else:
                print('Буквы закончились!')
                break
            del letters[0]
            print(f"Добавляю букву: {', '.join(extra_letters_2)}")
            user_list_2.extend(extra_letters_2)
            num -= 1
            continue

if sum(score_player_1) > sum(score_player_2):
    print(f'Счет {sum(score_player_1)} : {sum(score_player_2)}\n{name_1} победил')
elif sum(score_player_1) < sum(score_player_2):
    print(f'Счет {sum(score_player_1)} : {sum(score_player_2)}\n{name_2} победил')
else:
    print(f'Счет {sum(score_player_1)} : {sum(score_player_2)}\nНичья!')

