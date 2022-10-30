import random


def file_unpacking():
    with open('world.txt', 'r') as worlds:
        for world in worlds:
            world_all.append(world.strip())

world_all = []
file_unpacking()
print(world_all)

world_dict = {}

for i, word in enumerate(map(list, world_all)):
    random.shuffle(word)
    world_dict[world_all[i]] = ''.join(word)

print(world_dict)

print('Программа: Введите ваше имя')
user_name = input('Пользователь: ')
count = 0
for word, world_random in world_dict.items():
    print(f'Программа: Угадайте слово: {world_random}')
    user_answer = input('Пользователь: ')
    if user_answer == word:
        print('Программа: Верно! Вы получаете 10 очков.')
        count += 10
    else:
        print(f'Программа: Неверно! Верный ответ: {word}.')
print(f'Вы заработали: {count}')

with open('history.txt', 'a', encoding="utf-8") as file:
    file.write(f'{user_name} - количество очков: {count}\n')

line = 0
s = []
with open('history.txt', 'r', encoding="utf-8") as file:
    for i in file:
        line += 1
        s.append(*(int(s) for s in str.split(i) if s.isdigit()))
print(f'Количество игр: {line}')
print(f'Рекорд: {max(s)}')


