# Assignment 1 : Using for loop please print all the prime numbers between 1-200 using FOR LOOP AND RANGE function

flag=False

for num in range(2,200):
    for i in range(2,num):
        if(num % i==0):
            flag=True
            break
    else:
        print(num)
            

