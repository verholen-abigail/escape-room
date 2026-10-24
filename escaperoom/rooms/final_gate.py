import hmac       # for the HMAC
import hashlib    # has SHA256




class FinalGate(base.Room):

    gate = dict()       # key value from final_gate.txt

    tokens = dict()     # token name value

    msg = ""            # group_id

    digest = ""         # the HMAC in lowercase 

    # run every room and collect its token into self.tokens 
    def gather_tokens(self):
    #dummy values to test the HMAC
    # self.tokens["DNS"] = "VISTA"
    # self.tokens["SAFE"] = "7-8-15"
    #self.tokens["Malware"] = "malware-token"
    #self.tokens["SOC"] = "soc-token"
    return

    # read final_gate.txt and fill the gate dictionary
    def set_gate(self):

        file = open("data/final_gate.txt", encoding="utf-8")   # open file