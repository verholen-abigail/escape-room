import hmac       # for the HMAC
import hashlib    # has SHA256

from escaperoom.rooms.base import Room

class FinalGate(Room):

    gate = dict()       # key value from final_gate.txt

    tokens = dict()     # token name value

    msg = ""            # group_id

    digest = ""         # the HMAC in lowercase 

    # pull from inventory or final file
    def gather_tokens(self, inventory : dict):
        self.tokens = inventory
        return

    # read final_gate.txt and fill the gate dictionary
    def set_gate(self):

        file = open("data/final_gate.txt", encoding="utf-8")   # open file