def maxnumber():
    maxi = randomarray[0]
    for i in range(1,n):
        if randomarray[i]>maxi:
            maxi = randomarray[i]
    return maxi
def minnumber():
    min = randomarray[0]
    for i in range(1,n):
        if randomarray[i]<min:
            min = randomarray[i]
    return min

n  = int(input())
randomarray = []
for i in range(n):
    m = int(input())
    randomarray.append(m)

print("Print the maximum number:",maxnumber())
print("Print the minimum number:",minnumber())


