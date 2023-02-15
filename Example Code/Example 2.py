from NarrativeStateModel import StateController
device = StateController()
device.read_file("Narrative.json")


device.start_event()

forward = input("Would you like to proceed")
if forward == "yes":
    print(device.pick_state("Meeting_Fairies"))
    device.save_game_state()
