n=int(input("Enter Jug 1 capacity: "))
m=int(input("Enter Jug 2 capacity: "))
j1,j2,j1Cap,j2Cap = 0,0,n,m

target=int(input("Enter target value: "))

print("1. Fill Jug 1")
print("2. Fill Jug 2")
print("3. Empty Jug 1")
print("4. Empty Jug 2")
print("5. Transfer Jug 1 to Jug 2")
print("6. Transfer Jug 2 to Jug 1")

while j1!=target and j2!=target:
    ch = int(input("Enter choice: "))
    
    if ch==1:
        j1=j1Cap
        
    elif ch==2:
        j2=j2Cap
        
    elif ch==3:
        j1=0
        
    elif ch==4:
        j2=0
        
    elif ch==5:
        tmp=j2
        j2 = min(j1+j2, j2Cap)
        j1 = max(0,j1 - (j2Cap-tmp))
        
        #SIMPLIFIED
        # tmp = j2+j1
        # if(tmp>j2Cap):
        #     j1 = j1 - (j2Cap-j2)
        #     j2 = j2Cap
        # elif tmp==j2Cap:
        #     j1=0
        #     j2=j2Cap
        # else:
        #     j2=tmp
        #     j1=0
    
    
    elif ch==6:
        
        tmp=j1
        j1 = min(j1+j2, j1Cap)
        j2 = max(0,j2 - (j1Cap-tmp))
        
        #SIMPLIFIED
        # tmp = j2+j1
        # if(tmp>j1Cap):
        #     j2 = j2 - (j1Cap-j1)
        #     j1 = j1Cap
        # elif tmp==j1Cap:
        #     j2=0
        #     j1=j1Cap
        # else:
        #     j1=tmp
        #     j2=0
        
        
    print(j1,j2)
