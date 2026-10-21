import base64   # lets us decode Base64 text
import codecs   # has a built-in ROT13 decoder


class DNS:

    records = dict()    # key -> value from dns.cfg

    hint_name = ""      # which hint is the real one, e.g. hint2

    hint_encoding = ""  # b64 or rot13+b64

    sentence = ""       # the decoded sentence

    token = ""          # the final word, the DNS token

    # read the file and fill the records dictionary
    def set_records(self):

        file = open("data/dns.cfg", encoding="utf-8")   # open the file

        for line in file:                # go through each line
            line = line.strip()          # remove spaces/newlines

            # skip empty lines, comments and lines without =
            if(line == "" or line.startswith("#") or "=" not in line):
                continue

            # split at the FIRST = only
            key, value = line.split("=", 1)
            self.records[key.strip()] = value.strip()

        file.close()                     

        return

    # decode one payload value which returns the text
    def decode_value(self, encoded_value):
        encoding, payload = encoded_value.split(":", 1)

        if(encoding == "b64"):
            raw_bytes = base64.b64decode(payload)

        elif(encoding == "rot13+b64"):
            # reverse order of ROT13 first, then Base64
            undone_rot13 = codecs.decode(payload, "rot13")
            raw_bytes = base64.b64decode(undone_rot13)

        else:
            raise ValueError("Unknown encoding: " + encoding)

        self.hint_encoding = encoding    # remember the last encoding used
        return raw_bytes.decode("utf-8")  # fails if not valid UTF-8

    def main(self):
        # set up the records
        self.set_records()

        # token_tag tells us which hint is real
        tag = self.decode_value(self.records["token_tag"])
        self.hint_name = "hint" + tag

        # decode only that hint
        self.sentence = self.decode_value(self.records[self.hint_name])

        # remove the final '.', take the last word
        self.token = self.sentence.rstrip(".").split()[-1]

        print("TOKEN[DNS]=" + self.token)
        print("EVIDENCE[DNS].KEY=" + self.hint_name)
        print("EVIDENCE[DNS].ENCODING=" + self.hint_encoding)
        print("EVIDENCE[DNS].DECODED_LINE=" + self.sentence)


# only run when this file is run directly, not when the game imports it
if __name__ == "__main__":
    dns = DNS()
    dns.main()