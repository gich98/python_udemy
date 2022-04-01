import art
import game_data
from logic import random_data, compare_follower


data = game_data.data
correct = True
game_status = "Y"
user_a = random_data(data)
user_b = random_data(data)
score = 0

while game_status == "Y":
    while correct:
        user_more_followed = compare_follower(user_a.get("follower_count"), user_b.get("follower_count"))
        print(art.logo)
        print(f"Compare A: {user_a.get('name')}, a {user_a.get('description')}, from {user_a.get('country')}")
        print(art.vs)
        print(f"Against B: {user_b.get('name')}, a {user_b.get('description')}, from {user_b.get('country')}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess == user_more_followed:
            score += 1
            if guess == "A":
                print(f"You're right! {user_a.get('name')} has {user_a.get('follower_count')} MLN of followers, "
                      f"instead {user_b.get('name')} only has {user_b.get('follower_count')} MLN of followers."
                      f"\nYour current score is: {score}")
                user_a = user_b
                user_b = random_data(data)
            else:
                print(f"You're right! {user_b.get('name')} has {user_b.get('follower_count')} MLN of followers, "
                      f"instead {user_a.get('name')} only has {user_a.get('follower_count')} MLN of followers."
                      f"\nYour current score is: {score}")
                user_b = random_data(data)
            correct = True
        else:
            print(f"Sorry, that's wrong."
                  f"\n{user_a.get('name')} has {user_a.get('follower_count')} MLN of followers."
                  f"\n{user_b.get('name')} has {user_b.get('follower_count')} MLN of followers."
                  f"\nFinal score:{score}")
            correct = False
        print("================================================================================================")
    game_status = input("Do you want to keep playing? Type 'Y' to keep playing or 'N' to stop playing.\n").upper()
    if game_status == "Y":
        correct = True
        data = game_data.data
        user_a = random_data(data)
        user_b = random_data(data)
        score = 0
