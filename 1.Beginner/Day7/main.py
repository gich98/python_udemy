# Step 1

import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
lives = 6
used_letters = []
display = ["_"] * len(chosen_word)

print(hangman_art.logo)


while ("_" in display) and lives >= 0:
    print(f"The word is: {display}")
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter not in used_letters:
        used_letters += guessed_letter
        correct = False
        for i in range(len(chosen_word)):
            if guessed_letter == chosen_word[i]:
                display[i] = guessed_letter
                correct = True
        if not correct:
            print(hangman_art.stages[lives])
            lives -= 1
            print(f"The letter \"{guessed_letter}\" is not in the word!")
    else:
        print(f"The letter \"{guessed_letter}\" was already used!")

if lives < 0:
    print(f"You have lost! The word was {chosen_word}")
else:
    print(f"You have won! The correct word is {chosen_word}")

