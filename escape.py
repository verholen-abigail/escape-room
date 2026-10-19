'''class TestEngine:
    #def look(self):
        print("LOOK worked!")

    #def move(self, room):
        print("MOVE worked! Room:", room)

    #def inspect(self, item):
        print("INSPECT worked! Item:", item)

    #def use(self, item):
        print("USE worked! Item:", item)

    #def inventory(self):
        print("INVENTORY worked!")

    #def hint(self):
        print("HINT worked!")

    #def save(self):
        print("SAVE worked!")

    #def load(self):
        print("LOAD worked!")'''

def start_game(engine):
    while True:
        command = input("> ")

        match command.split():
            case ["look"]:
                engine.look()
                
            case ["move", room]:
                engine.move(room)
            
            case ["inspect", item]:
                engine.inspect(item)
                
            case ["use", item]:
                engine.use(item)
                
            case ["inventory"]:
                engine.inventory()
                
            case ["hint"]:
                engine.hint()
            
            case ["save"]:
                engine.save()
            
            case ["load"]:
                engine.load()
            
            case ["quit"]:
                break
            case _:
                print("Unknown command") 

#engine = TestEngine()
#start_game(engine)