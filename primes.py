import time
currentnumber = 1            # won't work if you increase
prime = []                   # all primes stored here
ticklimit = -1               # how many primes are currently stored (don't ask why its negative)
check2 = True                # this can almost definitely be removed
y = "y"
n = "n"
print("*"*26,"\n*\tPrime number tester  *\n**************************")
input2 = input("do you want all prime numbers listed y/n:")
if input2 == y:
    show = True
elif input2 == n:
    show = False
else:
    print("please restart and enter a valid answer")
    time.sleep(10)
    exit()
userinput = input("enter a valid number less than 1000000:")
try:                                      # avoiding errors
    userinput = int(userinput)
except:
    print("please restart and enter a valid number")
    time.sleep(10)
    exit()
if userinput < 1 or userinput > 1000000:  # avoiding errors
    print("please restart and enter a valid number")
    time.sleep(10)
    exit()
else:
    while currentnumber < 1000000:  # change this to change limit of checked numbers
        check = False               # don't know why i'm defining this again but whatever(doesn't work if you remove it)
        tick = 0                    # what prime number in the list is being checked
        while tick <= ticklimit != -1 and check is False:  # the actual checking prime factors loop
            check2 = False
            if currentnumber % prime[tick] == 0 and prime[tick] != 1 and currentnumber != 1:
                if currentnumber == userinput:
                    factor = prime[tick]
                check = 0
            elif tick < ticklimit:
                tick = tick + 1
                check = False
            else:
                check = True
                tick = 0

        if currentnumber != 1 and check2 is True or check is True:  # if the number's prime
            if currentnumber == userinput and show is False:
                print(userinput, "is prime")
                time.sleep(10)
                exit()
            elif currentnumber == userinput and show is True:
                print(userinput, "is prime")
                print("primes less than", userinput, "are:")
                print(prime)
                time.sleep(10)
                exit()
            check = False
            prime.append(currentnumber)
            currentnumber = currentnumber + 1
            ticklimit = ticklimit + 1
        elif currentnumber == 1:                              # if it's one (1)
            if userinput == 1:
                print("1 isn't prime for some reason")
                time.sleep(10)
                exit()
            check = False
            currentnumber = currentnumber + 1
        else:                                                 # if it's some other integer
            if currentnumber == userinput and show is False:
                print(userinput, "isn't prime")
                print(factor, "and", int(userinput/factor), "are factors of", userinput)
                time.sleep(10)
                exit()
            elif currentnumber == userinput and show is True:
                print(userinput, "isn't prime")
                print(factor, "and", int(userinput / factor), "are factors of", userinput)
                print("primes less than", userinput, "are:")
                print(prime)
                time.sleep(10)
                exit()
            currentnumber = currentnumber + 1