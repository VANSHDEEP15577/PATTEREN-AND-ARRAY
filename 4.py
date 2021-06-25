num=int(input("ENTER THE NUMBER:"))
for i in range(num+1,0,-1):
    for j in range(1,i):
        print(num,end=" ")
    print("\r")