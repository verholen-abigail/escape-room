class Room:
    def __init__(self, name, doors, items, description):
        self.name = name
        self.description = description
        self.doors = doors
        self.items = items

    def get_token():
        return ""

    def arrival(self):
        message = f"You enter {self.name}.\n{self.description}\nDoors lead to: " + ", ".join(self.doors)

        if self.items:
               message += "\nItems here : " + ", ".join(self.items)
        return message

    def look(self):
        message = f"You are in {self.name}.\n{self.description}\nDoors lead to: " + ", ".join(self.doors)

        if self.items:
             message += "\nItems here: " + ", ".join(self.items)
        return message