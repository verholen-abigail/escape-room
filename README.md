# Escape Room

Group 03's Cyber Escape-Room for Programming Fundamentals (MCYSD-18)

# About

This is a python command-line escape room that simulates defensive security analysis. Players are tasked with investigating the supplied data packs, collecting tokens, and using those tokens to complete the Final Gate.

The rooms include:

- SOC: validate SSH authentication records and identify the subnet with the most failed logins.
- DNS: decode the authoritative hint from the configuration file.
- Vault Corridor: Find the 'SAFE{a-b-c}' candidate that passes its checksum.
- Malware Lab: Traverse the process graph to find the exfiltration process.
- Final Gate: assemble the tokens in the supplied order and calculate an HMAC-SHA256.

# Requirements
-Python 3.10 or newer

# Getting Started

From the project root, run:

python escape.py --start intro --transcript run.txt

The game utilizes a set of commands including: look, move, inspect, inventory, hint, quit, save, load, and use. 

If you are unsure what you can do in a given room, use 'help' to see what possible actions are. If you are unsure what room you are in, use 'look'. For example, if someone uses 'look' in the SOC room, they will see that connecting rooms includes the intro room and the relevant things in the room include an auth.log file. 

To move between rooms, you must input a valid room name following 'move'

Similar logic applies to other commands such as inspect.


# Data Pack

The data/ directory contains the groups evidence files:
* auth.log
* dns.cfg
* vault_dump.txt
* proc_tree.jsonl
* final_gate.txt


# End Result

An example of the completed final run.txt file can be found in the run-completed.txt file.


# Authors
Ananya Kasiraj, Abigail Verholen, and Zane Stephens
