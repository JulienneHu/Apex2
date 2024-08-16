import streamlit as st
import pandas as pd

# Function to recommend shoulder straps size based on chest circumference
def recommend_shoulder_straps(height, chest_circumference):
    if height < 180:
        if 74 <= chest_circumference < 86:
            return "Size 1"
        elif 86 <= chest_circumference < 92:
            return "Size 2"
        elif 92 <= chest_circumference < 103:
            return "Size 3"
        elif 103 <= chest_circumference < 119:
            return "Size 4"
    else:
        if 103 <= chest_circumference < 119:
            return "Size 5"
        elif chest_circumference >= 123:
            return "Size 6"
    return "Size not found"

# Function to recommend band size based on height
def recommend_band_size(height):
    if height <= 160:
        return "Size 1"
    elif 160 < height <= 170:
        return "Size 2"
    elif 170 < height <= 183:
        return "Size 3"
    elif 183 < height <= 193:
        return "Size 4"
    elif 193 < height <= 200:
        return "Size 5"
    elif height > 200:
        return "Size 6"
    return "Size not found"

# Function to recommend thigh sleeves size based on thigh circumference
def recommend_thigh_sleeves(circumference):
    if 44 <= circumference <= 60:
        return "Size 1"
    elif 58 <= circumference <= 70:
        return "Size 2"
    elif 66 <= circumference <= 80:
        return "Size 3"
    return "Size not found"


st.title("HeroWear Apex2 Sizing Guide")
st.header("Input your measurements")


height = st.number_input("Enter your height (in cm):", min_value=100, max_value=250, step=1)
chest_circumference = st.number_input("Enter your chest circumference (in cm):", min_value=74, max_value=150, step=1)
thigh_circumference = st.number_input("Enter your thigh circumference (in cm):", min_value=44, max_value=100, step=1)

if st.button("Get Recommendations"):
    shoulder_straps = recommend_shoulder_straps(height, chest_circumference)
    band_size = recommend_band_size(height)
    thigh_sleeves = recommend_thigh_sleeves(thigh_circumference)

    st.subheader("Recommended Sizes")
    st.write(f"**Shoulder Straps:** {shoulder_straps}")
    st.write(f"**Bands:** {band_size}")
    st.write(f"**Thigh Sleeves:** {thigh_sleeves}")


shoulder_straps_data = {
    "Height": ["Under 6' Tall", "6' Tall and Up"],
    "Size 1": ["30\" - 34\"<br>(74 cm - 86 cm)", ""],
    "Size 2": ["34\" - 38\"<br>(86 cm - 92 cm)", ""],
    "Size 3": ["38\" - 42\"<br>(92 cm - 103 cm)", ""],
    "Size 4": ["42\" - 47\"<br>(103 cm - 119 cm)", ""],
    "Size 5": ["", "42\" - 47\"<br>(103 cm - 119 cm)"],
    "Size 6": ["", "48\" - 54\"+<br>(123 cm - 134 cm)"]
}

thigh_sleeves_data = {
    "Size": ["Size 1", "Size 2", "Size 3"],
    "Thigh Circumference": [
        "17\" - 24\"<br>(44 cm - 60 cm)", 
        "22.8\" - 27.5\"<br>(58 cm - 70 cm)", 
        "25.9\" - 31.4\"<br>(66 cm - 80 cm)"
    ]
}

bands_data = {
    "Strength": ["S1000", "S1500", "S2000"],
    "Size 1": ["5'3\" and shorter<br>(160 cm)", "5'3\" and shorter<br>(160 cm)", ""],
    "Size 2": [
        "5'3\" - 5'7\"<br>(160 cm - 170 cm)", 
        "5'3\" - 5'7\"<br>(160 cm - 170 cm)", 
        "5'3\" - 5'7\"<br>(160 cm - 170 cm)"
    ],
    "Size 3": [
        "5'7\" - 6'0\"<br>(170 cm - 183 cm)", 
        "5'7\" - 6'0\"<br>(170 cm - 183 cm)", 
        "5'7\" - 6'0\"<br>(170 cm - 183 cm)"
    ],
    "Size 4": [
        "6'0\" - 6'4\"<br>(183 cm - 193 cm)", 
        "6'0\" - 6'4\"<br>(183 cm - 193 cm)", 
        "6'0\" - 6'4\"<br>(183 cm - 193 cm)"
    ],
    "Size 5": [
        "6'4\" - 6'7\"<br>(193 cm - 200 cm)", 
        "6'4\" - 6'7\"<br>(193 cm - 200 cm)", 
        "6'4\" - 6'7\"<br>(193 cm - 200 cm)"
    ],
    "Size 6": ["6'7\"+<br>(200 cm+)", "6'7\"+<br>(200 cm+)", "6'7\"+<br>(200 cm+)"]
}


shoulder_straps_df = pd.DataFrame(shoulder_straps_data)
thigh_sleeves_df = pd.DataFrame(thigh_sleeves_data)
bands_df = pd.DataFrame(bands_data)

st.subheader("Shoulder Straps Table")
st.markdown(shoulder_straps_df.to_html(escape=False, index=False), unsafe_allow_html=True)

st.subheader("Thigh Sleeves Table")
st.markdown(thigh_sleeves_df.to_html(escape=False, index=False), unsafe_allow_html=True)

st.subheader("Bands Table")
st.markdown(bands_df.to_html(escape=False, index=False), unsafe_allow_html=True)
