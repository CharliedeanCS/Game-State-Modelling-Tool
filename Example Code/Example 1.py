from NarrativeStateModel import StateController
device = StateController()
device.read_file("Narrative.json")


device.start_event()


decision = 1
if decision == 1:
        print ("Path 1 : Go Right path")
        print ("Path 2 : Go Left path")
        choice = input("Enter 1 or 2")
        if choice == "1":
            print(device.choose_path(1,int(choice),"Trusting_Advice"))
            print(device.choose_path(decision,int(choice),"Fighting_Bandits"))
        if choice == "2":
            print(device.choose_path(decision,int(choice),"Continuing_On"))
