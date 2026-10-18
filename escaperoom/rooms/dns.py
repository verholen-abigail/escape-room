
import base64   # lets us decode Base64 text
import codecs   # has a built-in ROT13 decoder



records = {}    # an empty dictionary: it will store  key -> value

file = open("dns.cfg", encoding="utf-8")   # open the file for reading

for line in file:                # go through the file one line at a time
    line = line.strip()          # remove spaces/newlines at both ends

    if line == "":               # skip empty lines
        continue
    if line.startswith("#"):     # skip comment lines (Task 1)
        continue
    if "=" not in line:          # skip anything that is not key=value
        continue

    # split at the FIRST "=" only (the 1 means "split once")
    key, value = line.split("=", 1)

    # strip() again because there can be spaces around key and value (Task 2)
    records[key.strip()] = value.strip()

file.close()                     # good habit: close the file when done

print("Keys found:", list(records.keys()))


def decode_value(encoded_value):
    # Task 3: split at the first ":" into encoding name and payload
    encoding, payload = encoded_value.split(":", 1)

    if encoding == "b64":
        # Base64 text -> bytes
        raw_bytes = base64.b64decode(payload)

    elif encoding == "rot13+b64":
        # Reverse order! The puzzle made it:  Base64 first, then ROT13.
        # So we undo it:  ROT13 first, then Base64.
        undone_rot13 = codecs.decode(payload, "rot13")
        raw_bytes = base64.b64decode(undone_rot13)

    else:
        raise ValueError("Unknown encoding: " + encoding)

    # Task 6: bytes -> text. This fails with an error if it is not valid UTF-8.
    text = raw_bytes.decode("utf-8")

    # return BOTH the text and the encoding name, we need both later
    return text, encoding



tag_text, tag_encoding = decode_value(records["token_tag"])
print("token_tag decodes to:", tag_text)

hint_name = "hint" + tag_text    # "hint" + "2"  ->  "hint2"
print("Authoritative hint is:", hint_name)



sentence, hint_encoding = decode_value(records[hint_name])
print("Decoded sentence:", sentence)

sentence_no_period = sentence.rstrip(".")   # remove the final period
words = sentence_no_period.split()          # split into a list of words
token = words[-1]                           # [-1] means the LAST item



print()
print("TOKEN[DNS]=" + token)
print("EVIDENCE[DNS].KEY=" + hint_name)
print("EVIDENCE[DNS].ENCODING=" + hint_encoding)
print("EVIDENCE[DNS].DECODED_LINE=" + sentence)
