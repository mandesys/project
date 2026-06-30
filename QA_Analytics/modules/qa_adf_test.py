"""
==========================================================
QA Analytics Workbench
Module : qa_adf_test.py
Version : 1.0

ADF Stationarity Test

Author : NG Suyasa
==========================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller


def adf_test(data):

    data = np.asarray(data)
    data = data[~np.isnan(data)]

    result = adfuller(data, regression="ct")

    adf_stat = result[0]
    pvalue = result[1]
    lags = result[2]
    nobs = result[3]
    crit = result[4]

    stationary = (pvalue < 0.05) and (adf_stat < crit["5%"])

    if stationary:
        status = "PASS"
        conclusion = "Evidence of Stationary Process"
        recommendation = "Process variability stable; suitable for forecasting models."
    else:
        status = "WARNING"
        conclusion = "Non-Stationary Process"
        recommendation = "Consider differencing, detrending, or process stabilization."

    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(data)
    ax.set_title("ADF Stationarity Test")

    txt = f"ADF={adf_stat:.3f}\np={pvalue:.4f}\nStationary={stationary}"

    ax.text(
        0.02, 0.95, txt,
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=dict(facecolor="white")
    )

    ax.grid(True)

    return {
        "ADF Statistic": adf_stat,
        "p-value": pvalue,
        "Lag": lags,
        "Observation": nobs,
        "Critical Value": crit,
        "Stationary": stationary,
        "Status": status,
        "Conclusion": conclusion,
        "Recommendation": recommendation,
        "figure": fig
    }