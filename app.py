import streamlit as st
import pandas as pd
import time

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor


st.set_page_config(
    page_title="Meridian | Automated Valuation",
    page_icon="📐",
    layout="centered",
    initial_sidebar_state="collapsed"
)


@st.cache_resource
def load_model():

    housing = fetch_california_housing()

    X = pd.DataFrame(
        housing.data,
        columns=housing.feature_names
    )

    y = housing.target

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model


model = load_model()


st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500&display=swap');

:root {
    --ink: #0B1E33;
    --ink-2: #10233c;
    --grid: rgba(95, 179, 212, 0.14);
    --cyan: #5FB3D4;
    --brass: #C9A468;
    --parchment: #EDEDE3;
    --muted: #7E93A8;
}

.stApp {
    background-color: var(--ink);
    background-image:
        linear-gradient(var(--grid) 1px, transparent 1px),
        linear-gradient(90deg, var(--grid) 1px, transparent 1px);
    background-size: 28px 28px;
}

.block-container {
    max-width: 760px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

* {
    font-family: 'Inter', sans-serif;
}

/* ---------- Hero ---------- */

.hero {
    text-align: center;
    margin-bottom: 2.2rem;
    padding-bottom: 1.6rem;
    border-bottom: 1px solid rgba(201, 164, 104, 0.25);
}

.hero .eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    letter-spacing: 0.22em;
    color: var(--cyan);
    text-transform: uppercase;
    margin-bottom: 10px;
}

.hero h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    letter-spacing: -0.01em;
    margin: 0;
    color: var(--parchment);
}

.hero p {
    font-family: 'IBM Plex Mono', monospace;
    color: var(--muted);
    font-size: 12.5px;
    letter-spacing: 0.05em;
    margin-top: 10px;
}

/* ---------- Section label ---------- */

.section-title {
    font-family: 'IBM Plex Mono', monospace;
    color: var(--brass);
    font-size: 12px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-title::after {
    content: "";
    flex: 1;
    height: 1px;
    background: rgba(201, 164, 104, 0.3);
}

/* ---------- Parcel card wrapper ---------- */

.parcel-card {
    position: relative;
    border: 1px solid rgba(95, 179, 212, 0.35);
    padding: 28px 26px 10px 26px;
    margin-bottom: 20px;
}

.parcel-card::before,
.parcel-card::after,
.parcel-card .tick-br,
.parcel-card .tick-bl {
    content: "";
    position: absolute;
    width: 14px;
    height: 14px;
    border: 2px solid var(--brass);
}

.parcel-card::before {
    top: -1px; left: -1px;
    border-right: none; border-bottom: none;
}

.parcel-card::after {
    top: -1px; right: -1px;
    border-left: none; border-bottom: none;
}

/* ---------- Inputs ---------- */

div[data-testid="stNumberInput"] label {
    font-family: 'IBM Plex Mono', monospace !important;
    color: var(--muted) !important;
    font-weight: 500 !important;
    font-size: 11.5px !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

div[data-testid="stNumberInput"] input {
    font-family: 'IBM Plex Mono', monospace !important;
    background-color: transparent !important;
    color: var(--parchment) !important;
    border: none !important;
    border-bottom: 1px solid rgba(95, 179, 212, 0.4) !important;
    border-radius: 0 !important;
    padding-left: 0 !important;
    font-size: 16px !important;
}

div[data-testid="stNumberInput"] input:focus {
    border-bottom: 1px solid var(--brass) !important;
    box-shadow: none !important;
}

div[data-testid="stNumberInput"] button {
    background-color: transparent !important;
    border: 1px solid rgba(95, 179, 212, 0.25) !important;
    color: var(--cyan) !important;
}

/* ---------- Button ---------- */

.stButton > button {
    width: 100%;
    height: 52px;
    border: 1px solid var(--brass);
    border-radius: 2px;
    background: transparent;
    color: var(--brass);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    transition: all 0.2s ease;
    margin-top: 12px;
}

.stButton > button:hover {
    background: rgba(201, 164, 104, 0.1);
    color: var(--parchment);
    border-color: var(--parchment);
}

/* ---------- Result stamp ---------- */

.stamp-wrap {
    display: flex;
    justify-content: center;
    margin-top: 32px;
    animation: stampIn 0.35s cubic-bezier(0.2, 0.9, 0.3, 1.2);
}

.stamp {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    border: 2px solid var(--brass);
    outline: 1px solid rgba(201, 164, 104, 0.35);
    outline-offset: 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}

.stamp .label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10.5px;
    letter-spacing: 0.2em;
    color: var(--cyan);
    text-transform: uppercase;
    margin-bottom: 8px;
}

.stamp .value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: var(--parchment);
}

.stamp .sub {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9.5px;
    color: var(--muted);
    letter-spacing: 0.1em;
    margin-top: 8px;
}

@keyframes stampIn {
    from { opacity: 0; transform: scale(1.4) rotate(-6deg); }
    to   { opacity: 1; transform: scale(1) rotate(0deg); }
}

/* ---------- Footer ---------- */

.footer {
    text-align: center;
    margin-top: 3rem;
    padding-top: 1.4rem;
    border-top: 1px solid rgba(95, 179, 212, 0.15);
    color: var(--muted);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10.5px;
    letter-spacing: 0.08em;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <div class="eyebrow">Parcel Assessment · Automated Valuation Model</div>
    <h1>MERIDIAN</h1>
    <p>ESTIMATE ISSUED FROM COORDINATE &amp; STRUCTURE DATA</p>
</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="section-title">Parcel Details</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="parcel-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    medinc = st.number_input(
        "Median Income (10k USD)",
        value=3.5,
        min_value=0.0
    )

    houseage = st.number_input(
        "House Age (yrs)",
        value=25.0,
        min_value=0.0
    )

    averooms = st.number_input(
        "Average Rooms",
        value=5.0,
        min_value=0.0
    )

    avebedrms = st.number_input(
        "Average Bedrooms",
        value=1.0,
        min_value=0.0
    )


with col2:

    population = st.number_input(
        "Block Population",
        value=1000.0,
        min_value=0.0
    )

    aveoccup = st.number_input(
        "Average Occupancy",
        value=3.0,
        min_value=0.0
    )

    latitude = st.number_input(
        "Latitude",
        value=34.0
    )

    longitude = st.number_input(
        "Longitude",
        value=-118.0
    )

st.markdown('</div>', unsafe_allow_html=True)


predict = st.button(
    "Run Appraisal"
)


if predict:

    input_data = pd.DataFrame(
        [[
            medinc,
            houseage,
            averooms,
            avebedrms,
            population,
            aveoccup,
            latitude,
            longitude
        ]],
        columns=[
            "MedInc",
            "HouseAge",
            "AveRooms",
            "AveBedrms",
            "Population",
            "AveOccup",
            "Latitude",
            "Longitude"
        ]
    )

    with st.spinner(
        "Surveying parcel and cross-referencing comparables..."
    ):

        time.sleep(1.2)

        prediction = model.predict(
            input_data
        )[0]

    st.markdown(f"""
    <div class="stamp-wrap">
        <div class="stamp">
            <div class="label">Appraised Value</div>
            <div class="value">${prediction * 100000:,.0f}</div>
            <div class="sub">LAT {latitude:.2f} · LON {longitude:.2f}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div class="footer">
    RANDOM FOREST REGRESSION · TRAINED ON CALIFORNIA HOUSING DATASET
</div>
""", unsafe_allow_html=True)
