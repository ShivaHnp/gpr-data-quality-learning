# Step 1: process a real GPR profile with GPRPy
# Example data: GSSI file that comes with GPRPy (gprpy/exampledata/GSSI/FILE____032.DZT)
import matplotlib
matplotlib.use("Agg")
import gprpy.gprpy as gp

import glob
found = glob.glob("**/exampledata/GSSI/FILE____032.DZT", recursive=True)
if not found:
    raise SystemExit("Example file not found. Put this script in the folder that contains the GPRPy folder.")
DATA = found[0]
print("Using:", DATA)

gpr = gp.gprpyProfile(DATA)
print("Number of samples x traces:", gpr.data.shape)
print("Profile length (m):", gpr.profilePos[-1])
print("Time window (ns):", gpr.twtt[-1])

gpr.printProfile("fig1_raw.pdf", dpi=150)          # 1. raw data

gpr.dewow(window=10)                                 # 2. remove low-frequency 'wow'
gpr.remMeanTrace(ntraces=100)                        # 3. background removal (removes flat bands)
gpr.tpowGain(power=1.5)                              # 4. gain: make deeper (weaker) signals visible
gpr.printProfile("fig2_processed.pdf", dpi=150)

gpr.setVelocity(0.1)                                 # 5. assumed velocity 0.1 m/ns -> depth axis
gpr.printProfile("fig3_depth.pdf", dpi=150)

gpr.writeHistory("processing_history.py")          # every step and parameter, saved as a script
print("Done. Processing history saved to processing_history.py")
