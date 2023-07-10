import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    # Implementing vectors e,s as lists (arrays) of length 26
    # with p[0] being the probability of 'A' and so on
    e = [0] * 26
    s = [0] * 26

    with open('e.txt', encoding='utf-8') as f:
        for line in f:
            # strip: removes the newline character
            # split: split the string on space character
            char, prob = line.strip().split(" ")
            # ord('E') gives the ASCII (integer) value of character 'E'
            # we then subtract it from 'A' to give array index
            # This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char) - ord('A')] = float(prob)
    f.close()

    with open('s.txt', encoding='utf-8') as f:
        for line in f:
            char, prob = line.strip().split(" ")
            s[ord(char) - ord('A')] = float(prob)
    f.close()

    return (e, s)


def shred(filename):
    # Using a dictionary here. You may change this to any data structure of
    # your choice such as lists (X=[]) etc. for the assignment
    X = dict()
    letters = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0,
               "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    with open(filename, encoding='utf-8') as f:
        # TODO: add your code here
        for line in f:
            for char in line:
                if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
                    x = letters.get(char.upper())
                    letters.update({char.upper(): int(1 if x is None else x + 1)})
            # print(line)
        print("Q1")
        for key, value in letters.items():
            print(key, value)
        print("Q2")
        e, s = get_parameter_vectors()
        print("{:.4f}".format(math.log(e[0]) * letters["A"]))  # A is 65
        print("{:.4f}".format(math.log(s[0]) * letters["A"]))
        print("Q3")
        totale = 0
        for i in range(26):
            totale += math.log(e[i]) * letters[chr(65 + i)]
        fEnglish = totale + math.log(.6)
        print("{:.4f}".format(fEnglish))
        totals = 0
        for i in range(26):
            totals += math.log(s[i]) * letters[chr(65 + i)]
        fSpanish = totals + math.log(.4)
        print("{:.4f}".format(fSpanish))
        print("Q4")
        if fSpanish - fEnglish >= 100:
            print(0)
        elif fSpanish - fEnglish <= -100:
            print(1)
        else:
            print("{:.4f}".format(1 / (1+ math.pow(math.e, (fSpanish-fEnglish)))))
    return X


shred("letter.txt")
get_parameter_vectors()
# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
