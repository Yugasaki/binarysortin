lk = input("for what are you looking ") 
iit = True
try:
    int(lk)
except:
    iit = False

if (iit == True):
    lk = int(lk)

lis = [1,2,3,4,5,6,7,8,10,11,12]

l = 0    # Left
r = len(lis) - 1    #Right
mid = None  #mid that we use to astablish numbers

count = 0
rep = True
done = False
numberNotExist = False
lr = []
rl =[]
oldl = None
oldr = None
while (rep == True and iit == True): #The iit is checked to chek it is int

    count += 1
    mid = (l + r) // 2
    rl.append(l)
    rl.append(r)

    if (count > 1 and lr == rl):
        print("this work")
    rl.clear
    if (lk == lis[mid]):
        print(lis[l:r])
        print("done in ",count," operations")
        rep = False
        
    elif (lk < lis[mid]):
        r = mid - 1
        print(lis[l:r + 1],mid + 1)
        if (oldl == l and oldr == r):
            print("number dont exist")
            rep = False
        else:
            oldr = r
            oldl = l


    elif (lk > lis[mid]):
        l = mid + 1
        print(mid + 1,lis[l:r + 1])
        if (oldl == l and oldr == r):
            print("number not exist")
            rep = False
        else:
            oldr = r
            oldl = l
