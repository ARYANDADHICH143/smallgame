command=""
started=False
while True:
    command = input (">").lower()
    if command== "start":
        if started:
            print("car is already started")
        else:
            started=True
            print("car is started ")
    elif command== "stop":
        if not started:
            print("car is already stopped kya kar raha h bhai")
        else:
            started=False
            print("car is stoped")
    elif command== "help":
        print("""      
start - start the car
stop- stop the car 
quit- quit the game """)
    elif command=="quit":
        break
else:
    print("sorry i not understand that ")