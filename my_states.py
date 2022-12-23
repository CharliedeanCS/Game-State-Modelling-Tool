# my_states.py


from state import State
import json
import argparse




StateReached = []
Lines = []
States = []
NarrativeStates = []
Paths = []


class StateController():

    def __init__(self):
     print ('Processing current state:'), str(self)

    def Create_File(self):
      global data
      with open('YourStates.txt', 'w') as f:
       f.write('')
      with open("YourStates.txt", "a") as file2:
       iterator = 0
       check = 0
       for line in data["Narrative"]:
          if line["title"] == "Game Narrative":
            if check == 1:
              file2.write("End of Decision" + "\n")
            iterator = iterator + 1;
            file2.write("State" + str(iterator) + ": " + line["State"] + "\n")
            check = 0
          else:
            iterator = iterator + 1;
            if check == 0:
              file2.write("Decision: "+str(line["decision"]) + "\n")
            file2.write("State" + str(iterator) + ": " + "Path-" + str(line["path"]) + ": " + line["State"] + "\n")
            check = 1
       return True
  
    def read_file(self,file):
      global data
      with open(file) as file:
        data = json.load(file)

      for line in data["Narrative"]:
        States.append(line["State"])
        if line["title"] == "Game Narrative":
          NarrativeStates.append(line["State"])
          Lines.append(line["description"])
      self.Create_File()


    def states_between(self,State1,State2):
       global States,Paths
       itera = 0
       itera_2 = 0
       StatesBetween = []
       for line in data["Narrative"]:
         if line["State"] == State1:
           break
         else:
           itera = itera + 1;
       for line in data["Narrative"]:
         if line["State"] == State2:
           break
         else:
           itera_2 = itera_2 + 1;
       while itera < itera_2-1:
        itera = itera +1;
        if States[itera] in Paths or States[itera] in NarrativeStates:
          StatesBetween.append(States[itera])
       while itera_2 < itera - 1:
        itera = itera -1;
        if States[itera] in Paths or States[itera] in NarrativeStates:
          StatesBetween.append(States[itera])    
       return StatesBetween


    def state_reached(self,state):
      Statesreached = []
      for line in data["Narrative"]:
          if line["description"] == self.state:
            Statesreached.append(line["State"])
            break;
          else:
            if line["State"] in Paths or line["title"] == "Game Narrative":  
              Statesreached.append(line["State"])             
      for states in Statesreached:
        if states == state:
          return True
      return False


    
    def start_event(self):
        global current,current_line
        for line in data["Narrative"]:
          current = line["description"]
          current_line = line
          self.state = current
          break
        return current

    def get_line(self):
      global current_line
      return current_line
       
    def pick_state(self,state_name):
          global Lines,States,current_line
          for line in data["Narrative"]:
             if line["title"] == "Game Narrative":
               if line["State"] == state_name:
                 self.state = line["description"]
                 current_line = line
                 return self.state
      
    def choose_path(self,decision,path,state_name):
          global data,current_line,Paths
          for line in data["Narrative"]:
             if line["title"] == "Game Branch":
               if line["decision"] == decision:
                 if line["path"] == path:
                   Paths.append(line["State"])
                   if line["State"] == state_name:
                     self.state = line["description"]
                     current_line = line
                     return self.state

parser = argparse.ArgumentParser()
args = parser.parse_args()
                    
             





