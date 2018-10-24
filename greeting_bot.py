import random
import string

greetings = ['hola', 'hello', 'hi', "Glad to chat with you", 'hey!','Welcome']
random_greeting = random.choice(greetings)

questions= ["how are you?", "how are you", "how is life?","how is life" ,"how have you been?", "how have you been"]
responses = ['Okay','I am fine','Awesome','fantastic',]
random_response = random.choice(responses)

flag = True
print(" I am your greet bot")

def greeting(sentence):
    if sentence in greetings:
        print(random.choice(greetings))
    elif sentence in questions:
        #print("1")
        responses = ['Okay', 'I am fine', 'Awesome', 'fantastic', ]
        print(random.choice(responses))

    else:
        print("Sorry. I did not understand")


while (flag == True):

    userInput = input(">>> ")
    userInput = userInput.lower()
    #print('the user input is'+ userInput)
    if (userInput != 'bye'):
        if (userInput == 'thanks' or userInput == 'thank you'):
            flag = False
            print(">>>: You are Welcome")
        else:
            greeting(userInput)
    else:
        flag = False
        print(" Bye! take care..")