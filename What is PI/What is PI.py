import time
print("Hello, People of Earth")
time.sleep(3)
print("My name is  PythonBot")
time.sleep(2)
name=input("What i your name: ")
print("-----------------------------------------------------")
print("Nice to Meet You", name)
print("-----------------------------------------------------")
time.sleep(2)
print(name, "I have a question for you?")
time.sleep(2)
print("Do you know what PI")
answer = None
while answer not in ("yes", "no"):
    answer = input("Respond with yes or no: ")
if answer == "yes":
    print("Great, I hope you have a wonderful day!!!")
elif answer == "no":
    print("Do you need more information about PI")
    answer = None
    while answer not in ("yes", "no"):
        answer = input("Respond with yes or no: ")
    if answer == "yes":
        print("GOGGLELING YOU QUESTION")
        time.sleep(3)
        print("Here's you Answer:")
        print("-----------------------------------------------------")
        print("Pi is the ratio of a circle's circumference to its diameter. Regardless of the size of the circle,")
        print("pi is always the same number. ... Pi is also an irrational number,")
        print("which means that its value cannot be expressed exactly as a simple fraction.")
        print("As a result, pi is an infinite decimal.")
        print("-----------------------------------------------------")
        time.sleep(5)
    answer = None
    while answer not in("yes", "no"):
        answer = input("Did That answer your question: ")
    if answer == "yes":
        print("Great, i hope you have the most amazing day!!!")
    elif answer == "no":
        print("I'm sorry about that")
        time.sleep(2)
        print("ERROR 404")
    else:
        print("I can't give you an answer if you don't respond correctly!")
        time.sleep(3)
        answer = input("Respond with yes or no: ")