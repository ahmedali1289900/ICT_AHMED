import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Title
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

# Student Information
st.markdown("### Developed By")
st.write("**Name:** Ahmed Ali")
st.write("**Roll Number:** 25-ME-115")

st.markdown("---")

# =========================
# UNIT CONVERTER SECTION
# =========================
st.header("📏 Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Force", "Pressure"]
)

# LENGTH CONVERSION
if conversion_type == "Length":
    value = st.number_input("Enter value", min_value=0.0)

    from_unit = st.selectbox("From", ["Meter", "Millimeter", "Centimeter"])
    to_unit = st.selectbox("To", ["Meter", "Millimeter", "Centimeter"])

    # Convert to meters first
    if from_unit == "Meter":
        meters = value
    elif from_unit == "Millimeter":
        meters = value / 1000
    else:
        meters = value / 100

    # Convert to target
    if to_unit == "Meter":
        result = meters
    elif to_unit == "Millimeter":
        result = meters * 1000
    else:
        result = meters * 100

    st.success(f"Converted Value = {result}")

# FORCE CONVERSION
elif conversion_type == "Force":
    value = st.number_input("Enter value ", min_value=0.0)

    from_unit = st.selectbox("From ", ["Newton", "Kilonewton"])
    to_unit = st.selectbox("To ", ["Newton", "Kilonewton"])

    if from_unit == "Newton":
        newton = value
    else:
        newton = value * 1000

    if to_unit == "Newton":
        result = newton
    else:
        result = newton / 1000

    st.success(f"Converted Value = {result}")

# PRESSURE CONVERSION
elif conversion_type == "Pressure":
    value = st.number_input("Enter value  ", min_value=0.0)

    from_unit = st.selectbox("From  ", ["Pascal", "Kilopascal"])
    to_unit = st.selectbox("To  ", ["Pascal", "Kilopascal"])

    if from_unit == "Pascal":
        pascal = value
    else:
        pascal = value * 1000

    if to_unit == "Pascal":
        result = pascal
    else:
        result = pascal / 1000

    st.success(f"Converted Value = {result}")

st.markdown("---")

# =========================
# MATERIAL DENSITY CHECKER
# =========================
st.header("🧪 Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500
}

selected_material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[selected_material]

st.info(f"Density of {selected_material} = {density} kg/m³")

st.markdown("---")
st.caption("Made using Streamlit & GitHub")
