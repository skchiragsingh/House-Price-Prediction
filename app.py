import streamlit as st
import pandas as pd
import time

from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor


st.set_page_config(
    page_title="HomeValue | Price Predictor",
    page_icon="🏠",
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

.stApp {
    background:
        radial-gradient(
            circle at top left,
            rgba(59, 130, 246, 0.18),
            transparent 35%
        ),
        radial-gradient(
            circle at bottom right,
            rgba(16, 185, 129, 0.12),
            transparent 35%
        ),
        #0f172a;
}

.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.hero {
    text-align: center;
    margin-bottom: 2.5rem;
}

.logo {
    width: 78px;
    height: 78px;
    margin: auto;
    margin-bottom: 1rem;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 38px;

    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    border-radius: 22px;

    box-shadow:
        0 15px 40px
        rgba(37, 99, 235, 0.35);
}

.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
    color: #f8fafc;
}

.hero p {
    color: #94a3b8;
    font-size: 1.1rem;
}

.section-title {
    color: #f8fafc;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 20px;
}

div[data-testid="stNumberInput"] label {
    color: #cbd5e1 !important;
    font-weight: 600;
}

div[data-testid="stNumberInput"] input {
    background-color: #111827 !important;
    color: #f8fafc !important;
    border: 1px solid #475569 !important;
    border-radius: 10px !important;
}

.stButton > button {
    width: 100%;
    height: 54px;
    border: none;
    border-radius: 14px;

    background: linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );

    color: white;
    font-size: 17px;
    font-weight: 600;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow:
        0 12px 30px
        rgba(37, 99, 235, 0.35);
}

.prediction-card {
    margin-top: 25px;
    padding: 28px;

    text-align: center;

    background:
        rgba(16, 185, 129, 0.12);

    border:
        1px solid
        rgba(16, 185, 129, 0.4);

    border-radius: 18px;

    animation: fadeIn 0.4s ease;
}

.prediction-title {
    color: #94a3b8;
    font-size: 15px;
}

.prediction-value {
    color: #6ee7b7;
    font-size: 38px;
    font-weight: 800;
    margin-top: 8px;
}

.footer {
    text-align: center;
    margin-top: 3rem;
    color: #64748b;
    font-size: 14px;
}

@keyframes fadeIn {

    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">

    <div class="logo">🏠</div>

    <h1>HomeValue</h1>

    <p>
        AI-powered house price prediction using machine learning.
    </p>

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="section-title">Enter Property Details</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    medinc = st.number_input(
        "Median Income",
        value=3.5,
        min_value=0.0
    )

    houseage = st.number_input(
        "House Age",
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
        "Population",
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


predict = st.button(
    "✨ Predict House Price"
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
        "🤖 AI is analyzing property data..."
    ):

        time.sleep(1.5)

        prediction = model.predict(
            input_data
        )[0]

    st.markdown(f"""
    <div class="prediction-card">

        <div class="prediction-title">
            ESTIMATED HOUSE PRICE
        </div>

        <div class="prediction-value">
            ${prediction * 100000:,.0f}
        </div>

    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div class="footer">

    Powered by Machine Learning
    • Random Forest Regression
    • California Housing Dataset

</div>
""", unsafe_allow_html=True)
