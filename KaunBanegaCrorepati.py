questions = ["Who is Prime Minister Of India?","What is Capital Of India?","Who is first Man Who step on the moon?"]
answers = [1,2,3]
import random
ran = random.randint(0,2)

options = [["Narendra Modi", "Droupadi Murmu", "Amit Shah", "Ramnath Kovind"],
           ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
           ["Buzz Aldrin", "Rakesh Sharma", "Neil Armstrong", "Yuri Gagarin"]]

wel = "Welcome To QuestionHome"
print(wel)

j = 1
print("Q.No",questions[ran])
for i in options[ran]:
    print(j,i)
    j += 1

guess = int(input("What is your answer: "))
if 1 <= guess <= 4:
    if guess == answers[ran]:
        print("Well Done Brother.")

    else:
        print("Wrong!!")
else:
    print("Invalid Option")
