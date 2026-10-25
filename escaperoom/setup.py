# create all rooms and flavour text
# import the room classes
import escaperoom.rooms.base as base
import escaperoom.rooms.dns as dns
import escaperoom.rooms.final_gate as fg
import escaperoom.rooms.malware as mal
import escaperoom.rooms.soc as soc
import escaperoom.rooms.vault as vault

from .engine import Engine

rooms = {
    "intro": base.Room(
        "intro",
        ["soc","dns","vault","malware","final"], 
        [],
        "A terminal blinks in the corner."
    ),

    "soc": soc.SOC(
        "soc", 
        ["intro"],
        ["auth.log"],
        "A cluttered screen shows failed SSH login attempts."
    ),

    "dns": dns.DNS(
        "dns",
        ["intro"],
        ["dns.cfg"],
        "The walls are covered with scribbled key=value pairs."
    ),

    "malware": mal.Malware(
        "malware",
        ["intro"],
        ["proc_tree.jsonl"],
        "A process graph flickers; exfil hides behind an innocent chain."
    ),
    
    "vault": vault.Vault(
        "vault",
        ["intro"],
        ["vault_dump.txt"],
        "A noisy dump scrolls past. Somewhere a SAFE{a-b-c} hides."
    ),

    "final_gate": fg.FinalGate(
        "final_gate",
        ["final gate"],
        ["gate"],
        "You stand before the Final Gate. The console asks for proof."
    )

}



def start(room : str, transcript):
    engine = Engine(rooms, rooms[room], transcript)
    Engine.start_game(engine)