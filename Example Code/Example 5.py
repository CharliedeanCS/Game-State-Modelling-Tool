from NarrativeStateModel import StateController
device = StateController()
device.read_file("Narrative.json")

device.Create_File()

device.start_event()


line = device.get_line()

decision = 0

def game_choice():
    global decision
    decision = decision +1
    if decision == 1:
        print ("Path 1 : Go Right path")
        print ("Path 2 : Go Left path")
    elif decision == 2:
        print ("Path 1 : Join Rebels")
        print ("Path 2 : Continue without getting involved")
    elif decision == 3:
        print ("Path 1 : Explore the Realm")
        print ("Path 2 : Return to Journey")
    elif decision == 4:
        print ("Path 1 : Fight Dragon")
        print ("Path 2 : Find Alternative")

    a = input("Would you like 1 or 2")
    a = int(a)
    counter = device.path_size(decision,a)
    b=0
    while b < counter:
        print(f"{device.next_path(decision,a)}")
        b = b+1

def start_game():
    global nextstate,line
    while line["State"] != "Defeating_Sorcerer":
                if line["title"] == "Game Narrative":
                    print(device.current_state())
                    device.next_state()
                    line = device.get_line()
                if line["title"] == "Game Branch":
                    game_choice()
                    device.next_NarrativeState()
                    line = device.get_line()
start_game()
