#importing libraries
import os
import re

#asking the user for the path and name of the file to be analyzed
print("============================================")
print("|                                          |")
print("|  Welcome to the paragraph analysis tool  |")
print("|                                          |")
print("============================================")
#file = input("What's the name of the file you want to analyze? (in Resources folder):")
#for testing purposes, switch comment above and below when testing is done
file = 'paragraph_1.txt'


#checking if the file exists
txtpath = os.path.join('Resources', file)
file_exists = os.path.exists(txtpath)
while file_exists == False:
    file_exists = os.path.exists(txtpath)
    if file_exists == False:
        file = input("Error: file does not exist, make sure it is on the /Resources folder and it is typed correctly:")
        txtpath = os.path.join('Resources', file)

#opening and storing the txt file
paragraph = open(txtpath).read()

#counting words
word_count = 1 #initializes to 1 because last word has no space
for _ in paragraph:
    if _ == " ":
        word_count += 1

#counting sentences
sentences = re.split("(?<=[.!?]) +", paragraph)
sentence_count = len(sentences)

#calculating average letter by word

#initializing variables
letters_by_word = []

#splitting the paragraph in separate words
paragraph_by_words = paragraph.split(" ", -1)

#obtaining number of letters
for word in paragraph_by_words:
    letters_by_word.append(len(word))

#calculating average
total_words = 0
for _ in letters_by_word:
    total_words += letters_by_word[_]
average_letters = float(total_words) / float(word_count)
        

print(paragraph)
print(str(word_count) + " words")
print(str(sentence_count) + " sentences")
print(paragraph_by_words)
print(letters_by_word)
print(average_letters)
