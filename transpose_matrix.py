li=[]
n=int(input("enter the no of rows"))
m=int(input("Enter the no of columns"))
print("Enter first matrix")
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    li.append(l)
lt=[]
for i in range(n):
    for j in range(m):
        lt.append(li[j][i])
print(lt)