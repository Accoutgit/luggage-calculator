import streamlit as st
from datetime import datetime, date, time
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Cloakroom Charge Calculator",
    page_icon="🧳",
    layout="centered"
)

# ---------- HEADER ----------
st.markdown(
    "<h2 style='text-align: center;'>🧳 Cloakroom Charge Calculator</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Simple • Accurate • Official</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------- INPUT SECTION ----------
st.subheader("Deposit Details")

col1, col2 = st.columns(2)

with col1:
    deposit_date = st.date_input(
        "Deposit Date",
        value=date.today()
    )

with col2:
    deposit_time = st.time_input(
        "Deposit Time",
        value=datetime.now().time().replace(second=0, microsecond=0)
    )

st.subheader("Luggage Charge")

base_amount = st.selectbox(
    "Charge for 24 Hours (₹)",
    options=[20, 30, 40, 50, 60, 80, 100],
    index=2
)

st.divider()

# ---------- CALCULATION ----------
if st.button("Calculate Amount", use_container_width=True):

    deposit_datetime = datetime.combine(deposit_date, deposit_time)
    collection_datetime = datetime.now()

    if collection_datetime < deposit_datetime:
        st.error("❌ Collection time cannot be before deposit time.")
    else:
        total_seconds = (collection_datetime - deposit_datetime).total_seconds()
        total_hours = total_seconds / 3600

        chargeable_days = math.ceil(total_hours / 24)
        total_amount = chargeable_days * base_amount

        # ---------- OUTPUT ----------
        st.success("✅ Calculation Completed")

        st.subheader("Bill Summary")

        col3, col4 = st.columns(2)

        with col3:
            st.metric("Total Hours Used", f"{round(total_hours, 2)} hrs")

        with col4:
            st.metric("Chargeable Days", f"{chargeable_days} day(s)")

        st.markdown(
            f"""
            <div style='
                background-color:#f0f2f6;
                padding:20px;
                border-radius:10px;
                text-align:center;
                font-size:22px;
                font-weight:bold;
            '>
                Total Amount to Pay: ₹ {total_amount}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(
            f"Collection Time: {collection_datetime.strftime('%d-%m-%Y %H:%M')}"
        )

# ---------- FOOTER ----------
st.divider()
st.caption("Powered by Python • Streamlit • Free Deployment")
