from escaperoom.rooms.base import Room

class SOC(Room):

    # return the token
    def get_token(self):
        return self.token

    # CHANGE ONCE IMPLEMENTED TO SOC TRANSCRIPT LINES
    # return the transcript lines 
    def get_transcript(self):
        return f"""TOKEN[DNS]= {self.token}
EVIDENCE[DNS].KEY= {self.hint_name}
EVIDENCE[DNS].ENCODING= {self.hint_encoding}
EVIDENCE[DNS].DECODED_LINE= {self.sentence}"""

    def main():
        return

    