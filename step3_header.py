# Step 3: print the file header as GPRPy reads it
import glob
import gprpy.toolbox.gprIO_DZT as dzt

found = glob.glob("**/exampledata/GSSI/FILE____032.DZT", recursive=True)
if not found:
    raise SystemExit("Example file not found. Put this script in the folder that contains the GPRPy folder.")
data, info = dzt.readdzt(found[0])
for key, value in info.items():
    print(key, ":", value)
