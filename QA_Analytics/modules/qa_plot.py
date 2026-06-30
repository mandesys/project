"""
==========================================================
QA Analytics Workbench
Module : qa_plot.py
Version : 1.0

Description
-----------
Plot Time Series

Author : NG Suyasa
==========================================================
"""

import matplotlib.pyplot as plt


# ==========================================================
# TREND PLOT
# ==========================================================

def plot_trend(df, column):
    """
    Plot time series.

    Parameters
    ----------
    df : pandas.DataFrame

    column : str

    Returns
    -------
    matplotlib.figure.Figure
    """

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        df.index,
        df[column],
        color="blue",
        linewidth=1.5
    )

    ax.set_title("Time Series Trend", fontsize=14)

    ax.set_xlabel("Observation")

    ax.set_ylabel(column)

    ax.grid(True)

    plt.tight_layout()

    return fig


# ==========================================================
# CONTROL CHART
# ==========================================================

def plot_control_chart(
    data,
    mean,
    ucl,
    lcl,
    drift=False
):
    """
    Plot Equilibrium Control Chart.

    Parameters
    ----------
    data : array-like

    mean : float

    ucl : float

    lcl : float

    drift : bool

    Returns
    -------
    matplotlib.figure.Figure
    """

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        data,
        color="royalblue",
        linewidth=1.2,
        marker="o",
        markersize=3
    )

    # Mean
    ax.axhline(
        mean,
        color="green",
        linestyle="-",
        linewidth=2,
        label=f"Mean = {mean:.3f}"
    )

    # UCL
    ax.axhline(
        ucl,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"UCL = {ucl:.3f}"
    )

    # LCL
    ax.axhline(
        lcl,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"LCL = {lcl:.3f}"
    )

    # Zero Line
    ax.axhline(
        0,
        color="black",
        linewidth=1
    )

    if drift:

        title = "Equilibrium Test (DRIFT)"

    else:

        title = "Equilibrium Test (NO DRIFT)"

    ax.set_title(title, fontsize=14)

    ax.set_xlabel("Observation")

    ax.set_ylabel("Delta")

    ax.legend()

    ax.grid(True)

    plt.tight_layout()

    return fig


# ==========================================================
# HISTOGRAM
# ==========================================================

def plot_histogram(data):
    """
    Plot Histogram.

    Parameters
    ----------
    data : array-like

    Returns
    -------
    matplotlib.figure.Figure
    """

    fig, ax = plt.subplots(figsize=(8,5))

    ax.hist(
        data,
        bins=20,
        edgecolor="black"
    )

    ax.set_title("Histogram")

    ax.set_xlabel("Value")

    ax.set_ylabel("Frequency")

    ax.grid(True)

    plt.tight_layout()

    return fig


# ==========================================================
# SAVE FIGURE
# ==========================================================

def save_figure(fig, filename):
    """
    Save matplotlib figure.

    Parameters
    ----------
    fig : matplotlib.figure

    filename : str
    """

    fig.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )