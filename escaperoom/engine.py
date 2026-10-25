import ast

class Engine:
    def __init__(self, rooms, intro, transcript):
        # game state info
        self.rooms = rooms
        self.current_room = intro
        self.inventory = []
        self.tokens = []

        self.running = True
        self.transcript = transcript
        

    # list of commands avalible to the user
    def help(self):
        print("""look \nmove <room> \ninspect <item in room> \nuse <door or gate>
inventory \nhint \nsave \nload \nquit""")
        return

    # relays the description of the current room
    def look(self):
        return self.current_room.look()

    # moves to a new room if the doorway exists
    def move(self, room):
            if room not in self.rooms :
                print(f"{room} does not exist.")
                return
            
            if room not in self.current_room.doors:
                print(f"You cannot go to {room} from here.")
                return
            
            destination = self.rooms[room]
            
            self.current_room = destination
            print(self.current_room.arrival())

    # inspects the item in that room and adds the found inventory and tokens
    def inspect(self, item):
        if item not in self.current_room.items:
            print(f"There is no {item} here.")
            return

        print(f"Inspecting {item}...")

        match item :

            case "auth.log":
                #SOC Analyzer
                self.rooms["soc"].main()
                self.inventory.append("KEYPAD")
                self.tokens.append({"keypad": self.rooms["soc"].get_token()})
                
            case "dns.cfg":
                #DNS Analyzer
                self.rooms["dns"].main()
                self.inventory.append("DNS")
                self.tokens.append({"dns": self.rooms["dns"].get_token()})

            case "vault_dump.txt":
                #Vault Analyzer
                self.rooms["vault"].main()
                self.inventory.append("SAFE")
                self.tokens.append({"safe": self.rooms["vault"].get_token()})
            
            case "proc_tree.jsonl":
                #Malware Analyzer
                self.rooms["malware"].main()
                self.inventory.append("PID")
                self.tokens.append({"pid": self.rooms["malware"].get_token()})
           
            case "gate":
                #Final Gate
                print("This gate may be able to be <used>")

            case _:
                print("Unknown item/room paring") 
        
    # using the final gate
    def use(self, item):
        if item == "gate" and self.current_room == self.rooms["final_gate"]:
            self.rooms["final_gate"].set_tokens(self.tokens)
            self.rooms["final_gate"].main()
        else:
            print(f"You can't seem to use {item}.")

    # shows current inventory
    def show_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        return "Inventory: " + ", ".join(self.inventory)

    # prints a hint for the user
    def hint(self):
        print("""Hint: try looking in rooms, inspecting items, or moving to new rooms.
            Use "help" for a list of all commands.""") 

    # saves game with critical information
    def save_game(self):
        filename = input("Enter save file name: ")
        with open(filename + ".txt", 'w') as file:
            file.write(self.current_room.name + "\n")
            file.write(",".join(self.inventory)+ "\n")

            # change dicts to str
            str_tokens = []
            for token in self.tokens:
                str_tokens.append(str(token))
            file.write("$".join(str_tokens))

        print(f"[Game] Your game has been saved.")

    # loads game 
    def load_game(self):
        filename = input("Enter save file name: ")

        try:
            with open(filename + ".txt", 'r') as file:
                room_name = file.readline().strip()
                inventory = file.readline().strip()
                all_tokens = file.readline().strip()

            if room_name in self.rooms:
                self.current_room = self.rooms[room_name]
            else:
                print("Saved room does not exist.")
                return

            if inventory:
                self.inventory = inventory.split(",")
            else:
                self.inventory = []

            if all_tokens:
                # split the tokens into the format 
                tokens = all_tokens.split("$")
                for token in tokens:
                    try:
                        self.tokens.append(ast.literal_eval(token))
                    except:
                        print("Error with token parsing")

            print(f"[Game] Your game has been loaded. You are now in {room_name}.")

        except FileNotFoundError:
            print("Save file not found.")

    # write transcript and ends session
    def quit(self):
        self.transcript.transcribe(self.rooms)
        print("[Game] Thank you for playing.")
        self.running = False


    # starts engine and is the main loop 
    def start_game(engine):
        print("[Game] Cyber Escape Room started. Type 'help' for commands.")

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