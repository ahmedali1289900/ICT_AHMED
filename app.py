import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}

/* Main Title */
.main-title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* Card Styling */
.card {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Section Headers */
.section-header {
    color: #38bdf8;
    font-size: 28px;
    font-weight: bold;
    margin-bottom: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown('<div class="main-title">⚙️ Mechanical Unit Converter & Material Density Checker</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="sub-title">Professional Engineering Web App using Streamlit</div>',
    unsafe_allow_html=True
)

# =========================
# STUDENT INFO
# =========================
col1, col2 = st.columns(2)

with col1:
    st.info("👨‍🎓 **Name:** Ahmed Ali")

with col2:
    st.info("🆔 **Roll Number:** 25-ME-115")

st.markdown("---")

# =========================
# UNIT CONVERTER
# =========================
st.markdown('<div class="section-header">📏 Mechanical Unit Converter</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    conversion_type = st.selectbox(
        "Select Conversion Type",
        ["Length", "Force", "Pressure"]
    )

    # =========================
    # LENGTH
    # =========================
    if conversion_type == "Length":

        value = st.number_input("Enter Value", min_value=0.0)

        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox(
                "From",
                ["Meter", "Millimeter", "Centimeter"]
            )

        with col2:
            to_unit = st.selectbox(
                "To",
                ["Meter", "Millimeter", "Centimeter"]
            )

        # Convert to meters
        if from_unit == "Meter":
            meters = value
        elif from_unit == "Millimeter":
            meters = value / 1000
        else:
            meters = value / 100

        # Convert target
        if to_unit == "Meter":
            result = meters
        elif to_unit == "Millimeter":
            result = meters * 1000
        else:
            result = meters * 100

        st.success(f"✅ Converted Value = {result:.4f} {to_unit}")

    # =========================
    # FORCE
    # =========================
    elif conversion_type == "Force":

        value = st.number_input("Enter Value ", min_value=0.0)

        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox(
                "From ",
                ["Newton", "Kilonewton"]
            )

        with col2:
            to_unit = st.selectbox(
                "To ",
                ["Newton", "Kilonewton"]
            )

        if from_unit == "Newton":
            newton = value
        else:
            newton = value * 1000

        if to_unit == "Newton":
            result = newton
        else:
            result = newton / 1000

        st.success(f"✅ Converted Value = {result:.4f} {to_unit}")

    # =========================
    # PRESSURE
    # =========================
    elif conversion_type == "Pressure":

        value = st.number_input("Enter Value  ", min_value=0.0)

        col1, col2 = st.columns(2)

        with col1:
            from_unit = st.selectbox(
                "From  ",
                ["Pascal", "Kilopascal"]
            )

        with col2:
            to_unit = st.selectbox(
                "To  ",
                ["Pascal", "Kilopascal"]
            )

        if from_unit == "Pascal":
            pascal = value
        else:
            pascal = value * 1000

        if to_unit == "Pascal":
            result = pascal
        else:
            result = pascal / 1000

        st.success(f"✅ Converted Value = {result:.4f} {to_unit}")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# MATERIAL DENSITY CHECKER
# =========================
st.markdown('<div class="section-header">🧪 Material Density Checker</div>', unsafe_allow_html=True)

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Cast Iron": 7200,
    "Magnesium": 1740
}

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    selected_material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[selected_material]

    st.metric(
        label=f"Density of {selected_material}",
        value=f"{density} kg/m³"
    )

    # Density Status
    if density > 7000:
        st.warning("⚠️ High Density Material")
    elif density > 3000:
        st.info("ℹ️ Medium Density Material")
    else:
        st.success("✅ Lightweight Material")

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit | Mechanical Engineering Project</div>',
    unsafe_allow_html=True
)
st.caption("Made using Streamlit & GitHub")
