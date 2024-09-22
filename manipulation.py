#ask for input from user
#read length of the users input
#display the lenght of the input

#index the last char in input
#replace each of the same char with @

#index the last 3 char in input
#display them backwards

#index first 3 char. and last 2 char from users input
#create a word with the indexed char.

#start
str_manip = input("please enter a sentence ")
print(str_manip) #displays user sentence

print(len(str_manip)) #displays number of characters including spaces

last_letter = (str_manip[-1:]) #indexes the final letter in users input
new_sentence = str_manip.replace(last_letter, '@')#replaces each occurrence of last_letter with @
print(new_sentence)

letters_backwards = (str_manip[:-4:-1]) # index starts from position -4 (not included) finds 3 lastl letters in reverse
print(letters_backwards) # prints  in reverse the 3 final letters of the input

new_word = (str_manip[0:3])+(str_manip[-2:]) #finds first 3 char and adds them to last 2 char of user input
print(new_word)
