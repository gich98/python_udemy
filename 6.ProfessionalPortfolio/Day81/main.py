import re
from morse_code import MORSE_CODE_DICT
from morse_code_art import logo, bye

special_char = True
end = False
regexp = re.compile('[^0-9a-zA-Z ]+')
word = ""


def user_choice_input():
    """
    Gets the choice of the user and checks if it is a valid input or not.
    If it is correct return the choice of the user, otherwise return 0
    :return: The choice entered by the user
    """
    print("\n===============================================================\n")
    try:
        choice = int(input("What do you want to do?\n"
                           "1) Encode Word to Morse Code\n"
                           "2) Decode Morse Code to Word\n"
                           "3) Exit\n"
                           "- "))
        if not (0 < choice < 4):
            choice = 0
    except ValueError:
        choice = 0
    return choice


def encode_to_morse(word_to_encode: str) -> str:
    """
    Encode the word passed as parameter into Morse Code.
    Creates a list with the value from the MORSE_CODE_DICT associated with each letter of the word entered as input
    and then joins them into a string that will be returned from the function
    :param word_to_encode: Word entered by the user
    :return: The conversion of the word entered into Morse Code, each morse code is separated by a space
    """
    return ''.join([MORSE_CODE_DICT.get(letter) + ' ' for letter in word_to_encode])


def decode_from_morse(word_to_decode: str) -> str:
    """
    Decode the Morse Code into Plain Text.
    Creates a list of the code to decode by splitting the Morse Code by spaces, after that
    it creates a list with the index (alphanumeric) of the MORSE_CODE_DICT associated with each code of the list
    and then joins them into a string that will be returned from the function
    :param word_to_decode: Morse Code entered by the user
    :return: The conversion of the Morse COde into Plain Text
    """
    word_to_decode_list = word_to_decode.split(' ')
    try:
        result = ''.join([list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(code)]
                          for code in word_to_decode_list])
    except ValueError:
        result = ''
    return result


print(logo)
user_choice = user_choice_input()

while user_choice != 3:
    if user_choice == 1:
        word_input = (
            input("Enter the sentence or word to encode (PS: You can only enter letters and numbers):\n\t- ")
        ).upper()
        if not regexp.search(word_input):
            encoded_word = encode_to_morse(word_input)
            print(f"{word_input}\nENCODED TO MORSE:\n{encoded_word}")
        else:
            print(f"ERROR!!! Special characters are not supported.\n")
    elif user_choice == 2:
        code_input = (input("Enter the morse code you want to decode into plain text (PS: SPACE BAR = /):\n\t- "))
        decoded_word = decode_from_morse(code_input)
        if decoded_word:
            print(f"{code_input}\nDECODED FROM MORSE:\n{decoded_word}")
        else:
            print(f"ERROR!!! '{code_input}' can not be decoded, please check again the morse code entered.")
    else:
        print("Only 1, 2 and 3 are valid inputs. Please try again.")

    user_choice = user_choice_input()

print(bye)
