#Holly Cheek
#18 November 2017 @ DjangoGirls Santa Barbara 2017

#Selects a random participant to win the Microsoft Bluetooth Speaker



import random

file = open('djangoParticipants.txt', 'r')
s = file.read()
names=set(s.split('\n'))
L=[]
for i in names:
    L.append(i)
comment = "Here is a list of all participants from today:"
comment1 = "And our winner is... "
print(comment + ('\n'*2 ))
print(L)
print('\n'*2 )
print(comment1 + random.choice(L) + ('\n'*2) + "Congratulations!" + '\n')





