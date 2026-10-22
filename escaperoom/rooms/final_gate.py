import hmac       # for the HMAC
import hashlib    # has SHA256

import base

from .dns import DNS
from .vault import Vault
from .malware import Malware


class FinalGate(base.Room):

    gate = dict()       # key value from final_gate.txt

    tokens = dict()     # token name value

    msg = ""            # group_id

    digest = ""         # the HMAC in lowercase 

    # run every room and collect its token into self.tokens
    def gather_tokens(self):

        # DNS room
        dns_room = DNS()
        dns_room.main()
        self.tokens["DNS"] = dns_room.token

        # Vault room
        vault_room = Vault()
        vault_room.main()
        self.tokens["SAFE"] = vault_room.token

        # Malware room
        malware_room = Malware("hi", 1, 1, 1)
        malware_room.main()
        self.tokens["PID"] = malware_room.token

        # SOC room (KEYPAD) is not written yet
        # soc_room = SOC()
        # soc_room.main()
        # self.tokens["KEYPAD"] = soc_room.token

        return

    # read final_gate.txt and fill the gate dictionary
    def set_gate(self):

        file = open("data/final_gate.txt", encoding="utf-8")   # open file