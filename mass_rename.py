import os
counter = 0

location = input("Where are the files you would like to rename? ")
for i in os.listdir(location):
    print(str(i))
prefix = input("What do you want the prefix to be? ")
for i in os.listdir(location):
    args = i.split('.')
    os.rename(str(location)+'\\'+str(i), str(location)+'\\'+str(prefix)+str(counter)+'.'+str(args[1]))
    counter = counter + 1
    
for i in os.listdir(location):
    print(str(i))





