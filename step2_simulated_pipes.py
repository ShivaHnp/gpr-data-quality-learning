# Step 2: why the same pipe looks different in different soils
# A very simple simulation: each buried pipe appears as a hyperbola in a radargram.
# Two-way travel time: t(x) = 2 * sqrt((x - x0)^2 + d^2) / v
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

pipes = [(3.0, 0.6), (6.5, 1.0)]          # (position along profile in m, depth in m)
soils = {"Dry sand (v = 0.15 m/ns)": 0.15,
         "Wet clay (v = 0.07 m/ns)": 0.07}
x = np.linspace(0, 10, 400)               # profile positions (m)
t = np.linspace(0, 40, 500)               # two-way travel time (ns)

def wavelet(tt, t0, f=0.4):               # simple Ricker wavelet, centre frequency in GHz
    a = (np.pi * f * (tt - t0)) ** 2
    return (1 - 2 * a) * np.exp(-a)

fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
rng = np.random.default_rng(1)
for ax, (name, v) in zip(axes, soils.items()):
    img = np.zeros((t.size, x.size))
    for x0, d in pipes:
        tt = 2 * np.sqrt((x - x0) ** 2 + d ** 2) / v
        amp = np.exp(-d * (0.5 if v > 0.1 else 2.5))        # clay attenuates more
        for j in range(x.size):
            img[:, j] += amp * wavelet(t, tt[j])
    img += 0.05 * rng.standard_normal(img.shape)
    ax.imshow(img, cmap="gray", aspect="auto", extent=[x[0], x[-1], t[-1], t[0]], vmin=-0.6, vmax=0.6)
    ax.set_title(name)
    ax.set_xlabel("Profile position (m)")
axes[0].set_ylabel("Two-way travel time (ns)")
fig.suptitle("Same two pipes (0.6 m and 1.0 m deep), two soil conditions")
fig.tight_layout()
fig.savefig("fig4_simulated_pipes.png", dpi=150)
print("Done. Saved fig4_simulated_pipes.png")
