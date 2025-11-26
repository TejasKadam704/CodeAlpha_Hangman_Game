import random

someWords = ['python', 'code', 'html', 'cpp', 'java']

def play_game():
    word = random.choice(someWords)
    print('Guess the word! HINT: word is related to programming')
    print(f'The word has {len(word)} letters')
    print('You can guess a single letter OR the whole word!')

    guessed_letters = set()
    chances = 6
    flag = False

    print(" ".join("_" for _ in word))

    while chances > 0 and not flag:
        print(f"\nChances remaining: {chances}")
        guess = input("Enter a letter or the whole word: ").lower().strip()

        if not guess.isalpha():  
            print("Enter only LETTERS!")
            continue


        if len(guess) > 1:
            if guess == word:
                print("\nThe word is:", word)
                print("Congratulations, You won!")
                return
            else:
                print(f'Sorry! "{guess}" is not the correct word')
                chances -= 1
                continue


        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f'Good guess! "{guess}" is in the word')
        else:
            print(f'Sorry! "{guess}" is not in the word')
            chances -= 1

        current_display = ""
        completed = True
        for char in word:
            if char in guessed_letters:
                current_display += char + " "
            else:
                current_display += "_ "
                completed = False

        print(current_display)

        if completed:
            print("\nThe word is:", word)
            print("Congratulations, You won!")
            flag = True

    if not flag:
        print("\nYou lost! Try again..")
        print("The word was:", word)


if __name__ == "__main__":
    while True:
        play_game()
        restart = input("\nDo you want to play again? (yes/no): ").lower()
        if restart not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break
