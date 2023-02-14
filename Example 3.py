from my_states import StateController
device = StateController()
device.read_file("Person.json")

device.start_event()

device.load_game_state()

print(device.current_state())
