import time
print ("Hello, and welcome to the Age Calculator")
time.sleep(3)
print ("May a Please have you name?")
time.sleep(3)
name=input("Name: ")
print ("Nice to meet", name)
time.sleep(3)
print ("To make this program wokr i Need you Age?")
time.sleep(4)
age=int(input("Age: "))
days = age * 365
minutes = age * 525948
seconds = age * 31556926
print (name, "You have lived on this planet for: ", days,"days", minutes, "minutes and", seconds, "seconds! Wow!")
