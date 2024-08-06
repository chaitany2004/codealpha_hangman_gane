import random
stages=['''
+----+
 |   |
 0   |
/|\  |
/ \  |
     |
''','''
+----+
 |   |
 0   |
/|\  |
/    |
     |
''','''
 +---+
 |   |
 0   |
/|   |
     |
     |
''','''
 +----+
 |    |
 0    |
 |    |
      |
      |
''','''
 +-----+
 |     |
 0     |
       |
       |
       |
''','''
  +------+
  |      |
         |
         |
         |
         |
'''
]

print("------------WELCOME TO THE HANGMAN GAME LET'S PLAY-------------\n\n")
word_list=["apple","potato","beautiful","mango"]
lives=5
chosen_word=random.choice(word_list)
display=[]
for i in range(len(chosen_word)):
    display+='_'
    
print(display,"\n\n")
print("***********************************************")


game_over=False
while not game_over:
    guessed_letter=input("Guess a letter :: ").lower()
    print("***********************************************\n")

    
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
            print("You guessed correct letter",guessed_letter)
            
    print(display)
            
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("***************************************")
            print("You lose !!")
            print("The correct word is :",chosen_word)
            print("please try again!!")
            print("***************************************")
            
    if '_' not in display:
        game_over=True
        print("***********************************\n")
        print("CONGRATULATIONS YOU WON THE GAME !!!")
        
    print(stages[lives])
    