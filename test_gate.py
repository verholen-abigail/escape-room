# run from the repo root:  python test_gate.py
# FAKE values, only for testing. Do not commit this file.
from escaperoom.rooms.final_gate import FinalGate

fake_tokens = [
    {"dns": "vista"},
    {"safe": "7-8-15"},
    {"pid": 1431},
    {"keypad": "1234"},
]

# test 1: all four tokens, should print the 3 lines
print("test 1: all four tokens")
gate = FinalGate("final_gate", ["intro"], ["gate"], "test")
gate.set_tokens(fake_tokens)
gate.main()

# test 2: keypad missing, should say Missing token: KEYPAD
print("")
print("test 2: keypad missing")
gate = FinalGate("final_gate", ["intro"], ["gate"], "test")
gate.tokens = {}                      # start clean
gate.set_tokens(fake_tokens[:3])
gate.main()

# test 3: different keypad value, the hmac should change
print("")
print("test 3: different keypad value")
gate = FinalGate("final_gate", ["intro"], ["gate"], "test")
gate.tokens = {}
gate.set_tokens(fake_tokens[:3] + [{"keypad": "9999"}])
gate.main()

# test 4: the check lines (msg order, 64 character lowercase hex)
print("")
print("test 4: checks")
gate = FinalGate("final_gate", ["intro"], ["gate"], "test")
gate.tokens = {}
gate.set_tokens(fake_tokens)
gate.main()
print("msg correct:    ", gate.msg == "group03|vista-1431-7-8-15-TEST")
print("hmac length 64: ", len(gate.digest) == 64)
print("hmac lowercase: ", gate.digest == gate.digest.lower())