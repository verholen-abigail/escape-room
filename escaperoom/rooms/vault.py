
import re

#build regex pattern
# \s*   = zero or more spaces (this makes spaces "optional")
# (\d+) = one or more digits, saved as a group so we can read it later
# \{ \} = braces must be escaped with a backslash, because { } are special in regex
pattern = re.compile(
    r"SAFE\s*\{\s*(\d+)\s*-\s*(\d+)\s*-\s*(\d+)\s*\}"
)
# re.compile() builds the pattern once so we can reuse it on every line.

# Read the lines
file = open("vault_dump.txt", encoding="utf-8")

found = []   # an empty list to keep all VALID candidates

for line in file:
    match = pattern.search(line)    # look for the pattern anywhere in the line

    if match is None:               # no candidate on this line (e.g. "SAFE{3-4-}")
        continue                    # skip to the next line

    # get the numbers out of the groups and make them integers
    a = int(match.group(1))         # first  (\d+)
    b = int(match.group(2))         # second (\d+)
    c = int(match.group(3))         # third  (\d+)

    # the checksum test (Task 3)
    if a + b == c:
        matched_text = match.group(0)   # group(0) = the WHOLE matched text, spaces included
        found.append((a, b, c, matched_text))

file.close()

print("Valid candidates found:", len(found))

#  there should be exactly one (Task 4)
a, b, c, matched_text = found[0]

print()
print("TOKEN[SAFE]=" + str(a) + "-" + str(b) + "-" + str(c))
print('EVIDENCE[SAFE].MATCH="' + matched_text + '"')
print("EVIDENCE[SAFE].CHECK=" + str(a) + "+" + str(b) + "=" + str(c))