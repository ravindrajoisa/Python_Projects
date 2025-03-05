import random
word_list=["apple", "beautiful", "potato"]
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)): # 0 1 2 3 4 5 #apple
    display += '_'
print(display)
game_over=False
while not game_over:
    gussed_letter = input("Guess a letter: ").lower() #r
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter==gussed_letter:
            display[position]=gussed_letter
    print(display)    
    if gussed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")
    if '_' not in display:
        game_over=True
        print("You Win!")