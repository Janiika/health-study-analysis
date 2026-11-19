import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(ax, data, title, xlabel, bins=20, mean_line=False):
    ax.hist(data, bins=bins, edgecolor="white")
    if mean_line:
        mean_value = data.mean()
        ax.axvline(mean_value, ls="--", color="orange", lw=2, label=f"Medel ≈ {mean_value:.1f}")
        ax.legend()
    ax.set(title=title, xlabel=xlabel, ylabel="Antal")
    ax.grid(axis="y", alpha=0.5)


def plot_barchart(ax, categories, values, title, xlabel, ylabel, ylim=None):
    bars = ax.bar(categories, values)
    ax.bar_label(bars, fmt="%.1f", padding=3)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    if ylim is not None:
        ax.set_ylim(*ylim)
    ax.grid(axis="y", alpha=0.5)


def plot_boxplot(ax, groups, tick_labels=None, title="", xlabel="", ylabel=""):
    ax.boxplot(groups, tick_labels=tick_labels, patch_artist=True)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.grid(axis="y", alpha=0.5)


def plot_scatter_with_trendline(ax, x, y, title, xlabel, ylabel):
    ax.scatter(x=x, y=y, alpha=0.6, label="Observationer")
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    k, m = np.polyfit(x, y, 1)
    ix = np.argsort(x)
    ax.plot(x[ix], (k*x + m)[ix], color="orange", label="Linjär trendlinje")
    ax.legend()
    ax.grid(alpha=0.3)


def create_health_dashboard(df):
    """
    Använder färdiga visualizationfunktioner för att skapa en dashboard 
    av fyra diagram: histogram för blodtryck, barchart för andel rökare
    per kön, boxplot för vikt per kön och scatter för ålder/kolesterol"
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    plot_histogram(
        axes[0, 0],
        data=df["systolic_bp"],
        title="Fördelning av blodtryck",
        xlabel="Systoliskt blodtryck (mmHg)",
        mean_line=True
    )

    smokers_per_sex = (
        df.groupby("sex")["smoker"]
        .apply(lambda x : (x == "Yes").mean() * 100)
        .sort_values(ascending=False)
    )
    
    plot_barchart(
        axes[0, 1],
        categories=smokers_per_sex.index,
        values=smokers_per_sex.values,
        title="Andel rökare per kön",
        xlabel="Kön",
        ylabel="Andel (%)"
    )

    axes[0, 1].set_ylim(0, 100)

    female_weight = df.loc[df["sex"] == "F", "weight"]
    male_weight = df.loc[df["sex"] == "M", "weight"]

    plot_boxplot(
        axes[1, 0],
        groups=[female_weight, male_weight],
        tick_labels=["F", "M"],
        title="Vikt per kön",
        ylabel="Vikt (kg)"
    )

    plot_scatter_with_trendline(
        axes[1, 1],
        x=df["age"],
        y=df["cholesterol"],
        title="Ålder vs. kolesterol",
        xlabel="Ålder",
        ylabel="Kolesterol (mmol/L)"
    )

    fig.suptitle("Hälsostudie - Sammanfattande dashboard", fontsize=16)

    plt.tight_layout()

    return fig