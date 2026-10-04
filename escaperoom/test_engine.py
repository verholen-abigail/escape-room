from .engine import TestEngine
from .rooms import Room

rooms = {
    "intro": Room(
        "intro", 
        "A terminal blinks in the corner.",
        ["soc","dns","vault","malware","final"], 
        []
        ),
    "soc": Room(
        "soc", 
        "A cluttered screen shows failed SSH login attempts.",
        ["intro"],
        ["auth.log"]
        ),
    "dns": Room(
        "dns",
        "A DNS analysis terminal.",
        ["intro"],
        ["dns.cfg"]
        ),
    "vault": Room(
        "vault",
        "A heavily secured vault.",
        ["intro"],
        [],
        locked=True,
        required_item="VAULT_KEY"
        ),
}

engine = TestEngine(rooms, rooms["intro"])
engine.inventory.append("key")
engine.inventory.append("usb")

TestEngine.start_game(engine)