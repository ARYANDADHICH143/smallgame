
secret_number=5
i=0
j=3
while i<j:
    guess= int(input("guess:"))
    i=i+1
    if guess==secret_number:
        print("you wonnnnn")
        break
else:
    print("sorry! you failed")

input("press enter to exit")

