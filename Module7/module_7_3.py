"""
Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут
file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:

    'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    ['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

Алгоритм получения словаря такого вида в методе get_all_words:

    Создайте пустой словарь all_words.
    Переберите названия файлов и открывайте каждый из них, используя оператор with.
    Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не
    дефис в слове).
    Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.
"""


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = tuple(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for symbol in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        line = line.replace(symbol, '')
                    splited_line = line.split()
                    all_words[file_name] = all_words.get(file_name, []) + splited_line
        return all_words

    def find(self, word):
        word = word.lower()
        find_dict = {}
        for name, words in self.get_all_words().items():
            cnt = 1
            for w in words:
                if w == word:
                    find_dict[name] = cnt
                    break
                cnt += 1
        return find_dict

    def count(self, word):
        word = word.lower()
        count_dict = {}
        for name, words in self.get_all_words().items():
            cnt = 0
            for w in words:
                if w == word:
                    cnt += 1
            count_dict[name] = cnt
        return count_dict


# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
