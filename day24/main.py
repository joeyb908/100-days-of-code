import os

script_dir = os.path.dirname(os.path.abspath(__file__))

# open list of names and copy to a separate list
with open("../Input/Names/invited_names.txt", mode="r") as names:
    names = names.readlines()
    names_list = []
    names_list = names.copy()

# take away the \n
for index in range(0, len(names_list) - 1):
    names_list[index] = names_list[index].strip("\n")

#Replace the [name] placeholder with the actual name.
with open("../Input/Letters/starting_letter.txt", mode="r") as letters:
    letter = letters.read()
    letter_copy = letter

# checks if ReadyToSend exits, if not, creates it THEN writes the finished letter
for name in names_list:
    completed_letter = letter_copy.replace("[name]", name)
    if os.path.exists("./ReadyToSend"):
        with open(f"./ReadyToSend/letter_{name}.txt", mode='w+') as finished_letter:
            finished_letter.write(completed_letter)
    else:
        os.mkdir("./ReadyToSend")