"""Regenerates the 7 result figures in ../figures/ from the paper's logged numbers.
Run from the code/ directory: python make_figures.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.size": 10, "font.family": "serif",
                      "axes.edgecolor": "#333333", "axes.linewidth": 0.8})
IEEE_BLUE, IEEE_ORANGE, IEEE_GREY = "#1f3f66", "#c9622a", "#8a8a8a"
IEEE_GREEN, IEEE_RED = "#3a7d44", "#a4333f"
PALETTE = [IEEE_BLUE, IEEE_ORANGE, IEEE_GREY, IEEE_GREEN, IEEE_RED]
OUT = "../figures/"

strategies = ["Random", "Class-\nbalanced", "Uncer-\ntainty", "Diversity", "Adaptive\n(proposed)"]
fidelity_1000 = [0.3764, 0.3651, 0.2751, 0.2760, 0.3236]
fig, ax = plt.subplots(figsize=(4.6, 2.8))
bars = ax.bar(strategies, fidelity_1000, color=PALETTE, width=0.62, edgecolor="black", linewidth=0.6)
for b, v in zip(bars, fidelity_1000):
    ax.text(b.get_x()+b.get_width()/2, v+0.008, f"{v:.3f}", ha="center", va="bottom", fontsize=8)
ax.set_ylabel("Fidelity (agreement w/ victim)"); ax.set_ylim(0, 0.45)
ax.set_title("Query-selection strategy comparison\n(CNN victim, 1000-query budget)", fontsize=9)
ax.tick_params(axis="x", labelsize=7.6)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_strategy_comparison.pdf"); plt.close()

labels = ["Random", "Adaptive\n(proposed)"]; means = [0.3653, 0.3286]
err = [[0.0187, 0.0204], [0.0187, 0.0204]]
fig, ax = plt.subplots(figsize=(3.2, 2.6))
ax.bar(labels, means, yerr=err, capsize=5, color=[IEEE_BLUE, IEEE_ORANGE], width=0.5,
       edgecolor="black", linewidth=0.6, error_kw={"elinewidth": 1.1})
ax.set_ylabel("Fidelity (mean, n=5 seeds)"); ax.set_ylim(0, 0.45)
ax.set_title("Multi-seed comparison with 95% CI\n(paired $t$=-3.35, $p$=0.029, Cohen's $d$=-1.50)", fontsize=8.3)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_multiseed_ci.pdf"); plt.close()

budgets = [100, 500, 1000, 5000, 10000]
random_sweep = [0.2237, 0.2505, 0.3552, 0.4558, 0.4638]
adaptive_sweep = [0.1300, 0.2179, 0.3612, 0.4503, 0.4863]
fig, ax = plt.subplots(figsize=(3.6, 2.7))
ax.plot(budgets, random_sweep, marker="o", color=IEEE_BLUE, label="Random", linewidth=1.6)
ax.plot(budgets, adaptive_sweep, marker="s", color=IEEE_ORANGE, label="Adaptive (proposed)", linewidth=1.6)
ax.set_xscale("log"); ax.set_xlabel("Query budget (log scale)"); ax.set_ylabel("Fidelity")
ax.set_title("Fidelity vs. query budget (CNN victim)", fontsize=9)
ax.legend(fontsize=7.5, loc="lower right"); ax.grid(alpha=0.3, linestyle=":")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_budget_sweep.pdf"); plt.close()

families = ["CNN\n(ResNet-18)", "ViT\n(ViT-B/16-scale)", "CLIP\n(ViT-B/32 + linear)"]
fam_fid = [0.3236, 0.1464, 0.4861]
fig, ax = plt.subplots(figsize=(4.4, 2.8))
bars = ax.bar(families, fam_fid, color=[IEEE_BLUE, IEEE_GREEN, IEEE_RED], width=0.55, edgecolor="black", linewidth=0.6)
for b, v in zip(bars, fam_fid):
    ax.text(b.get_x()+b.get_width()/2, v+0.01, f"{v:.3f}", ha="center", va="bottom", fontsize=8)
ax.set_ylabel("Fidelity (adaptive strategy, 1000 q)"); ax.set_ylim(0, 0.6)
ax.set_title("Victim-family vulnerability (RQ1/H1)", fontsize=9)
ax.tick_params(axis="x", labelsize=7.6)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_victim_family.pdf"); plt.close()

abl_labels = ["Full\n(U+D+I)", "No U\n(D+I only)", "No D\n(U+I only)", "No I\n(U+D only)"]
abl_vals = [0.3236, 0.2892, 0.3491, 0.2851]
fig, ax = plt.subplots(figsize=(4.2, 2.8))
bars = ax.bar(abl_labels, abl_vals, color=[IEEE_BLUE, IEEE_GREY, IEEE_GREY, IEEE_GREY],
              width=0.55, edgecolor="black", linewidth=0.6)
for b, v in zip(bars, abl_vals):
    ax.text(b.get_x()+b.get_width()/2, v+0.008, f"{v:.3f}", ha="center", va="bottom", fontsize=8)
ax.set_ylabel("Fidelity"); ax.set_ylim(0, 0.42)
ax.set_title("Component ablation of $S(x)=\\alpha U+\\beta D+\\gamma I$", fontsize=9)
ax.tick_params(axis="x", labelsize=7.6)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_ablation.pdf"); plt.close()

settings = ["Lenient", "Moderate\n(default)", "Strict"]
naive = [0.2273, 0.1039, 0.2397]; rate_mim = [0.1300, 0.0830, 0.0291]; stealth_opt = [0.0506, 0.0644, 0.0602]
x = np.arange(3); width = 0.25
fig, ax = plt.subplots(figsize=(3.6, 2.7))
ax.bar(x-width, naive, width, label="Naive", color=IEEE_BLUE, edgecolor="black", linewidth=0.5)
ax.bar(x, rate_mim, width, label="Rate-mimicking", color=IEEE_ORANGE, edgecolor="black", linewidth=0.5)
ax.bar(x+width, stealth_opt, width, label="Stealth-optimized", color=IEEE_RED, edgecolor="black", linewidth=0.5)
ax.set_xticks(x); ax.set_xticklabels(settings); ax.set_ylabel("Fidelity under defense")
ax.set_title("Security--utility trade-off across defense\nstrength and attacker stealth level", fontsize=9)
ax.legend(fontsize=7, loc="upper right")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_tradeoff_curve.pdf"); plt.close()

levels = ["Naive", "Rate-\nmimicking", "Stealth-\noptimized"]
v2, v3 = [1.00, 0.00, 0.00], [1.00, 0.00, 0.56]
x = np.arange(3); width = 0.32
fig, ax = plt.subplots(figsize=(3.4, 2.6))
ax.bar(x-width/2, v2, width, label="Detector v2 (4 features)", color=IEEE_GREY, edgecolor="black", linewidth=0.5)
ax.bar(x+width/2, v3, width, label="Detector v3 (6 features)", color=IEEE_GREEN, edgecolor="black", linewidth=0.5)
ax.set_xticks(x); ax.set_xticklabels(levels); ax.set_ylabel("Recall"); ax.set_ylim(0, 1.15)
ax.set_title("Extraction-risk detector recall by\nattacker stealth level", fontsize=9)
ax.legend(fontsize=7, loc="upper right")
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
plt.tight_layout(); plt.savefig(OUT+"fig_detector_recall.pdf"); plt.close()

print("All 7 figures regenerated in", OUT)
