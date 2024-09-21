lk = int(input("what are you serching for "))

print("...")
print("...")
print("...")

lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

L = 1
R = int(len(lis))
M = (L + R) // 2

rep = True
fir = True
count = 0

while (rep == True):

    count += 1

    if (lk == lis[M - 1]):
        print("...")
        print("...")
        print("...")
        print("Number " + str(lis[M - 1]) + " finded")
        print(str(M - 1) + "th index")
        print("done in "+ str(count) +" operations")
        rep = False

    elif (lk < lis[M - 1]):
        R = M - 1
        print(lis[L - 1:R])
    
    elif (lk > lis[M - 1]):
        L = M + 1
        print(lis[L - 1:R])

    else:
        rep = False
        print("error")

    M = (L + R) // 2
