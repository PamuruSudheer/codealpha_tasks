import random
word=['apple','banana','mango','grapes','orange','pineapple','cherry']
lives=6
chosen=random.choice(word)
print("🎮 Welcome to Hangman!")
print("You have 6 chances to guess the word.")
print("Let's start!\n")
#print(chosen)
display=[]
for letter in range(len(chosen)):
    display+="_"
print(display)
game=False
while not game:
    user=input("Guess a letter:").lower()
    print("Wrong guesses left:", lives)

    for position in range(len(chosen)):
        letters=chosen[position]
        if letters==user:
           display[position]=user
           print("✅ Good job! That letter is in the word.\n")
    print(display)
    if user not in chosen:

        print("❌ Sorry, that letter is not in the word.\n")
        lives -=1
        if lives ==0:
            game=True
            print("😢 You lost! The word was:",chosen)
    if '_' not in display:
        game=True
        print(" 🎉 You win! The word was:",chosen)