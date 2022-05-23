"""Final project in the subject of Computer Linguistics"""

# coding: utf8

import string
import os

print("Program had started and is working, please stand by...")


def text_transformer(input_txt):
    """This functions removes all the punctuation marks, lowers all the letters
    and generally makes the text more appropriate for the following work"""
    input_txt = open("TextAnalyzer/in.txt", "r", encoding='windows-1251')
    formatted_text = input_txt.read()
    formatted_text = formatted_text.replace("\n", " ")
    formatted_text = formatted_text.lower()
    formatted_text = formatted_text.split(" ")
    formatted_text = ["".join(c for c in s if c not in string.punctuation) for s in formatted_text]
    while "" in formatted_text:
        formatted_text.remove("")

    return formatted_text


formatted_text = text_transformer("in.txt")


def listToDict(txt):
    """This function transforms list to dictionary
    to count number of repetitions of a word in a given text"""
    d = {}
    for i in formatted_text:
        if i not in d:
            d[i] = [1]
        else:
            d[i] = [d[i][0] + 1]

    return dict(sorted(d.items(), reverse=True, key=lambda item: item[1]))


dictionary = listToDict("formatted_text")


def frequencyAndPercentage(dictionary):
    """This function returns a frequency and percentage of the words used in text"""
    for i in dictionary:
        freq = dictionary[i]
        freq.append(freq[0] / len(formatted_text))
        dictionary[i] = freq
        perc = dictionary[i]
        perc.append(freq[0] / len(formatted_text) * 100)
        dictionary[i] = perc
        dictionary[i][2] = str(dictionary[i][2]) + ' %'

    return dictionary


out = open("out.txt", "w", encoding='windows-1251')

# out.write(str(f'Слова, содержащиеся в словаре: {text_transformer("d")}\n'))
out.write(str(f'Quantity of words: {len(text_transformer("in.txt"))}\n'))
out.write(str(
    f'The number of word repetitions, frequency and percentage of the total number of words: {frequencyAndPercentage(listToDict(formatted_text))}'))
print("Job's done, pay attention to the 'out.txt' file.")
os.startfile('.\out.txt')
