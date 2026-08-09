import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({"font.family": "serif",
                     "font.serif": ["Times New Roman", "DejaVu Serif"]})

fig, ax = plt.subplots(figsize=(3.45, 2.55))
ax.set_xlim(0, 100); ax.set_ylim(0, 74)
ax.axis("off")

INK, FILL = "#1a1a1a", "#f3f3f3"
ACC, ACCF = "#33337a", "#e9e9f6"

def rbox(x, y, w, h, fc=FILL, ec=INK, lw=0.9):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0,rounding_size=1.8",
        linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2))

def txt(x, y, s, fs=7.0, c=INK, bold=False, va="center", ls=1.4):
    ax.text(x, y, s, ha="center", va=va, fontsize=fs, color=c,
            fontweight="bold" if bold else "normal", linespacing=ls, zorder=3)

def arr(x1, y1, x2, y2, ec=INK, lw=0.9):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
        mutation_scale=7, linewidth=lw, color=ec, zorder=4, shrinkA=0, shrinkB=0))

# ---- interface -------------------------------------------------
rbox(4, 57, 92, 13)
txt(50, 66.0, "Conversational interface", 7.3, bold=True)
txt(50, 60.5, "fixed 10-question protocol  ·  free-text answers", 6.1)

arr(50, 57, 50, 52)

# ---- LLM (manipulation) ----------------------------------------
rbox(4, 27, 92, 25, fc=ACCF, ec=ACC, lw=1.35)
txt(50, 48.0, "GPT-4o-mini  ·  system-prompt conditioning", 7.3, ACC, bold=True)
txt(50, 42.6, "sets elicitation framing and justification phrasing", 6.1, ACC)
for lab, xx in zip(["A  feature", "B  narrative", "C  comparative"], [6.5, 35.5, 64.5]):
    ax.add_patch(FancyBboxPatch((xx, 29.5), 29, 7,
        boxstyle="round,pad=0,rounding_size=1.3",
        linewidth=0.8, edgecolor=ACC, facecolor="white", zorder=3))
    txt(xx + 14.5, 33.0, lab, 6.0, ACC, bold=True)

arr(28, 27, 28, 20)
txt(25.5, 23.5, "preferences", 5.8, INK)
ax.texts[-1].set_ha("right"); ax.texts[-1].set_style("italic")
arr(72, 20, 72, 27)
txt(74.5, 23.5, "3 products", 5.8, INK)
ax.texts[-1].set_ha("left"); ax.texts[-1].set_style("italic")

# ---- backend ---------------------------------------------------
rbox(4, 5, 92, 15)
txt(50, 16.0, "CR-HKGE backend", 7.3, bold=True)
txt(50, 10.6, "knowledge graph embedding, 340 products\nidentical scoring in all three conditions", 6.1)

fig.tight_layout(pad=0.08)
fig.savefig("fig_architecture.png", dpi=400, bbox_inches="tight", facecolor="white")
fig.savefig("fig_architecture.pdf", bbox_inches="tight", facecolor="white")
print("ok")
