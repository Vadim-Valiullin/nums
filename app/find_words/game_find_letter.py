words = {"mouse": 2, "difficult": 7, "surprise": 7}
answers = {}

def name_user():
    print(f"Привет, напиши, пожалуйста, имя!\nОно должно быть без пробелов и цифр.")
    while True:
        global name
        name = input("Имя: ")
        if " " in name:
            print(f"\nКажется, в имени пользователя есть пробелы.")
            continue
        elif not name.isalpha():
            print(f"\nКажется, в имени пользователя есть цифры.")
            continue
        else:
            print(f"\nОтлично, {name}, давай начнем тренировку!")
            break

def traning_memory():
    counter = 1
    for word, number in words.items():
        word_1 = word.replace(word[number - 1],"*") # вывод слова со *
        print(f"Вставьте пропущенную букву в слове {word_1}.")
        answer = input()
        if answer == word[number - 1]:
            print(f"Ответ верный\n")
            answers[counter] = True
            counter += 1
        else:
            print(f"Ответ неверный. Верный ответ – {word}\n")
            answers[counter] = False
            counter += 1


if __name__ == "__main__":
    name_user()
    traning_memory()
    print(f"Вот и все, {name}.")
    word_answer = []
    for word in words.keys():
        word_answer.append(word)
    for key, value in answers.items():
        if value == True:
            print(f"{key} - {word_answer[key-1]} - угадано!")
        else:
            print(f"{key} - {word_answer[key-1]} - не угадано!")