str=input('Enter your name: ')
char=input('Enter character you want me to search: ')
i = 0 
count = 0
while i < len(str):
    if str[i] == char:
        count+=1 
    i = i+1

print(char,count)