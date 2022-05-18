#jumble words game to be played between two players
#words will be given by system for fairness in game


from numpy import choose
import random


def choose():
    word = ["rainbow","light","World","domestic","rohan","vipin","sky","beautiful","computer","programming"]
    pick=random.choice(word)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def play():
    print("--Lets play jumble words--")
    p1name = input("what is your good name player 1 ? ")
    p2name = input("what is your good name player 2 ?")
    pp1 = 0
    pp2 = 0
    turn = 0

    while(1):
    # computer task
        pick_word = choose()
    # create question
        ques = jumble(pick_word)
        print("The jumbled word is - ",ques)
        if (turn%2==0):
        # for player1
            print(p1name, "its your turn")
            ans = input("what you guessed ? ")
            if ans == pick_word:
                print("wow! you guessed it right ")
                pp1 = pp1+1
            else:
                print(" oo ! Better luck next time. The word is - ", pick_word)
            c = int(input("Do you wanna continue(1) or quit()0 ?"))
            if c == 0:
                print(f"Thankyou for playing, {p1name} your score is {pp1} and {p2name} your score is {pp2} ")
                break
        else:
        # for player2
            print(p2name, "its your turn")
            ans = input("what you guessed ?")
            if ans == pick_word:
               print("Wow! you guessed it right. ")
               pp2 = pp2+1
            else:
                print(" oo! Better luck next time. The word is", pick_word)
            c = int(input("Do you wanna continue(1) or quit()0 ? " ))
            if c == 0:
                print(f"Thankyou for playing, {p1name} your score is {pp1} and {p2name} your score is {pp2} ")
                break

        turn = turn+1
play()
