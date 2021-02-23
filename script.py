# author = skokanova

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 5 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

separator = 80 * "-"
short_separator = 30 * "-"
text_count = str(len(TEXTS))
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Get username and password from user

print(separator)
name = input("Enter your username: ").lower()
password = input("Enter your password: ")

# Check, if obtained inputs are correct.
# If the user is registered, say hello and let him analyse the text.

success = False
while not success:
    if registered_users.get(name) == password:
        print(separator)
        print("You are logged in :)")
        print("Welcome to the application " + name + "!")
        print("We have " + text_count + " texts to be analyzed.")
        success = True
        print(separator)
    else:
        print("Username or password is incorrect! Try again.")
        success = False
        name = input("Enter your username: ").lower()
        password = input("Enter your password: ")

# Choose which text to analyse
number_text_analysed = int(input(f"Enter a number between 1 and {text_count} to select: "))
text_selected = int(number_text_analysed) - 1
success1 = False

while not success1:
    if int(number_text_analysed) >= 1 and int(number_text_analysed) <= 3:
        print(separator)
        print("You selected this text to be analysed:")
        print(separator)
        print(TEXTS[int(number_text_analysed) - 1])
        print(separator)
        success1 = True
    else:
        number_text_analysed = input(f"Incorrect number was selected! Please select number from 1 to {text_count} again: ")
        success1 = False

# Prepare text for further analysis

dirty_words = TEXTS[text_selected].split()
clean_words = []

for word in dirty_words:
    clean_words.append(word.strip(".,!?:"))

# Text analysis

words_count = len(clean_words)
title_count = 0
upper_count = 0
lower_count = 0
integer_count = 0
sum_count = 0

for word1 in clean_words:
    if word1.istitle():
        title_count += 1
    elif word1.isupper():
        upper_count += 1
    elif word1.islower():
        lower_count += 1
    elif int(word1):
        integer_count += 1
        sum_count += int(word1)

# Text analysis output

print(f"There are {words_count} words in the selected text.")
print(f"There are {title_count} titlecase words.")
print(f"There are {upper_count} uppercase words.")
print(f"There are {lower_count} lowercase words.")
print(f"There are {integer_count} numeric strings.")
print(f"The sum of all the numbers: {sum_count}.")

# Bar chart

word_dict = dict()
length = 0
max_length = 0

# longest word

for word in clean_words:
    length = len(word)
    if length > max_length:
        max_length = length

# Dictionary init

for i in range(max_length)[1:]:
    word_dict[i] = 0

length = 0
for word in clean_words:
    length = len(word)
    if length in word_dict:
        word_dict[length] += 1
    else:
        word_dict[length] = 1


print(short_separator)

print("LEN  |   OCCURANCES     | NR.")
print(short_separator)
for i in word_dict:
    word_length = word_dict.get(i)
    stars = word_dict.get(i) * "*"
    print(f'{f"{i}:":5}|{f"{stars}":<18}|{f"{word_length}"}')

print(short_separator)
