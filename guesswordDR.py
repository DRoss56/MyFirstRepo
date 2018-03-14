import random

words = ["intricate","i cup","innovitation","vsauce"]

hint1 = ["The best word","if apple made a cup","the future, what drives the world","hey ______ Michael here"]

hint2 = ["I always love to say it ","what you see with and what you drink out of","flows like a river","A great source of spit facts"]

number = random.randint(0,3)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the best word")
    print("Type 'hint1', 'hint2', 'firstletter', 'lastletter', or 'give up' for help.")
    guess = input()
    counter += 1
    if guess == secretword:
        print ("You are correct? It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(  hint1[number]   )


        print(  hint2[number]   )

    elif guess == "first letter":
        print ( secretword[0] )

    elif guess == "last letter":
        print ( secretword[-1] )

    elif guess == "give up":
        print ("One of the best words is " + secretword )
        break
