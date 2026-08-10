import matplotlib
matplotlib.use("Agg")
# Embed TrueType (Type 42) instead of matplotlib's default Type 3 bitmap fonts.
# IEEE Xplore and EDAS reject Type 3.
matplotlib.rcParams["pdf.fonttype"] = 42
matplotlib.rcParams["ps.fonttype"] = 42
import matplotlib.pyplot as plt
from math import sqrt

plt.rcParams.update({"font.family": "serif",
                     "font.serif": ["Times New Roman", "DejaVu Serif"]})

N, TCRIT = 30, 2.045          # t(29), 95%
INK, GREY = "#1a1a1a", "#9a9a9a"

# JASP descriptives: mean, SD  (n = 30 per cell)
data = {
    "Perceived trust":    {"A": (4.483, 0.4639), "B": (4.050, 0.6345), "C": (4.650, 0.3511)},
    "Purchase intention": {"A": (3.783, 0.7733), "B": (3.550, 0.8444), "C": (4.233, 0.5208)},
}
# Dunn post hoc, Holm-corrected
sig = {
    "Perceived trust":    [("A", "B", "*"), ("B", "C", "***")],
    "Purchase intention": [("A", "C", "*"), ("B", "C", "**")],
}
ylim = {"Perceived trust": (3.4, 5.45), "Purchase intention": (3.0, 5.05)}

fig, axes = plt.subplots(1, 2, figsize=(3.45, 2.25))
xs = {"A": 0, "B": 1, "C": 2}

for ax, (title, d) in zip(axes, data.items()):
    for k, (m, sd) in d.items():
        ci = TCRIT * sd / sqrt(N)
        ax.errorbar(xs[k], m, yerr=ci, fmt="o", ms=3.6, color=INK,
                    ecolor=INK, elinewidth=0.85, capsize=2.6, capthick=0.85, zorder=3)
    lo, hi = ylim[title]
    ax.set_xlim(-0.55, 2.55); ax.set_ylim(lo, hi)
    ax.set_xticks([0, 1, 2]); ax.set_xticklabels(["A", "B", "C"], fontsize=7)
    ax.tick_params(axis="y", labelsize=6.2, length=2.2, pad=1.5)
    ax.tick_params(axis="x", length=0, pad=2.5)
    ax.set_title(title, fontsize=7.2, pad=4.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_linewidth(0.7); ax.spines[s].set_color(GREY)
    ax.grid(axis="y", linewidth=0.4, color="#e4e4e4", zorder=0)
    ax.set_axisbelow(True)

    # significance brackets, stacked above the data
    top = max(m + TCRIT * sd / sqrt(N) for m, sd in d.values())
    step = (hi - lo) * 0.115
    y = top + step * 0.55
    for a, b, star in sig[title]:
        x1, x2 = xs[a], xs[b]
        h = step * 0.17
        ax.plot([x1, x1, x2, x2], [y, y + h, y + h, y], lw=0.75, color=INK, zorder=4)
        ax.text((x1 + x2) / 2, y + h * 1.05, star, ha="center", va="bottom",
                fontsize=7.4, color=INK, zorder=4)
        y += step

axes[0].set_ylabel("Mean rating", fontsize=6.8, labelpad=2)
fig.tight_layout(pad=0.25, w_pad=1.1)
fig.savefig("fig_means.png", dpi=400, bbox_inches="tight", facecolor="white")
fig.savefig("fig_means.pdf", bbox_inches="tight", facecolor="white")

for title, d in data.items():
    for k, (m, sd) in d.items():
        ci = TCRIT * sd / sqrt(N)
        print(f"{title:19s} {k}  M={m:.3f}  95% CI [{m-ci:.3f}, {m+ci:.3f}]")
