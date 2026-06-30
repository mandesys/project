"""
===========================================================
QA Analytics Workbench
Module : qa_wn_test.py
Version: 1.0

White Noise Test (Ljung-Box)

Author : NG Suyasa
===========================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox


def white_noise_test(data, lags=10):
    """
    White Noise Test using Ljung-Box
    """

    data = np.asarray(data)
    data = data[~np.isnan(data)]

    # ======================================================
    # LJUNG-BOX TEST
    # ======================================================

    lb_test = acorr_ljungbox(data, lags=[lags], return_df=True)

    pvalue = float(lb_test["lb_pvalue"].iloc[0])
    statistic = float(lb_test["lb_stat"].iloc[0])

    is_white_noise = pvalue > 0.05

    # ======================================================
    # CONCLUSION LOGIC
    # ======================================================

    if is_white_noise:
        status = "PASS"
        conclusion = "White Noise (Random Process)"
        recommendation = (
            "Data bersifat acak. Tidak terdapat autocorrelation signifikan. "
            "Model prediksi sulit memberikan improvement."
        )
    else:
        status = "WARNING"
        conclusion = "Non White Noise (Structured Process)"
        recommendation = (
            "Terdapat pola/autocorrelation. Data memiliki struktur temporal. "
            "Cocok untuk forecasting model."
        )

    # ======================================================
    # PLOT
    # ======================================================

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(data, linewidth=1)

    ax.set_title("White Noise Test (Ljung-Box)")
    ax.grid(True)

    txt = f"LB Stat={statistic:.3f}\np={pvalue:.4f}"

    ax.text(
        0.02,
        0.95,
        txt,
        transform=ax.transAxes,
        bbox=dict(facecolor="white"),
        verticalalignment="top"
    )

    return {
        "Ljung Box Statistic": statistic,
        "p-value": pvalue,
        "White Noise": is_white_noise,
        "Status": status,
        "Conclusion": conclusion,
        "Recommendation": recommendation,
        "figure": fig
    }