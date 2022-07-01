import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

my_dict = {}
for (index, row) in df.iterrows():
    my_dict[row.letter] = row.code


def generate_phonetics():
    word_input = str(input("Enter a word: ")).upper()
    try:
        result = [my_dict[letter] for letter in word_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(result)


generate_phonetics()
