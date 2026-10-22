# create all rooms and flavour text
import rooms.base as base
import rooms.dns as dns
import rooms.final_gate as fg
import rooms.malware as mal
import rooms.soc as soc
import rooms.vault as vault

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
        "A DNS analysis terminal."
    ),

    "malware": mal.Malware(
        "malware",
        ["intro"],
        ["proc_tree.jsonl"],
        "Malware creeps along the walls."
    ),
    
    "vault": vault.Vault(
        "vault",
        ["intro"],
        [],
        "A heavily secured vault.",
        locked=True,
        required_item="VAULT_KEY"
    ),

}