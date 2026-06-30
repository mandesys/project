"""
==========================================================
QA Analytics Workbench
Module : qa_equilibrium.py
Version : 1.0

Equilibrium Test

Author : NG Suyasa
==========================================================
"""

import numpy as np

from modules.qa_plot import plot_control_chart


# ==========================================================
# EQUILIBRIUM TEST
# ==========================================================

def equilibrium_test(data):
    """
    Equilibrium Test

    Parameters
    ----------
    data : array-like

    Returns
    -------
    dict
    """

    data = np.asarray(data)

    mean = np.mean(data)

    std = np.std(data, ddof=1)

    ucl = mean + 3 * std

    lcl = mean - 3 * std

    # -----------------------------------------
    # Drift Decision
    # -----------------------------------------

    drift = not (lcl <= 0 <= ucl)

    # -----------------------------------------
    # Figure
    # -----------------------------------------

    fig = plot_control_chart(
        data=data,
        mean=mean,
        ucl=ucl,
        lcl=lcl,
        drift=drift
    )

    # -----------------------------------------
    # Result
    # -----------------------------------------

    result = {

        "Mean": mean,

        "Std": std,

        "UCL": ucl,

        "LCL": lcl,

        "Drift": drift,

        "figure": fig

    }

    return result