# Easy tests for the DNS and Vault rooms.
# Run from the test folder:  python test_rooms_easy.py
# Every check prints PASS or FAIL, and the program keeps going.
import sys
sys.path.append('./')
from escaperoom.rooms.dns import DNS
from escaperoom.rooms.vault import Vault

passed = 0
failed = 0


#  DNS 
print("Testing DNS...")

dns = DNS("dns", ["intro"], ["dns.cfg"], "A DNS analysis terminal.")
dns.records = dict()        # start with an empty dictionary

# 1. Base64 decoding: "Mg==" is the text 2
result = dns.decode_value("b64:Mg==")
if result == "2":
    print("PASS: base64 decode")
    passed += 1
else:
    print("FAIL: base64 decode, got " + result)
    failed += 1

# 2. ROT13 then Base64 decoding of hint2 gives the real sentence
payload = "ITuyVTS1qTuipzy0LKEcqzHtnTyhqPOyozEmVTS0VUMcp3EuYt=="
result = dns.decode_value("rot13+b64:" + payload)
if result == "The authoritative hint ends at vista.":
    print("PASS: rot13+b64 decode")
    passed += 1
else:
    print("FAIL: rot13+b64 decode, got " + result)
    failed += 1

# 3. reading the file: the keys we need are found
dns.set_records()
if "token_tag" in dns.records and "hint2" in dns.records:
    print("PASS: dns.cfg was read")
    passed += 1
else:
    print("FAIL: dns.cfg was read, keys are " + str(list(dns.records.keys())))
    failed += 1

# 4. the whole room finds the right token
dns.main()                  # this prints the transcript, that is fine
if dns.token == "vista":
    print("PASS: DNS token")
    passed += 1
else:
    print("FAIL: DNS token, got " + dns.token)
    failed += 1


#  Vault 
print("")
print("Testing Vault...")

vault = Vault("vault", ["intro"], [], "A heavily secured vault.")
vault.found = list()        # start with an empty list

# 1. the pattern matches a line without spaces
if vault.pattern.search("SAFE{5-6-12}") is not None:
    print("PASS: pattern matches without spaces")
    passed += 1
else:
    print("FAIL: pattern matches without spaces")
    failed += 1

# 2. the pattern matches a line with spaces
if vault.pattern.search("SAFE { 7 - 5 - 41 }") is not None:
    print("PASS: pattern matches with spaces")
    passed += 1
else:
    print("FAIL: pattern matches with spaces")
    failed += 1

# 3. a line with a missing number does not match
if vault.pattern.search("SAFE{3-4-}") is None:
    print("PASS: bad line is skipped")
    passed += 1
else:
    print("FAIL: bad line is skipped, it matched")
    failed += 1

# 4. the numbers come out as groups 1, 2 and 3
match = vault.pattern.search("SAFE{ 7-8-15 }")
if match.group(1) == "7" and match.group(2) == "8" and match.group(3) == "15":
    print("PASS: groups are 7, 8, 15")
    passed += 1
else:
    print("FAIL: groups are 7, 8, 15")
    failed += 1

# 5. the whole room finds the one valid line, where a + b == c
vault.main()                # this prints the transcript, that is fine
if vault.token == "7-8-15":
    print("PASS: Vault token")
    passed += 1
else:
    print("FAIL: Vault token, got " + vault.token)
    failed += 1


#  result 
print("")
print("passed: " + str(passed) + "  failed: " + str(failed))