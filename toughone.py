
flag = [0 for i in range (100)]
for i in range(1,10):
    if i<=5:
        print(i)
        if i==5:
            flag[i]=1
            j = i-1

    else:
        print(j)
        j-=1

