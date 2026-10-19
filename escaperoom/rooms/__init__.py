class Room:
    def __init__(self, name, description, doors, items, locked=False, required_item=None):
        self.name = name
        self.description = description
        self.doors = doors
        self.items = items
        self.locked = locked
        self.required_item = required_item

    def arrival(self):
        message = f"You enter the {self.name}.\n{self.description}\nDoors lead to: " + ", ".join(self.doors)

        if self.items:
               message += "\nItems here : " + ", ".join(self.items)
        return message

    def look(self):
        message = f"You are in the {self.name}.\n{self.description}\nDoors lead to: " + ", ".join(self.doors)

        if self.items:
             message += "\nItems here: " + ", ".join(self.items)
        return message