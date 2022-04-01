# import subprocess
import art


def clear():
    for i in range(20):
        print("\n")
    # subprocess.call("C:\\Windows\\System32\\cmd.exe cls", shell=True)
    # if os.name == "nt":
    #     os.system("cls")
    # else:
    #     os.system("clear")


def auction_winner():
    winner_name = ""
    winner_bid = 0
    for key in auction:
        if auction[key] > winner_bid:
            winner_name = key
            winner_bid = auction[key]

    print(f"The winner is {winner_name} with a bid of ${winner_bid}")


print(art.logo)
print("Welcome to the secret auction program.")

auction = {}
repeat = "yes"

while repeat == "yes":
    name = input("What is your name?\n")
    bid = float(input("What is your bid?\n$"))
    auction[name] = bid
    repeat = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if repeat == "yes":
        clear()

auction_winner()
