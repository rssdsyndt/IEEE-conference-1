import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
})

fig, ax = plt.subplots(figsize=(3.45, 4.30))
ax.set_xlim(0, 100); ax.set_ylim(0, 132)
ax.axis("off")

INK, GREY, FILL = "#1a1a1a", "#8a8a8a", "#f3f3f3"
ACC, ACCF = "#33337a", "#e9e9f6"

def rbox(x, y, w, h, fc=FILL, ec=INK, lw=0.9):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
        boxstyle="round,pad=0,rounding_size=2.0",
        linewidth=lw, edgecolor=ec, facecolor=fc, zorder=2))

def title(x, w, y, s, fs=7.5, c=INK):
    ax.text(x + w/2, y, s, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=c, zorder=3)

def sub(x, w, y, s, fs=6.2, c=INK, ls=1.5):
    ax.text(x + w/2, y, s, ha="center", va="top",
            fontsize=fs, color=c, linespacing=ls, zorder=3)

def arr(x1, y1, x2, y2, ec=INK, lw=0.9):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
        mutation_scale=7.5, linewidth=lw, color=ec, zorder=4,
        shrinkA=0, shrinkB=0))

# ------------------------------------------------------------ setting frame
ax.add_patch(Rectangle((1.0, 1.0), 98.0, 130.0, linewidth=0.75,
    edgecolor=GREY, facecolor="none", linestyle=(0, (4, 2.6)), zorder=1))
ax.text(3.2, 128.4, "Physical perfume store  ·  on-site web application",
        fontsize=6.1, color=GREY, style="italic", va="top", zorder=3)

# ------------------------------------------------------------ participant
rbox(28, 113.5, 44, 9.5)
title(28, 44, 118.2, "Participant")

arr(50, 113.5, 50, 106.5)
ax.text(52.0, 110.0, "natural-language dialogue", fontsize=5.9,
        style="italic", color=INK, ha="left", va="center", zorder=4)

# ------------------------------------------------------------ interface
rbox(9, 88.0, 82, 18.5)
title(9, 82, 101.8, "Aromatique AI  ·  conversational interface")
sub(9, 82, 97.6, "fixed 10-question protocol, one question per message\n"
                 "free-text answers  ·  familiarity captured at Q1")

arr(50, 88.0, 50, 81.0)

# ------------------------------------------------------------ LLM (manipulation)
rbox(5, 50.0, 90, 31.0, fc=ACCF, ec=ACC, lw=1.4)
title(5, 90, 76.6, "GPT-4o-mini", c=ACC)
sub(5, 90, 72.4, "system-prompt conditioning  ·  no fine-tuning\n"
                 "sets elicitation framing and justification phrasing",
    fs=6.1, c=ACC)

for i, (lab, xx) in enumerate(zip(
        ["A  feature-based", "B  narrative-based", "C  comparative-based"],
        [7.5, 36.0, 64.5])):
    ax.add_patch(FancyBboxPatch((xx, 52.2), 28.0, 7.2,
        boxstyle="round,pad=0,rounding_size=1.4",
        linewidth=0.8, edgecolor=ACC, facecolor="white", zorder=3))
    ax.text(xx + 14.0, 55.8, lab, ha="center", va="center",
            fontsize=5.7, fontweight="bold", color=ACC, zorder=4)

ax.text(50, 63.3, "condition set once per session", ha="center", va="center",
        fontsize=5.8, style="italic", color=ACC, zorder=3)

# ------------------------------------------------------------ backend
arr(30, 50.0, 30, 39.0)
ax.text(28.0, 44.5, "preference\nrecord", fontsize=5.9, style="italic",
        color=INK, ha="right", va="center", linespacing=1.35, zorder=4)

arr(70, 39.0, 70, 50.0)
ax.text(72.0, 44.5, "3 ranked\nproducts", fontsize=5.9, style="italic",
        color=INK, ha="left", va="center", linespacing=1.35, zorder=4)

rbox(9, 21.0, 82, 18.0)
title(9, 82, 34.4, "CR-HKGE backend")
sub(9, 82, 30.4, "knowledge graph embedding over a structured\n"
                 "perfume graph  ·  identical in all three conditions")

arr(50, 21.0, 50, 14.5)

# ------------------------------------------------------------ output
rbox(9, 3.0, 82, 11.5)
title(9, 82, 11.0, "Recommendation page  →  questionnaire")
sub(9, 82, 7.6, "8 Likert items  +  binary sensory-access item", fs=6.1)

fig.tight_layout(pad=0.1)
fig.savefig("fig_architecture.png", dpi=400, bbox_inches="tight", facecolor="white")
fig.savefig("fig_architecture.pdf", bbox_inches="tight", facecolor="white")
print("ok")
