import sqlite3
import unittest


#
# class Test(unittest):
#     pass



###########################################
#                   database
###########################################

def open_dictionary():
    connection = sqlite3.connect("Dictionary.db")
    return connection


def close_dictionary(connection):
    connection.close()

def query(cursor, pattern_word):
    query = """select word, definition from entries where 
                word like {0} and wordtype='n.'""".format(pattern_word)
    results = cursor.execute(query)
    if results:
        return results.fetchall()

def random_word(cursor, min_len=3, max_len=10):
    while True:
        query = """SELECT word FROM entries ORDER BY RANDOM() LIMIT 100"""
        result = cursor.execute(query)
        result = result.fetchall()
        for wrd, *_ in result:
            wrd = wrd
            if len(wrd) >= min_len and len(wrd) <= max_len:
                return wrd
###########################################


##########################################
# Структуры
##########################################

words = []
nodes = []


class IncorrectDate(Exception):
    pass


def word(letters, vertical):
    """Возвращает словарь описыващий слово
    'letters' - letter - список букв
    'vertical' - Boolean - положение слова"""
    return {'letters': letters,'vertical': vertical, 'str': "".join([k.get('letter') for k in letters])}

def letter(letter, x, y):
    """Возвращает словарь описывающий букву
    'coord' - tuple - координаты буквы"""
    return {'coord': (x, y), 'letter': letter}

def node(letter, *words):
    if len(words) != 2:
        raise IncorrectDate()
    return {'words': (word for word in words), 'cross': letter}

def build_word(word_str, vertical, x, y):
    """конструирует словарь слова"""
    letters = []
    for i, l in enumerate(word_str):
        if vertical:
            letters.append(letter(l, x, y + i))
        else:
            letters.append(letter(l, x + i, y))
    return word(letters, vertical)


def put_word(parent_word):
    """записывает новое слово в кроссворд"""
    global words
    global nodes
    




if __name__ == '__main__':
    connection = open_dictionary()
    cursor = connection.cursor()
    first_word = random_word(cursor)
    w = build_word(first_word, False, 0, 0)

    close_dictionary(connection)
