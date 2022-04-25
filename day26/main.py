import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

user_word = input("Enter a word: ").upper()
# for letter in user_word:
#     if letter in nato_dict:
#         print(nato_dict[letter])

nato_word = [nato_dict[letter] for letter in user_word]
print(nato_word)

# user_letters = [char for char in user_word]