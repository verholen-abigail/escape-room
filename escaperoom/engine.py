class Engine:
    def __init__(self, rooms, intro):
        self.rooms = rooms
        self.current_room = intro
        self.inventory = []
        self.running = True
        self.hints = []
        self.tokens = []

    def help(self):
        print("""look \nmove <room> \ninspect <item in room> \nuse <item in inventory>
            \ninventory \nhint \nsave \nload \nquit""")
        return

    def look(self):
        return self.current_room.look()

    def move(self, room):
            if room not in self.rooms :
                print(f"{room} does not exist.")
                return
            
            if room not in self.current_room.doors:
                print(f"You cannot go to {room} from here.")
                return
            
            destination = self.rooms[room]
            if destination.locked:
                if destination.required_item not in self.inventory:
                    print(f"The {room} is locked. You need {destination.required_item}.")
                    return
            self.current_room = destination
            print(self.current_room.arrival())

    def inspect(self, item):
        if item not in self.current_room.items:
            print(f"There is no {item} here.")
            return

        if item == "auth.log":
            #SOC Analyzer
            self.rooms["soc"].main()
            self.inventory.append("KEYPAD")
            self.tokens.append({"keypad": self.rooms["soc"].get_token()})
            print("Soc Analyzer Placeholder")

        if item == "dns.cfg":
            #DNS Analyzer
            self.rooms["dns"].main()
            self.inventory.append("DNS")
            self.tokens.append({"dns": self.rooms["dns"].get_token()})
            print("DNS Analyzer Placeholder")

        if item == "vault_dump.txt":
            #Vault Analyzer
            self.rooms["vault"].main()
            self.inventory.append("SAFE")
            self.tokens.append({"safe": self.rooms["vault"].get_token()})
            print("Vault Analyzer Placeholder")

        if item == "proc_tree.jsonl":
            #Malware Analyzer
            self.rooms["malware"].main()
            self.inventory.append("PID")
            self.tokens.append({"pid": self.rooms["malware"].get_token()})
            print("Malware Analyzer Placeholder")
        print(f"Inspecting {item}...")

    def use(self, item):
        if item in self.inventory:
            print(f"Using {item}...")
        else:
            print(f"You don't have {item} in your inventory.")

    def show_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        return "Inventory: " + ", ".join(self.inventory)
    
    def hint(self):
        print("""Hint: try looking in rooms, inspecting items, or moving to new rooms. \n
            Use "help" for a list of all commands.""") 

    def save_game(self):
        filename = input("Enter save file name: ")
        with open(filename + ".txt", 'w') as file:
            file.write(self.current_room.name + "\n")
            file.write(",".join(self.inventory))


    def load_game(self):
        filename = input("Enter save file name: ")

        try:
            with open(filename + ".txt", 'r') as file:
                room_name = file.readline().strip()
                inventory = file.readline().strip()

            if room_name in self.rooms:
                self.current_room = self.rooms[room_name]
            else:
                print("Saved room does not exist.")
                return

            if inventory:
                self.inventory = inventory.split(",")
            else:
                self.inventory = []
        except FileNotFoundError:
            print("Save file not found.")

    def quit(self):
        self.running = False

       
    def start_game(engine):
        while engine.running:
            command = input("> ")

            match command.split():
                case ["look"]:
                    print(engine.look())
                
                case ["move", room]:
                    engine.move(room)
            
                case ["inspect", item]:
                    engine.inspect(item)
                
                case ["use", item]:
                    engine.use(item)
                
                case ["inventory"]:
                    print(engine.show_inventory())
                
                case ["hint"]:
                    engine.hint()
            
                case ["save"]:
                    engine.save_game()
            
                case ["load"]:
                    engine.load_game()
            
                case ["quit"]:
                    engine.quit()

                case ["help"]:
                    engine.help()
                
                case _:
                    print("Unknown command") 