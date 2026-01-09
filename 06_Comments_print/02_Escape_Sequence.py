#Let's learn Escape Sequence chracters

#print("How are you?
#      I am good")   AKHI WE CAN'T TERMINATE STRING LITERAL IN THE NEXT LINE PY

print("Hey how are you?\nI am fine") #\n

print("Hey how are you?\nI am fine\\newline") #If we want\ literally in output, putdouble \\ and it wil consider double \\ as \

print("I am a Data Scientist\tI mean pursuing one") #\t

print("I am a Data Scientist\"I mean pursuing it") #\"

print("A stranger asked me \"Where do you live India?\"")

print('Hey there "Bro"') #Opposite quotes doesn't terminates (doesn't creates error) each other

print(3,12,2025, sep="|")
#Let's use sep"" with an e.g. file location
print("Home","Dekstop", "CWH", "02_Escape_Sequence", sep=" > ")
#sep="" after every element and end="" after the last element
print("Hey", "Hello", "World", sep=",", end="!") 