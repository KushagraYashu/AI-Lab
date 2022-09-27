i = int(input("Enter a number: "))

if i == 0:
    print("1")
    exit()

for j in range(i-1, 0, -1):
    i = i*j

print(i)