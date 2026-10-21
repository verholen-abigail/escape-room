import re   # regular expressions


class Vault:

    # SAFE{a-b-c} with optional spaces around braces, numbers and hyphens
    pattern = re.compile(r"SAFE\s*\{\s*(\d+)\s*-\s*(\d+)\s*-\s*(\d+)\s*\}")

    found = list()      # valid candidates (a, b, c, matched text)

    token = ""          # the final token, a-b-c

    matched_text = ""   # the matched text with its original spacing

    check = ""          # the checksum, a+b=c

    # read the file and keep every candidate where a + b == c
    def set_found(self):

        file = open("data/vault_dump.txt", encoding="utf-8")   # open file

        for line in file:                         # go through each line
            match = self.pattern.search(line)     # look for the pattern

            # no candidate on this line (e.g. SAFE{3-4-})
            if(match is None):
                continue

            # turn the three groups into integers
            a = int(match.group(1))
            b = int(match.group(2))
            c = int(match.group(3))

            # the checksum test
            if(a + b == c):
                
                self.found.append((a, b, c, match.group(0)))

        file.close()                             

        return

    def main(self):
        # find the valid sequence
        self.set_found()

        # there should be exactly one
        if(len(self.found) != 1):
            print("Expected 1 valid candidate, found " + str(len(self.found)))
            return

        a, b, c, self.matched_text = self.found[0]

        self.token = str(a) + "-" + str(b) + "-" + str(c)
        self.check = str(a) + "+" + str(b) + "=" + str(c)

        print("TOKEN[SAFE]=" + self.token)
        print('EVIDENCE[SAFE].MATCH="' + self.matched_text + '"')
        print("EVIDENCE[SAFE].CHECK=" + self.check)


# only run when this file is run directly to test, not when the game imports it
if __name__ == "__main__":
    vault = Vault()
    vault.main()