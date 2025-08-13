import streamlit as st
from packaging import version

supports_use_container_width = version.parse(st.__version__) >= version.parse("1.12.0")


st.set_page_config(
    page_title="AI_Healthcare",
    page_icon="",
    layout="wide"
)

# Custom CSS for Styling
st.markdown("""
    <style>
        

        body {
            font-family: 'Poppins', sans-serif;
            background-color: #0d1b2a;
            color: #e0e0e0;
        }

        /* Main Title */
        .title {
            font-size: 50px;
            font-weight: 600;
            color: #1e90ff;
            text-align: center;
            margin-bottom: 10px;
            
        }

        /* Subtitle */
        .subtitle {
            font-size: 24px;
            color: #black;
            text-align: center;
            font-weight: 300;
            margin-bottom: 40px;
        }

        /* Sections */
        .section {
            background: #1e1e1e;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
            transition: all 0.3s ease-in-out;
        }

        .section:hover {
            transform: translateY(-5px);
            box-shadow: 0px 6px 16px rgba(255, 255, 255, 0.2);
        }


      

        

    </style>
""", unsafe_allow_html=True)

# Main Content
st.markdown("<div class='title'>Artificial Intelligence for Healthcare </div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Transforming Healthcare with AI-driven Predictions & Insights</div>", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='section'>
        <h3>Disease Prediction</h3>
        <p>Analyze symptoms and predict possible diseases using advanced AI models.</p>
    </div>

    <div class='section'>
        <h3>Drug Recommendation</h3>
        <p>Get AI-powered medication suggestions based on medical history and diagnosis.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='section'>
        <h3>Heart Disease Risk Assessment</h3>
        <p>Assess your heart health and receive AI-powered risk analysis.</p>
    </div>

    
    """, unsafe_allow_html=True)

st.markdown("---")

# Technologies Used
st.markdown("<h2 style='text-align: center; color: #ffffff;'> Technologies Used</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='section'>
        <h3>Machine Learning</h3>
        <p>Utilizing RandomForest, XGBoost, and Deep Learning models.</p>
    </div>
    """, unsafe_allow_html=True)



with col2:
    st.markdown("""
    <div class='section'>
        <h3>Cloud Computing</h3>
        <p>Deployed using AWS, GCP, and Streamlit Cloud.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Why Use This App? (Separate Block)
st.markdown("""
    <div class='section'>
        <h2 style='text-align: center; color: #ffffff;'>Why Use This App?</h2>
        <p>
            <b>Accurate Predictions:</b> Our AI models are trained on vast healthcare datasets.<br>
            <b>Real-Time Assistance:</b> Get quick insights and recommendations.<br>
            <b>User-Friendly Interface:</b> Designed for both professionals and individuals.<br>
            <b>Secure & Reliable:</b> Your health data is protected with top-tier security.<br>
        </p>
    </div>
    """ , unsafe_allow_html=True)

