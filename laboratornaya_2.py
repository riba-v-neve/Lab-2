#Вариант №1

import csv
from random import randint as r
import xml.dom.minidom as minidom

#Задание_1

with open('books.csv', 'r') as table:
    books = csv.reader(table, delimiter=';') 

    count = 0
    for lines in books:
        if len(lines[1]) > 30:
            count += 1
    print(count)


#Задание_2

with open('books.csv', 'r') as table:
    books = csv.reader(table, delimiter=';') 
    flag = 0
    result = []
    author = input('Введите автора:').lower()
    for lines in books:
        if author == lines[3].lower() or author == lines[4].lower():
            if float(lines[7]) <= 150: 
                flag = 1
                if lines[1] not in result:
                    result.append(lines[1])
                
if flag == 0:
    print('Ничего не найдено:(')
else:
    for number in range(len(result)):
        print(str(number + 1) + '.', result[number])


#Задание_3

with open('books.csv', 'r') as table:
    books = csv.reader(table, delimiter=';')
    cnt = -1 
    for lines in books:
        cnt += 1

numbers = [r(1, cnt + 1) for i in range(20)]
numbers.sort()

number_2 = 0
cnt_2 = 0
with open('books.csv', 'r') as table:
    books = csv.reader(table, delimiter=';')
    with open('result.txt', 'w') as file:
        for book in books:
            cnt_2 += 1
            if cnt_2 in numbers:
                number_2 += 1
                file.write(str(number_2) + '. ' + '(' + str(cnt_2) + ' строка) ' + str(book[3]) + '. ' + str(book[1]) + ' - ' + str(book[6]) + '\n')
    file.close()


#Дополнительное задание_1

publisher = []
with open('books-en.csv', 'r') as table_en:
    books_en = csv.reader(table_en, delimiter=';') 
    for book_en in books_en:
        if book_en[4] not in publisher:
            publisher.append(book_en[4])
publisher.sort()
publisher.remove('Publisher')
print('Перечень всех издательств без повторений:')
number = 0
for name in publisher:
    number += 1
    print(str(number) + '.', name)


#Дополнительное задание_2

popular_books = {}
with open('books-en.csv', 'r') as table_en:
    books_en = csv.reader(table_en, delimiter=';')
    for book_en in books_en:
        if book_en[5] == 'Downloads':
            continue
        else:
            popular_books[book_en[1]] = int(book_en[5])


popular_books_sorted = sorted(popular_books.items(), key=lambda x: x[1], reverse=True)
popular_books_sorted_dict = dict(popular_books_sorted)

popular_books_sorted_list = list(popular_books_sorted_dict.keys())

print('Список самых популярных книг:')

for num in range(20):
    print(str(num + 1) + '.', popular_books_sorted_list[num])