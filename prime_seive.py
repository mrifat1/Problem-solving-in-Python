def SieveofE(n):
    p = 2
    prime[0] = False
    prime[1] = False
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1


n = int(input())
prime = [True for i in range(n + 1)]
SieveofE(n)
for i in range(n+1):
    if prime[i]==True:
        print("Numbers:",i,"Prime Activity:",prime[i])

