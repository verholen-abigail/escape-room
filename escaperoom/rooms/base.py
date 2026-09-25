class Room:
    def __init__(self, name, doors, items):
        self.name = name
        self.doors = doors
        self.items = items

    def arrival(self):
        return "string you get by entering"

    def look(self):
            return "string you get by looking"

    def doors(self):
            return "string of doors"

    def items(self):
                return "string of items"

base = Room("Intro Lobby", ["soc", "dns", "vault", "malware", "final"],
          [])
