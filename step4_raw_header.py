# Step 4: read two header fields directly from the raw .DZT file
# GPRPy's reader (step 3) does not show the antenna name and does not decode the
# creation date. Both are stored in the first bytes of the file, following the
# GSSI DZT header layout:
#   bytes 32-35: creation date and time, packed into 32 bits
#                (seconds/2: 5 bits, minutes: 6, hours: 5, day: 5, month: 4, years since 1980: 7)
#   bytes 98-111: antenna name (text)
import glob
import struct

found = glob.glob("**/exampledata/GSSI/FILE____032.DZT", recursive=True)
if not found:
    raise SystemExit("Example file not found. Put this script in the folder that contains the GPRPy folder.")

with open(found[0], "rb") as f:
    header = f.read(1024)

def decode_date(raw):
    v = struct.unpack("<I", raw)[0]
    sec = (v & 0x1F) * 2
    minute = (v >> 5) & 0x3F
    hour = (v >> 11) & 0x1F
    day = (v >> 16) & 0x1F
    month = (v >> 21) & 0x0F
    year = ((v >> 25) & 0x7F) + 1980
    return f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{sec:02d}"

print("Creation date and time:", decode_date(header[32:36]))
print("Last modified:         ", decode_date(header[36:40]))
print("Antenna name:          ", header[98:112].split(b"\x00")[0].decode("ascii"))
