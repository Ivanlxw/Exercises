import random

try:
    n = int(input("How many times do you want to flip a coin?  "))
except:
    print("Please enter an integer")
else:
    results=[]
    for i in range(n):
        r = random.randint(0,1)
        if r == 0:
            results.append('H')
        else: 
            results.append('T')
    print(results)
    print("NNumber of heads: {}".format(results.count('H')))
    print("NNumber of tails: {}".format(results.count('T')))
