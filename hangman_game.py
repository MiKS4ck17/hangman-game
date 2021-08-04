import os
import random as rd


hangman = ["""===========================================================
===========================================================
            *** Welcome to My Hangman Game ***
===========================================================
===========================================================
""",
"""❤ ❤ ❤ ❤ ❤ ❤ 
  ______________
 |              |
 |              |
 |              |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
---
""",
"""❤ ❤ ❤ ❤ ❤ 
  ______________
 |              |
 |              |
 |              |
 |            --~--
 |          -+     +-
 |         -         -
 |          -+     +- 
 |            --~--
 |
 |
 |
 |
 |
 |
 |
---
""",
"""❤ ❤ ❤ ❤
  ______________
 |              |
 |              |
 |              |
 |            --~--
 |          -+     +-
 |         -         -
 |          -+     +- 
 |            --~--
 |              |
 |              |
 |              |
 |
 |
 |
 |
---
""",
"""❤ ❤ ❤
  ______________
 |              |
 |              |
 |              |
 |            --~--
 |          -+     +-
 |         -         -
 |          -+     +- 
 |            --~--
 |             /|\\
 |            / | \\
 |           /  |  \\
 |
 |
 |
 |
---
""",
"""❤ ❤
  ______________
 |              |
 |              |
 |              |
 |            --~--
 |          -+     +-
 |         -         -
 |          -+     +- 
 |            --~--
 |             /|\\
 |            / | \\
 |           /  |  \\
 |             / \\
 |            /   \\
 |           /     \\
 | 
---
""",
"""❤
  ______________
 |              |
 |              |
 |              |
 |            --~--
 |          -+     +-
 |         -         -
 |          -+     +- 
 |            --~--
 |             /|\\
 |            / | \\
 |           /  |  \\
 |             / \\
 |            /   \\
 |          _/     \_
 | 
---
""",
"""  ______________
 |              |
 |              |
 |              |
 |            --~--
 |          -+     +-
 |         -  X   X  -
 |          -+  0  +- 
 |            --~--
 |             /|\\
 |            / | \\
 |           /  |  \\
 |             / \\
 |            /   \\
 |          _/     \_
 | 
---
""",
"""===========================================================
===========================================================
                     *** ¡FELICIDADES! ***
===========================================================
===========================================================
""",
"""===========================================================
===========================================================
            *** Suerte para la proxima :( ***
===========================================================
===========================================================
"""]


def replace_diacritic(word):
    word = word.replace('Á', 'A')
    word = word.replace('É', 'E')
    word = word.replace('Í', 'I')
    word = word.replace('Ó', 'O')
    word = word.replace('Ú', 'U')
    word = word.replace('\n', '')
    return word


def lines(word):
    a = ''
    for i in word:
        if i == '\n':
            continue
        a = a + '_ '
    return a
    


def read():
    with open('./data.txt', 'r') as f:
        words = [word for word in f]
        word = rd.choice(words).upper()
        word = replace_diacritic(word)
        return word


def obtain_result(input_char, word, lines):
    listlines = list(lines)
    for count, char in enumerate(word):
        if char == input_char:
            listlines[count * 2] = input_char
            listlines[count * 2 + 1] = ' '
    return "".join(listlines)


def run():
    # The word that I need to find
    word = read()
    # An string lines
    str_lines = lines(word)
    # Result
    result = ''
    # Tries
    TRIES = 7
    my_tries = 1
    while result != word and my_tries < TRIES:
        try:
            print(hangman[0])
            print(hangman[my_tries])
            print(str_lines)
            char = input('Ingrese un caracter: ').upper()
            if len(char) > 1:
                raise ValueError('Solo puedes ingresar un caracter por turno')
            if str_lines == obtain_result(char, word, str_lines):
                my_tries += 1
            str_lines = obtain_result(char, word, str_lines)
            result = str_lines.replace(' ', '')
            os.system("clear")
        except ValueError as ve:
            print(ve)
    if word == result:
        print(hangman[8])
    else:
        print(hangman[9])
    print(hangman[my_tries])
    print(word)

    


if __name__ == '__main__':
    run()