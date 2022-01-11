
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['@','#','$','%','<','^','<','&','*','~','<','>']
numbers=[1,2,3,4,5,6,7,8,9,0]
count=0
print("Welcome to the pypassword generator!")
nr_letters=int(input("How many letters would you like in your password"))
nr_symbols=int(input("How many symbols would you like in your password"))
nr_numbers=int(input("How many numbers would you like in your password"))
newlist=[]
for i in range(1,(nr_letters+1)):
    n=random.choice(letters)
    newlist.append(n)
    count=count+1
for i in range(1,(nr_symbols+1)):
    n=random.choice(symbols)
    newlist.append(n)
    count = count + 1
for i in range(1,(nr_numbers+1)):
    n=str(random.choice(numbers))
    newlist.append(n)
    count = count + 1
random.shuffle(newlist)
password=""
for i in newlist:
    password=password+i
print(f"The password is:{password}")