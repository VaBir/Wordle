import random
import sys
from termcolor import colored
import nltk
#nltk.download('words')
from nltk.corpus import words

def print_menu():
  print('WELCOME TO WORDLE!!!\n')
  print('\n Type a 5-letter word and hit "Enter"\n')

def read_random_word():
  with open('words.txt') as f:
    words = f.read().splitlines()
    return random.choice(words)

nltk.data.path.append('/work/words')
word_list = words.words()
words_five_let = [word for word in word_list if len(word) == 5]

print_menu()

play_again = ''
while play_again != 'q':
  #word = read_random_word()
  word = random.choice(words_five_let)
  





    
    if guess == word:
        print(colored(f'Congratulations!! You found the word in {attempt} !!!!!!', 'red'))
        break
  play_again = input('Want to play again? Type q to exit.')
  
