#
# file = open('file', 'rt')
#
# for line in file:
#     print(line)
#
# # content = file.read(10)
# # print(content)
#
# file.close()

with open('file', 'rt') as file:
    lines_quantity = len(file.readlines())
    for line in file:
        print(line)
    print(lines_quantity)