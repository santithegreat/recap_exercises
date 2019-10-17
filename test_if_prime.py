import random
print("This program asks for a number and tests if it is prime")
while True:
    try:
        read_line = input("Please give me an integer number")
        num = int(read_line)
    except ValueError:
        print("That was not a valid integer number")
        continue
    break
for i in range (2, num // 2):
    prime = True
    if num % i == 0:
        print("The number", num, "is not prime")
        prime = False
        break

if prime==True:
    print("The number", num, "is prime")

i=0
while i < 100:
    rand = int(random.random()*100)
    prime = True
    i+=1
    for f in range(2, rand // 2):
        if rand % f == 0:
            prime = False
    if prime==True:
        print(rand)
# generate 100 numbers, print only the prime ones
