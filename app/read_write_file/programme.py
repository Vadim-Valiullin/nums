with open('list.txt') as file:
    for student_data in file:
        name, language = student_data.rstrip('\n').split(':')
        print(f'{name} учит {language}!')

        # data = student_data.split(':')
        #
        # name = data[0]
        # language = data[1]


