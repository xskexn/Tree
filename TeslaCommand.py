#simple tesla engine
import random
#imported random for music choise
command = ""
print("HI, WELLCOME TO TESLA" + "\n"
      "I'm your Assistent ")
#music radio engine
musicplay = ["Badge Of A Chance", "Kiss Of The World","Thrill Of The Dusty Road" , "Gamble Of The Country","For Her Own Way", "772 Love", "suicidal", "Hide"]
music = random.choice(musicplay)
#start engine
while command.lower() != "off":
    command = input("Command Please:> ")
    if command.lower() == "start":
        print("Car is starting..." )
    elif command.lower() == "sleep":
        print("Car is on sleep mode...")
    elif command.lower() == "play":
        play = print("Now Playing... "+ music)
    elif command.lower() == "help":
        print("Input command ""Help"" for help" + "\n"
              "Start"" to start the car" + "\n"
              "Off"" to turn it off" + "\n"
              "Sleep"" to set in power saving" + "\n"
              """play to play Music""")
    elif command.lower() == "off":
        print("Car is stopping, Good bye!")
    else:
        print("Hey please input a valid key")