from random import *

def quizz(q,a,s):
        print(q)
        r = input(">>> ")
        if r == a:
            s += 1
            print("correct")
        else:
            print("false")
        return s

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why did the math book look sad? Because it had too many problems!",
    "How does a penguin build its house? Igloos it together!",
    "What do you get when you cross a snowman and a vampire? Frostbite!",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "What did one wall say to the other wall? I'll meet you at the corner!"
]

print("1- jokes , 2 - quizz , 3 - guess the number, 4 off")
x = input(">>>")

while x != "4":

    if x == "1":
        print(choice(jokes))

    elif x == "2":
        s=0
        s = quizz("What is the capital of Morocco?", "Rabat", s)
        s = quizz("What is the largest planet in our solar system?", "Jupiter", s)
        s = quizz("What is the capital of France?", "Paris", s)
        s = quizz("Who wrote 'Romeo and Juliet'?", "William Shakespeare", s)
        s = quizz("What is the boiling point of water in Celsius?", "100", s)
        s = quizz("What is the smallest prime number?", "2", s)
        s = quizz("What is the currency of Japan?", "Yen", s)
        s = quizz("Who painted the Mona Lisa?", "Leonardo da Vinci", s)
        s = quizz("What is the chemical symbol for gold?", "Au", s)
        s = quizz("What is the largest ocean on Earth?", "Pacific Ocean", s)
        print("Your score is",s,"out of 10")
    elif x == "3":
        n = randint(1,100)
        a = 10
        for i in range(a):
            print("Guess the number between 1 and 100 , you have",a-i,"attempts")
            v = int(input(">>> "))
            if v == n:
                print("You are right!")
                break
            elif v < n:
                print("Go higher")
            else:
                print("Go lower!")
    else:
        print("invalid input!")

    print("1- jokes , 2 - quizz , 3 - guess the number, 4 off")
    x = input(">>>")

print("Goodbye !")