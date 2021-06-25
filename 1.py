num=int(input("ENTER THE NUMBER:"))
current=1
for i in range(1,num+1):
    for j in range(1,i+1):
        print(current,end=" ")
        current+=1
    print("\r")