from my_states import StateController
device = StateController()
device.read_file("Person.json")
device.start_event()

