import re

"""
________________________________________________________________
Mac Address Format:
001A2B3C4D5E      - HEX / Canonical / Plain
00:1A:2B:3C:4D:5E - Colon / Standard / IEEE
00-1A-2B-3C-4D-5E - Hyphen / Dash / Cisco
001A.2B3C.4D5E    - Dot / Period / Cisco Trunk
00 1A 2B 3C 4D 5E - Space separated
________________________________________________________________
"""



def mac_to_hex_string(mac: str) -> str:
    """
    Convert a MAC address into a 12-character hexadecimal format.
    Example: '00:1A:2B:3C:4D:5E' -> '001A2B3C4D5E'
    """
    mac = mac.replace(":", "").replace("-", "").lower()

    if not re.fullmatch(r"[0-9a-f]{12}", mac):
        raise ValueError("Invalid MAC address format")

    return mac.upper()


