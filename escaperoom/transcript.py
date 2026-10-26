
class Transcript:
    def __init__ (self, file : str):
        self.file = file

    def transcribe(self, rooms: list):
        try:
            # opens the file or creates it
            with open(self.file , 'w+') as file:
                # clears file incase it exists
                file.truncate()
                for room in rooms:
                    if(not rooms[room].get_token()==""):
                        file.write(rooms[room].get_transcript() + "\n")
        except:
            print("Something went wrong with the transcript.")

