i = int(input("Enter a number: "))

for j in range(2, int((i/2)+1)):
    if i%j == 0:
        print("Not Prime")
        exit()

print("Prime")