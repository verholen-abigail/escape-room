class Room:
    def __init__(self, name, doors, items, dscr):
        self.name = name
        self.doors = doors
        self.items = items
        self.dscr = dscr

    def arrival(self):
        str = "You enter the" + self.name
        if(not self.dscr):
           str += self.dscr
        return str

    def look(self):
            str = "You are in the" + self.name +". \n"
            if(not self.doors.empty):
                str += "Doors lead to:" + self.get_doors + ". \n"
            if(not self.items.empty):
                str += "Items avalible in the room are:" + self.get_items + ". \n"
                                
            
            return str

    def get_doors(self):
            return self.doors

    def get_items(self):
                return self.items

base = Room("Intro Lobby", ["soc", "dns", "vault", "malware", "final"],
          [])
