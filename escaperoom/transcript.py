
class Transcript:
    def __init__ (self, file : str):
        self.file = file

    def transcribe(self, rooms: list):
        try:
            with open(self.file , 'w') as file:
                for room in rooms:
                    if(not room.token==""):
                        file.write(room.get_transcript() + "\n")
        except:
            print("Something went wrong with the transcript.")

    def save_transscript():
        pass

    
