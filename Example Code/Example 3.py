from NarrativeStateModel import StateController
device = StateController()
device.read_file("Narrative.json")

device.start_event()

device.load_game_state()

print(device.current_state())
