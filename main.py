from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
import words

def make_haiku(first,second,third):
    haiku_1 = make_line(5,first)
    haiku_2 = make_line(7,second)
    haiku_3 = make_line(5,third)
    
    print(haiku_1)
    print(haiku_2)
    print(haiku_3)

def make_line(vowels_allowed,word_list):
    counter = []
    
    for word in word_list:
        if words.exception_checker(word):
            counter.append(words.exception_vowels(word))
        else:
            counter.append(vowel_counter(word))
    
    if sum(counter) == vowels_allowed:
        return ' '.join(word_list)
    
    elif sum(counter) < vowels_allowed:
        vowels_left = vowels_allowed - sum(counter)
        new_word_list = words.add_words(vowels_left, word_list)
        return ' '.join(new_word_list)
    
    else:
        word_list.pop()
        make_line(vowels_allowed,word_list)
            
def vowel_counter(word):
    vowels = ['a','e','i','o','u','y','A','E','I','O','U',]
    #not including capital y since it will likely not be vowel sound
    counter = 0
    
    for i in word:
        if i in vowels:
            counter = counter + 1
     

#first_sentence = input("Enter first sentence:") 
#second_sentence = input("Enter second sentence:")
#third_sentence = input("Enter third sentence:")

first_sentence = "hello I am alisha"
second_sentence = "roses only fall when in need"
third_sentence = "I like to eat cake"     

first_list = word_tokenize(first_sentence)
second_list = word_tokenize(second_sentence)
third_list = word_tokenize(third_sentence)

make_haiku(first_list,second_list,third_list)

exception = input('Is this a haiku based on the vowel sounds/Do the number of vowel letters match the number of vowel sounds?(Y/N)')

if exception.lower() == 'n':
    print('Please include a word that you used where the number of vowel letters does not match the number of vowels sounds when prompted.')
    word = input('Enter the word:')
    vowel_sounds = input('Enter the number of vowel sounds:')
    
    words.exception_adder(vowel_sounds,word)
    
    print('Thanks for helping make this better!')    
else:
    print('Good to hear!')

print('Refresh to try a new haiku!') 