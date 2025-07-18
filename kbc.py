#date: 14 jan 2025

approach=int(input("there are 3 approach, enter 1/2/3 for desired one:-  "))
#most efficient one
if approach==1:
    questions = {
        "What is the capital of France?  a)paris   b)london   c)india:-  ":"paris",
        "What is 2 + 2? ": "4",
        "What is the color of the sky on a clear day? ": "blue"
    }
    score = 0
    consecutive_wrong = 0
    for question, answer in questions.items():
        user_answer = (input(question)).strip().lower()
        if user_answer == answer:
            print("Correct!")
            score += 1
            consecutive_wrong = 0
        else:
            print("Wrong answer.")
            consecutive_wrong += 1
        if consecutive_wrong == 2:
            print("You got two wrong answers in a row. Game over!")
            break
    print("Your final score:", score)
    print("Your wrong answer", 3-score)

    #least efficient one
elif approach==2:
    print('''your first question is on your screen:
    1)who is the PM of India?
    a)Modi
    b)Danis bhai
    c)Oggy Adityanath
    d)Rahul Gandhi''')
    q1 = input("choose your answer")
    if (q1 == 'a'):
        w1 = 10
        print("you are correct and you won 10 rupees.")
    elif (q1 != 'a'):
        w1 = 0
        print("your answer is incorrect")

    print('''your next question is:
    how many molecules of hydrogen present in water?
    a)1
    b)4
    c)2
    d)9''')
    q2 = input("choose your option")
    if (q2 == 'c'):
        w2 = 15
        print("your option is correct and you won 15 rupees")
    elif (q2 != 'c'):
        w2 = 0
        print("you answer is incorrect")
    s1 = w1 + w2
    if (s1 == 0):
        print("game over")
        print("your winning amount is:")
        print(w1 + w2)
        exit()
    print('''your next question is:
    what is the integral of cos(x)?
    a)sin(x)
    b)cos(x)+c
    c)tan(x)+c
    d)sin(x)+c''')
    q3 = input("choose your option")
    if (q3 == 'd'):
        w3 = 20
        print("you are correct and you won 20 rupees.")
    elif (q3 != 'd'):
        w3 = 0
        print("your answer is incorrect")
    s2 = w3 + w2
    if (s2 == 0):
        print("game overe")
        print("your winning amount is:")
        print(w1 + w2 + w3)
        exit()
    print('''your next question is:
    how many bones are their in human body?
    a)1000
    b)207
    c)206
    d)106''')
    q4 = input('choose your option')

    if (q4 == 'c'):
        w4 = 25
        print("you are correct and won 25 rupees")
    elif (q4 != "c"):
        w4 = 0
        print("you are incorrect")
    s3 = w3 + w4
    if (s3 == 0):
        print('game over')
        print("your winning amount is:")
        print(w1 + w2 + w3 + w4)
        exit()
    print('''next is our special round and conditions of next round is:
    if your answer of next round question is correct then you will win 30 more rupees and if your answer is incorrect then you will lose your all amount you won.''')
    k = input("do you still want to cintinue the game?")
    if (k == 'yes'):
        print('''your question of special round is :
        what is the formula of focal lenght of a spherical mirror?
    a= r/2
        b= r
        c= 2r/3
        d= r/4''')

        q5 = input("choose your option ")

        if (q5 == 'a'):
            w5 = 30
            print("your answer is correct")
            print("you have won :")
            print(w1 + w2 + w3 + w4 + w5)

        elif (q5 != 'a'):
            print("you are incorrect and you lost your all winning amount")

    elif (k == 'no'):
        print('ok! then game is over now')
        print("you have won:")
        print(w1 + w2 + w3 + w4)
        exit

    #third approach
elif approach==3:
    pointz:int =0
    a,b,c,d= False,False,False,False
    print(f"your current point is {pointz}")
    questions={"que1":"in which year modi's third term prime minister of india? a) 2018  b)2024  c)2014  d)2001",
               "que2":"enter 5th prime no.",
               "que3":"what is the 6th odd  no. ",
               "que4":"which month july is? "}
    print(questions["que1"])
    ans1=input("enter your answer:-  ")
    if ans1=="b":
        pointz += 1
        print(f"you won!!!   your current score is {pointz}")
    else:
        print("wrong answer!!!!  only one chance left")

    print(questions["que2"])
    ans2=int(input("enter your answer:-   "))
    if ans2==11:
        pointz += 1
        print(f"yeah! you won again!!!   and you current score is {pointz}")
        a = True
    else:
        print(f"you lost!!! and your current score is {pointz} ")

    if pointz >= 1:
        print(questions["que3"])
        ans3=int(input("enter your answer here:-   "))
        if ans3==11:
            pointz += 1
            print(f"wohhh! you won...    your current score is {pointz}")
        else:
            if not a:
                pointz=0
                print(f"game over!!!    your current point is {pointz}")
            else:
                print(f"you lost!!!   and your current score is {pointz}")
else:
    print("wrong choice")

