"""
============================================================
QA Analytics Workbench
Module : qa_engine.py
Version : 1.0

Main Engine

Workflow

DataFrame
    │
    ▼
Trend Plot
    │
    ▼
Equilibrium Test
    │
    ▼
Summary
============================================================
"""

from modules.qa_plot import plot_trend
from modules.qa_equilibrium import equilibrium_test
from modules.qa_summary import make_summary


# ==========================================================
# MAIN ENGINE
# ==========================================================

def run_analysis(df, column):
    """
    Run QA Analytics

    Parameters
    ----------
    df : pandas.DataFrame

    column : str

    Returns
    -------
    dict
    """

    # ---------------------------------------
    # Data
    # ---------------------------------------

    y = df[column].dropna().values

    # ---------------------------------------
    # Trend Chart
    # ---------------------------------------

    trend_fig = plot_trend(df, column)

    # ---------------------------------------
    # Equilibrium Test
    # ---------------------------------------

    eq = equilibrium_test(y)

    # ---------------------------------------
    # Summary
    # ---------------------------------------

    summary = make_summary(eq)

    # ---------------------------------------
    # Result Dictionary
    # ---------------------------------------

    result = {

        "trend_chart": trend_fig,

        "control_chart": eq["figure"],

        "Mean": eq["Mean"],

        "Std": eq["Std"],

        "UCL": eq["UCL"],

        "LCL": eq["LCL"],

        "Drift": eq["Drift"],

        "Status": summary["Status"],

        "Recommendation": summary["Recommendation"]

    }

    return result


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    import pandas as pd

    file = "sample_data/Dummy_Data.xlsx"

    df = pd.read_excel(file)

    result = run_analysis(

        df=df,

        column="Qty_Delta"

    )

    print(result)