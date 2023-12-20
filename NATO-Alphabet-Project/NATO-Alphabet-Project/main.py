import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

phonetic_dictionary= {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)

word = input("Enter a word: ").upper()
output_list = [phonetic_dictionary[letter] for letter in word]
print(output_list)