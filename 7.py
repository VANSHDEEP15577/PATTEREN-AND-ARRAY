num=int(input("ENTER THE NUMBER:"))
for i in range(0,num):
    for j in range(num-i,0,-1):
        print(j,end=" ")
    print("\r")