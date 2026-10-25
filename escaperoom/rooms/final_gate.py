import hmac       # for the HMAC
import hashlib    # has SHA256

from escaperoom.rooms.base import Room


class FinalGate(Room):

    gate = dict()       # key value from final_gate.txt

    tokens = dict()     # token name value

    msg = ""            # group_id

    digest = ""         # the HMAC in lowercase 

    # pull from inventory or final file
        # tokens come from the engine, e.g. [{"dns": "vista"}, {"pid": 1431}]
    def set_tokens(self, inventory):
        for item in inventory:
            for name, value in item.items():
                # token_order uses capital names and the message needs text
                self.tokens[name.upper()] = str(value)
        return

    # read final_gate.txt and fill the gate dictionary
    def set_gate(self):

        file = open("data/final_gate.txt", encoding="utf-8")   # open file
        for line in file:                # go through each line
            line = line.strip()          # remove spaces/newlines

            if(line == "" or "=" not in line):
                continue

            # split at the FIRST = only
            key, value = line.split("=", 1)
            self.gate[key.strip()] = value.strip()

        file.close()   
        return
    def build_msg(self):
        order = self.gate["token_order"].split(",")   # e.g. DNS,PID,SAFE,KEYPAD

        values = list()
        for name in order:
            name = name.strip()

            # stop with a clear message if a token is missing
            if(name not in self.tokens or self.tokens[name] == ""):
                print("Missing token: " + name)
                return False

            values.append(self.tokens[name])

        self.msg = self.gate["group_id"] + "|" + "-".join(values)

        return True

    # HMAC-SHA256 with hmac_key as the key and msg as the message
    def build_hmac(self):
        key = self.gate["hmac_key"].encode("utf-8")
        message = self.msg.encode("utf-8")

        self.digest = hmac.new(key, message, hashlib.sha256).hexdigest()

        return

    # the engine calls this with its list of collected tokens
    def main(self):
        self.set_gate()

        # only continue if all four tokens were found
        if(not self.build_msg()):
            return

        self.build_hmac()

        print("FINAL_GATE=PENDING")
        print("MSG=" + self.msg)
        print("HMAC=" + self.digest)