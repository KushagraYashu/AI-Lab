li=[]
n=int(input("enter the no of rows"))
m=int(input("Enter the no of columns"))
print("Enter first matrix")
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    li.append(l)
li2=[]
print("Enter second matrix")
for i in range(n):
    l=[]
    l=list(map(int,input().split()))
    li2.append(l)
for i in range(n):
    for j in range(m):
        li[i][j]+=li2[i][j]
for i in li:
    print(i)
