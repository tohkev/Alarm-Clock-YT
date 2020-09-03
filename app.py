import time
import webbrowser
import random
import os

#If file not in the folder

if os.path.isfile("YTLinks.txt") == False:
    print("ERROR: YTLinks.txt file not present. Creating file...")
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
    filecreate = os.open("YTLinks.txt", flags)
    with open("YTLinks.txt", 'w') as createdfile:
        createdfile.write("https://www.youtube.com/watch?v=NfuiB52K7X8")

#adds selection of links and check if link you are trying to enter in is already there or not
while True:
    link1 = input("Do you have additional Youtube links you want to add?\nPaste the link here or type 'no'\n")
    with open("YTLinks.txt") as textfile:
        content = textfile.readlines()
    if link1 == "no":
        break
    elif link1 in content:
        print("That link is in here already!")
    else:
        with open("YTLinks.txt", "a") as writedoc:
            writedoc.write("\n" + link1)
        print("Added to the list!")

#sets the time of to be woken up
Time = time.strftime("%H:%M")
print("The current time is " + Time + ".")
alarm = input("What time do you want to wake up?\n(Enter in military time e.g. 13:00)\n")
print("See you in " + alarm + "!")

#opens the .txt file
with open("YTLinks.txt") as textfile:
    content = textfile.readlines()

while Time != alarm:
    print("The time is " + Time + ".")
    Time = time.strftime("%H:%M")
    time.sleep(3)

if Time == alarm:
    print("Time to Wake UP!")
    random_video = random.choice(content)
    webbrowser.open(random_video)
