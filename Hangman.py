import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
print (hangman_art.logo)
display = []
for blank in chosen_word:
    display +="_"
print(f"{' '.join(display)}")

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess} and it is not in the word.  You lose a life")
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You've lost :( ")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You've won!")
    print(hangman_art.stages[lives])



