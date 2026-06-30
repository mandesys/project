"""
===========================================================
QA Analytics Workbench
Version : 1.1
File    : app.py
Author  : NG Suyasa
===========================================================
"""

import streamlit as st

from qa_engine import run_analysis
from modules.qa_adf_test import adf_test
from modules.qa_wn_test import white_noise_test

from modules.qa_reader import (
    read_excel,
    get_numeric_columns
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="QA Analytics Workbench",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# HEADER
# ==========================================================

st.title("📈 QA Analytics Workbench")
st.caption("Quantity Assurance Analytics Toolkit")
st.divider()

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("QA Analytics")
st.sidebar.write("Version 1.1")
st.sidebar.divider()

st.sidebar.success("✔ Equilibrium Test")
st.sidebar.success("✔ ADF Stationarity Test")
st.sidebar.success("✔ White Noise Test")

st.sidebar.info("Next Version Roadmap:")
st.sidebar.write("- White Noise Test")
st.sidebar.write("- Regression QA Model")
st.sidebar.write("- KPSS Stationarity Test")

# ==========================================================
# FILE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

if uploaded_file is None:
    st.info("Silakan upload file Excel (*.xlsx)")
    st.stop()

# ==========================================================
# READ DATA
# ==========================================================

try:
    df = read_excel(uploaded_file)
    numeric_cols = get_numeric_columns(df)

except Exception as e:
    st.error(f"Gagal membaca file Excel.\n\n{e}")
    st.stop()

# ==========================================================
# VALIDATION
# ==========================================================

if len(numeric_cols) == 0:
    st.error("Tidak ditemukan kolom numerik untuk analisis.")
    st.stop()

# ==========================================================
# PREVIEW DATA
# ==========================================================

st.subheader("Dataset Preview")
st.dataframe(df, use_container_width=True)

st.write(f"Jumlah Data   : {len(df)}")
st.write(f"Jumlah Kolom  : {len(df.columns)}")
st.divider()

# ==========================================================
# VARIABLE SELECTION
# ==========================================================

selected_column = st.selectbox(
    "Pilih Variabel yang Akan Dianalisis",
    numeric_cols
)

st.divider()

# ==========================================================
# RUN ANALYSIS
# ==========================================================

if st.button(
    "▶ RUN QA ANALYSIS",
    use_container_width=True,
    type="primary"
):

    with st.spinner("Running QA Analytics ..."):

        try:
            result = run_analysis(df, selected_column)

        except Exception as e:
            st.error(f"Error in QA Engine: {e}")
            st.stop()

    # ======================================================
    # TREND ANALYSIS
    # ======================================================

    st.subheader("Trend Analysis")
    st.pyplot(result["trend_chart"])

    # ======================================================
    # EQUILIBRIUM TEST
    # ======================================================

    st.subheader("Equilibrium Control Chart")
    st.pyplot(result["control_chart"])

    # ======================================================
    # ADF STATIONARITY TEST (NEW FEATURE)
    # ======================================================

    st.subheader("ADF Stationarity Test")

    try:
        series = df[selected_column].dropna().values
        adf_result = adf_test(series)

        st.pyplot(adf_result["figure"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "ADF Statistic",
                f"{adf_result['ADF Statistic']:.4f}"
            )

            st.metric(
                "p-value",
                f"{adf_result['p-value']:.6f}"
            )

        with col2:
            st.metric(
                "Lag",
                adf_result["Lag"]
            )

            st.metric(
                "Stationary",
                str(adf_result["Stationary"])
            )

        if adf_result["Status"] == "PASS":
            st.success("✔ ADF RESULT: STATIONARY PROCESS")
        else:
            st.warning("⚠ ADF RESULT: NON-STATIONARY PROCESS")

        st.info(adf_result["Recommendation"])

    except Exception as e:
        st.error(f"ADF Test Error: {e}")

    st.divider()

    # ======================================================
    # WHITE NOISE TEST
    # ======================================================

    st.subheader("White Noise Test (Ljung-Box)")

    try:
        series = df[selected_column].dropna().values
        wn_result = white_noise_test(series, lags=10)

        st.pyplot(wn_result["figure"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Ljung-Box Statistic",
                f"{wn_result['Ljung Box Statistic']:.4f}"
            )

            st.metric(
                "p-value",
                f"{wn_result['p-value']:.6f}"
            )

        with col2:
            st.metric(
                "White Noise",
                str(wn_result["White Noise"])
            )

            st.metric(
                "Status",
                wn_result["Status"]
            )

        if wn_result["Status"] == "PASS":
            st.success("✔ WHITE NOISE: RANDOM PROCESS")
        else:
            st.warning("⚠ STRUCTURED PROCESS DETECTED")

        st.info(wn_result["Recommendation"])

    except Exception as e:
        st.error(f"White Noise Test Error: {e}")

    st.divider()     	

    # ======================================================
    # SUMMARY STATISTICS
    # ======================================================

    st.subheader("Summary Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Mean", f"{result['Mean']:.4f}")
        st.metric("Standard Deviation", f"{result['Std']:.4f}")

    with col2:
        st.metric("Upper Control Limit", f"{result['UCL']:.4f}")
        st.metric("Lower Control Limit", f"{result['LCL']:.4f}")

    st.divider()

    # ======================================================
    # DRIFT & HEALTH STATUS
    # ======================================================

    if result["Drift"]:
        st.error("⚠ DRIFT DETECTED")
    else:
        st.success("✔ NO DRIFT DETECTED")

    if result["Status"] == "PASS":
        st.success("QA HEALTH STATUS : PASS")
    else:
        st.warning("QA HEALTH STATUS : WARNING")

    st.divider()

    # ======================================================
    # RECOMMENDATION
    # ======================================================

    st.subheader("Recommendation")
    st.info(result["Recommendation"])