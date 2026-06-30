"""
==========================================================
QA Analytics Workbench
Module : qa_summary.py
Version : 1.0

Summary Generator

Author : NG Suyasa
==========================================================
"""


# ==========================================================
# SUMMARY
# ==========================================================

def make_summary(eq_result):
    """
    Generate summary.

    Parameters
    ----------
    eq_result : dict

    Returns
    -------
    dict
    """

    drift = eq_result["Drift"]

    mean = eq_result["Mean"]

    std = eq_result["Std"]

    ucl = eq_result["UCL"]

    lcl = eq_result["LCL"]

    # --------------------------------------
    # Status
    # --------------------------------------

    if drift:

        status = "WARNING"

        recommendation = (
            "Control limit tidak mengapit nilai nol. "
            "Terindikasi terjadi drift atau bias sistematis. "
            "Periksa flow meter, kalibrasi, perubahan proses, "
            "atau perubahan operating condition."
        )

    else:

        status = "PASS"

        recommendation = (
            "Control limit masih mengapit nilai nol. "
            "Data masih berada pada kondisi equilibrium "
            "dan tidak terdapat indikasi drift."
        )

    return {

        "Status": status,

        "Recommendation": recommendation,

        "Mean": mean,

        "Std": std,

        "UCL": ucl,

        "LCL": lcl

    }


# ==========================================================
# PRINT SUMMARY
# ==========================================================

def print_summary(summary):
    """
    Print Summary
    """

    print()

    print("=" * 60)

    print("QA ANALYTICS SUMMARY")

    print("=" * 60)

    print(f"Status : {summary['Status']}")

    print()

    print(f"Mean : {summary['Mean']:.4f}")

    print(f"Std  : {summary['Std']:.4f}")

    print(f"UCL  : {summary['UCL']:.4f}")

    print(f"LCL  : {summary['LCL']:.4f}")

    print()

    print("Recommendation")

    print("-" * 60)

    print(summary["Recommendation"])

    print("=" * 60)