import os
import random
from datetime import datetime as dt

chat = True
while chat:
    msg = input("Enter your message : ")

    if msg == "hello" or msg == "hi" or msg == "hey":
        print("Hello User")
    elif msg == "play music" or msg == "play song":
        os.chdir(r"C:\Users\ASUS PC\Music")
        songs = os.listdir()
        song = random.choice(songs)
        print("Playing :",song)
        os.startfile(song)
    elif msg == "show songs":
        os.chdir(r"C:\Users\ASUS PC\Music")
        songs = os.listdir()
        for i in range(len(songs)):
            print(i, ":", songs[i])
        index = int(input("Enter the song number you want to play : "))
        song = songs[index]
        print("Playing :",song)
        os.startfile(song)
    elif msg == "date":
        d = dt.now().date()
        print("Date is",d.strftime('%d/%m/%y, %A'))
    elif msg == "time":
        t = dt.now().time()
        print("Time is",t.strftime('%H:%M:%S, %p'))
    elif msg == "bye":
        print("Bye User")
        chat = False
    else:
        print("I don't understand")
