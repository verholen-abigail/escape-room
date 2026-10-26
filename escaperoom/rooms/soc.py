from escaperoom.rooms.base import Room
import ipaddress 
from datetime import datetime

class SOC(Room):

    def __init__(self, name, doors, items, description):
        super().__init__(name, doors, items, description)
        self.token = ""
        self.top24 = ""
        self.count = 0
        self.sample = ""
        self.malformed = 0

    def get_token(self):
        return self.token

    def get_transcript(self):
        return (
            f"TOKEN[KEYPAD]={self.token}\n"
            f"EVIDENCE[KEYPAD].TOP24={self.top24}\n"
            f"EVIDENCE[KEYPAD].COUNT={self.count}\n"
            f"EVIDENCE[KEYPAD].SAMPLE={self.sample}\n"
            f"EVIDENCE[KEYPAD].MALFORMED_SKIPPED={self.malformed}"
        )

    def main(self):
        subnet_counts = {}
        ip_counts = {}
        samples = {}
        malformed = 0

        with open("data/auth.log", encoding="utf-8") as log:
            for line in log:
                original_line = line.rstrip("\n")
                parts = line.split()

                if len(parts) != 13:
                    malformed += 1
                    continue

                fields_are_in_place = (
                    parts[2].startswith("sshd[")
                    and parts[2].endswith("]:")
                    and parts[3] in ("Failed", "Accepted")
                    and parts[4:6] == ["password", "for"]
                    and parts[7] == "from"
                    and parts[9] == "port"
                    and parts[11:13] == ["protocol", "2"]
                )

                if not fields_are_in_place:
                    malformed += 1
                    continue

                pid_text = parts[2][5:-2]

                if "T" not in parts[0]:
                    malformed += 1
                    continue

                try:
                    datetime.fromisoformat(parts[0].replace("Z", "+00:00"))
                    int(pid_text)
                    int(parts[10])
                    address = ipaddress.IPv4Address(parts[8])
                except ValueError:
                    malformed += 1
                    continue

                if parts[3] != "Failed":
                    continue

                subnet = str(
                    ipaddress.IPv4Network(f"{address}/24", strict=False)
                )
                ip = str(address)

                subnet_counts[subnet] = subnet_counts.get(subnet, 0) + 1

                if subnet not in ip_counts:
                    ip_counts[subnet] = {}

                ip_counts[subnet][ip] = ip_counts[subnet].get(ip, 0) + 1

                if subnet not in samples:
                    samples[subnet] = original_line
        top_subnet = max(subnet_counts, key=subnet_counts.get)
        top_ip = max(ip_counts[top_subnet], key=ip_counts[top_subnet].get)

        count = subnet_counts[top_subnet]
        last_octet = top_ip.split(".")[-1]
        token = f"{last_octet}{count}"
        sample = samples[top_subnet]

        self.token = token
        self.top24 = top_subnet
        self.count = count
        self.sample = sample
        self.malformed = malformed
        
        print(self.get_transcript())
