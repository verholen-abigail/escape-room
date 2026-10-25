from escaperoom.rooms.base import Room

class SOC(Room):

    # return the token
    def get_token(self):
        return self.token

    # CHANGE ONCE IMPLEMENTED TO SOC TRANSCRIPT LINES
    # return the transcript lines 
    def get_transcript(self):
        return """TOKEN[DNS]= {self.token} \n
            EVIDENCE[DNS].KEY= {self.hint_name} \n
            EVIDENCE[DNS].ENCODING= {self.hint_encoding} \n
            EVIDENCE[DNS].DECODED_LINE= {self.sentence}"""

    def main():
        return

    