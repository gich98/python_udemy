import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rock_paper_scissors = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if 0 <= user_choice <= 2:
    print(f"{user_choice}\n{rock_paper_scissors[user_choice]}")
    computer_choice = random.randint(0, 2)
    print(rock_paper_scissors[computer_choice])
    if ((user_choice == 0 and computer_choice == 2)
            or (user_choice == 1 and computer_choice == 0)
            or (user_choice == 2 and computer_choice == 1)):
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lose!")
else:
    print("ERROR!!!")
