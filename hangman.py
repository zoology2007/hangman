import random

name=input("What is you name?")

print("Best of LUCK",name)

words=["fighting", "waste", "body", "leaflet", "youtube", "facebook", "whatsapp", "instagram", "snapchat", "you", "cant", "see", "me", "john", "cena"]

choose=random.choice(words)

print("Guess the charactors of the word!!!")

guesses=""

turns=12

while turns > 0:

    failed=0

    for i in choose:

        if i in guesses:

            print(i)

        else:

            print("_")

            failed+=1
    
    if failed==0:

        print("You win!!!!")

        print("The word is",choose)

        break

    guess=input("Guess a charactor")

    guesses+=guess

    if guess not in choose:

        turns-=1

        print("You have",turns,"left")

        if turns == 0:

            print("Better luck next time")