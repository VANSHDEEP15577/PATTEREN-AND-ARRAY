num=int(input("ENTER THE NUMBER:"))
current=0
for i in range(num,0,-1):
    current+=1
    for j in range(1,i+1):
        print(current,end=" ")
    print("\r")