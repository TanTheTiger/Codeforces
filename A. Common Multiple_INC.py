t = int(input())
s = 0
for i in range(t):
    n = int(input())
    array = input().split(" ")
    array = [int(i) for i in array]
    opres = array[0]
    # GCD Process for a,b
    for i in range(n-1): #Loops through the array for one test case
        a = max(opres, array[i+1])
        b = min(opres, array[i+1]) # a is the previous number and b is the next number
        while a % b != 0:
            b, a = a % b, b
        opres = (abs(opres*array[i+1]))/b #LCM from GCD
    print(opres)