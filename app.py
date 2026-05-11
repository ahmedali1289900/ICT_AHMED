import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Converter", page_icon="⚙️", layout="wide")

# Custom CSS for Professional Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stHeader {
        color: #1E3A8A;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1E3A8A;
        color: white;
        text-align: center;
        padding: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar / Header with Logo and Info
with st.container():
    col1, col2 = st.columns([1, 4])
    with col1:
        # Professional Mechanical Logo
        st.image("https://cdn-icons-png.flaticon.com/512/603/603173.png", width=100)
    with col2:
        st.title("Mechanical Unit Converter & Material Density Checker")
        st.subheader("Student Details")
        st.write("**Full Name:** Ahmed Ali")
        st.write("**Roll Number:** 25-ME-115")

st.divider()

# Navigation Tabs
tab1, tab2 = st.tabs(["📏 Unit Converter", "🔬 Density Checker"])

with tab1:
    st.header("Engineering Unit Conversion")
    conversion_type = st.selectbox("Select Dimension", ["Length", "Pressure", "Force", "Energy"])

    col_input, col_output = st.columns(2)

    if conversion_type == "Length":
        units = {"Meters": 1, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084}
    elif conversion_type == "Pressure":
        units = {"Pascal": 1, "Bar": 1e-5, "PSI": 0.000145038, "Atm": 9.8692e-6}
    elif conversion_type == "Force":
        units = {"Newton": 1, "KiloNewton": 0.001, "Pound-force": 0.224809}
    elif conversion_type == "Energy":
        units = {"Joule": 1, "KiloJoule": 0.001, "Calories": 0.239006, "BTU": 0.000947817}

    with col_input:
        val = st.number_input("Enter Value", value=1.0)
        from_unit = st.selectbox("From", list(units.keys()))
    
    with col_output:
        to_unit = st.selectbox("To", list(units.keys()))
        # Conversion Logic: (Value / From_Rate) * To_Rate
        result = (val / units[from_unit]) * units[to_unit]
        st.metric(label="Converted Value", value=f"{result:.4f} {to_unit}")

with tab2:
    st.header("Material Density Reference")
    st.write("Search for common engineering materials and their densities.")
    
    # Material Data
    data = {
        "Material": ["Steel", "Aluminum", "Copper", "Titanium", "Cast Iron", "PVC", "Concrete"],
        "Density (kg/m³)": [7850, 2700, 8960, 4500, 7200, 1400, 2400],
        "Modulus of Elasticity (GPa)": [200, 70, 117, 114, 110, 3, 30]
    }
    df = pd.DataFrame(data)
    
    search = st.text_input("Search Material (e.g., Steel)")
    if search:
        filtered_df = df[df['Material'].str.contains(search, case=False)]
        st.table(filtered_df)
    else:
        st.table(df)

# Footer
st.markdown("""<div class="footer">Mechanical Engineering Department - 25-ME-115</div>""", unsafe_allow_html=True)
