# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

project_path = "/Intermediate/Day24"

with open(f"{project_path}/Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()
with open(f"{project_path}/Input/Letters/starting_letter.txt") as starting_letter:
    content_letter = starting_letter.readlines()

for name in names:
    content_letter = "".join(content_letter)
    stripped_name = name.strip("\n")
    final_letter = content_letter.replace("[name]", stripped_name)
    letter_name = "letter_for_" + stripped_name
    with open(f"{project_path}/Output/ReadyToSend/{letter_name}.txt", mode="w") as letter:
        letter.write(final_letter)
