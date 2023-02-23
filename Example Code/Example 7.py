from NarrativeStateModel import StateController
device = StateController()
device.read_file("Narrative.json")
device.Create_File()
device.start_event()

choice = 1

def GameChoice():
    global choice
    if choice < 6:
        if choice == 1:
            print(device.current_state())
            print("Path 1 = Left")
            print("Path 2 = Right")
            path = input("Path 1 or 2: ")
            intPath = int(path)
            if intPath == 1:
                print("Going Left")
                print(device.choose_path(choice,intPath,"Trusting_Advice"))
                print(device.choose_path(choice,intPath,"Fighting_Bandits"))
            if intPath == 2:
                print("Going Right")
                print(device.choose_path(choice,intPath,"Continuing_On"))
            choice += 1
            GameChoice()
        if choice == 2:
            print(device.pick_state("Meeting_Rebels"))
            print ("Path 1 : Join Rebels")
            print ("Path 2 : Continue without getting involved")
            path = input("Path 1 or 2: ")
            intPath = int(path)
            if intPath == 1:
                print(device.choose_path(2,1,"Joining_Rebels"))
                print(device.choose_path(2,1,"Investigating_Cave"))
            if intPath == 2:
                print(device.choose_path(2,2,"Continuing_On2"))
            choice += 1
            GameChoice()
        if choice == 3:
            print(device.pick_state("Meeting_Helper"))
            print(device.pick_state("Entering_Portal"))
            print ("Path 1 : Explore the Realm")
            print ("Path 2 : Return to Journey")
            path = input("Path 1 or 2: ")
            intPath = int(path)
            if intPath == 1:
                print(device.choose_path(3,1,"Exploring_Realm"))
                print(device.choose_path(3,1,"Negotiating_With_Trolls"))
                print(device.choose_path(3,1,"Seeking_Artifact"))
            if intPath == 2:
                print(device.choose_path(3,2,"Returning_To_Journey"))
            choice += 1
            GameChoice()
        if choice == 4:
            print(device.pick_state("Encountering_Dragon"))
            print ("Path 1 : Fight Dragon")
            print ("Path 2 : Find Alternative")
            path = input("Path 1 or 2: ")
            intPath = int(path)
            if intPath == 1:
                print(device.choose_path(4,1,"Defeating_Dragon"))
                print(device.choose_path(4,1,"Dragon_Defeated"))
            if intPath == 2:
                print(device.choose_path(4,2,"Finding_Alternative"))
                print(device.choose_path(4,2,"Sneaking_Past_Dragon"))
                print(device.choose_path(4,2,"Treasure"))
            choice += 1
            GameChoice()
        if choice == 5:
            print(device.pick_state("Meeting_Fairies"))
            print(device.pick_state("Facing_Challenges"))
            print(device.pick_state("Defeating_Sorcerer"))
            choice += 1

GameChoice()
