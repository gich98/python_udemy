import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

again = True
while again:
    try:
        word = input("Enter a word: ").upper()
        word_nato = [alphabet_dict[value] for value in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word_nato)
        again = False
