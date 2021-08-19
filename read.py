file=open('./text.txt')

# for line in file:
#     print(line);

# file.seek(5)
# paragraph=file.read(100)
# print(paragraph)

with open('./text.txt') as file:
    file.seek(5)
    reading=file.read(50)
print(reading)