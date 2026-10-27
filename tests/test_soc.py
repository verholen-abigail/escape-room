import sys
sys.path.append("./")

from unittest.mock import mock_open, patch
from escaperoom.rooms.soc import SOC

def test_soc_summary():
    log_text = "\n".join([
        "2026-10-05T09:00:00Z lab1 sshd[1001]: Failed password for alice from 198.51.100.10 port 50001 protocol 2",
        "2026-10-05T09:00:01Z lab1 sshd[1002]: Failed password for bob from 198.51.100.10 port 50002 protocol 2",
        "2026-10-05T09:00:02Z lab1 sshd[1003]: Failed password for carol from 198.51.100.20 port 50003 protocol 2",
        "2026-10-05T09:00:03Z lab1 sshd[1004]: Failed password for dave from 192.0.2.7 port 50004 protocol 2",
        "2026-10-05T09:00:04Z lab1 sshd[1005]: Accepted password for alice from 198.51.100.10 port 50005 protocol 2",
        "2026-10-05T09:00:05Z lab1 sshd[1006]: Failed password for erin from 999.0.0.1 port 50006 protocol 2",
        "2026-10-05T09:00:06Z lab1 sshd: Failed password for frank from 203.0.113.8 port 50007 protocol 2",
        "2026-10-05T09:00:07Z lab1 sshd[1008]: Failed password for grace from 203.0.113.9 port 50008",
    ])

    soc = SOC("soc", [], [], "SOC test room")

    with patch("builtins.open", mock_open(read_data=log_text)):
        soc.main()

    assert soc.token == "103", f"expected token 103, got {soc.token}"
    assert soc.top24 == "198.51.100.0/24", f"unexpected subnet: {soc.top24}"
    assert soc.count == 3, f"expected 3 failures, got {soc.count}"
    assert soc.sample == ("2026-10-05T09:00:00Z lab1 sshd[1001]: Failed password for alice ""from 198.51.100.10 port 50001 protocol 2"), f"unexpected sample: {soc.sample}"
    assert soc.malformed == 3, f"expected 3 malformed lines, got {soc.malformed}"

def run_tests(*tests):
    for test in tests:
        try:
            test()
            print(f"Pass {test.__name__}")
        except AssertionError as error:
            print(f"Fail {test.__name__}: {error}")

run_tests(test_soc_summary)