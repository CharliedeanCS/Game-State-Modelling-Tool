# NarrativeStateModel.py
import json
import argparse


saveddecision = 0


Statesreached = []
Lines = []
States = []
NarrativeStates = []
Paths = []
current_path = []


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

    def path_size(self,decision,path):
        counter = 0
        for line in data["Narrative"]:
         if line["title"] == "Game Branch":
            if line["decision"] == decision:
                if line["path"] == path:
                    counter = counter +1;
        return counter
        


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

    def display_game_path(self):
      global Statesreached
      for line in data["Narrative"]:
          if line["description"] == self.state:
            Statesreached.append(line["State"])
            break;
          else:
            if line["State"] in Paths or line["title"] == "Game Narrative":  
              Statesreached.append(line["State"]) 
      print("Game path:")
      for line in data["Narrative"]:
            if line["State"] in Statesreached:
                print(f"- {line['State']}")

    def current_state(self):
        return self.state

    def save_game_state(self):
        state_data = {
            "current_state": self.state,
            "current_line": current_line,
            "Paths": Paths,
            "Statesreached": Statesreached,
            "Lines": Lines,
            "States": States,
            "NarrativeStates": NarrativeStates
        }
        with open("save_data.json", "w") as f:
            json.dump(state_data, f)

    def load_game_state(self):
        global Paths,NarrativeStates,States,Lines,Statesreached,current_line
        with open("save_data.json") as f:
            state_data = json.load(f)
        self.state = state_data["current_state"]
        current_line = state_data["current_line"]
        Statesreached = state_data["Statesreached"]
        Lines =  state_data["Lines"]
        States =  state_data["States"]
        NarrativeStates =  state_data["NarrativeStates"] 
        Paths = state_data["Paths"]
    
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

    def next_state(self):
        global current_line,current
        index = 0
        try:
            for line in data["Narrative"]:
                if line["description"] == self.state:
                    break
                else:
                    index = index + 1
            for line in data["Narrative"]:
                if line["State"] == States[index+1]:
                    self.state = line["description"]
                    current_line = line
                    current = self.state

            return self.state
        except:
            return 0
    
    def state_reached(self,state):
      global Statesreached 
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

    def next_NarrativeState(self):
        global current_line,current
        index = 0
        for line in data["Narrative"]:
            if line["description"] == self.state:
                break
            else:
                index = index + 1
        try:
            for line in data["Narrative"]:
                if line["State"] == States[index+1]:
                    if line["title"] == "Game Narrative":
                        self.state = line["description"]
                        current_line = line
                        current = self.state
                    else:
                        index = index + 1

            return self.state
        except:
            return 0
             
    def pick_state(self,state_name):
        global current_line
        found_state = False
        for line in data["Narrative"]:
            if line["title"] == "Game Narrative" and line["State"] == state_name:
                self.state = line["description"]
                current_line = line
                found_state = True
                return self.state
                break
        if not found_state:
            return f"Error: Could not find state with name '{state_name}'"
      
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
                    
    def next_path(self,decision,path):
          global data,current_path,Paths,current_pathstate,saveddecision
          indexcount = 0
          if decision != saveddecision and saveddecision != 0:
              current_path.clear()
              saveddecision = decision
          if saveddecision == 0 or decision == saveddecision:
              saveddecision = decision
              for line in data["Narrative"]:
                 if line["title"] == "Game Branch":
                   if line["decision"] == decision:
                     if line["path"] == path:
                       Paths.append(line["State"])
              if bool(current_path) == False:
                for line in data["Narrative"]:
                 if line["title"] == "Game Branch":
                   if line["decision"] == decision:
                       if line["path"] == path:
                           current_path.append(line["description"])
                           current_pathstate = line["State"]
                           return current_path[0]
                           break
              else:
                for state in Paths:
                    if state == current_pathstate:
                        path = Paths[indexcount+1]
                        for line in data["Narrative"]:
                           if line["State"] == path:
                               current_path[0] = line["description"]
                               current_pathstate = line["State"]
                               return current_path[0]
                               break
                        break
                    else:
                        indexcount = indexcount +1

              
              
          

parser = argparse.ArgumentParser()
args = parser.parse_args()
                    
             





