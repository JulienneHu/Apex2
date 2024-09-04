import streamlit as st
import importlib.util

# Set page config once at the start of app.py
st.set_page_config(
    page_title="Devices Guide",
    page_icon="🦸‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("MENU")

# Main pages
main_page = st.sidebar.selectbox(
    "DEVICES", 
    ["Apex2", "Xsens"]
)

if main_page == "Apex2":
    apex2_page = st.sidebar.radio(
        "Apex2 Pages",
        ["APEX2", "ABOUT_APEX2", "MEASUREMENT", "ASSEMBLY_AND_WEAR"]
    )
elif main_page == "Xsens":
    xsens_page = st.sidebar.radio(
        "Xsens Pages",
        ["XSENS", "ABOUT_XSENS"]
    )

# Display content in the main area based on selection
if main_page == "Apex2":
    if apex2_page == "APEX2":
        # Load 'APEX2.py' content
        spec = importlib.util.spec_from_file_location("APEX2", "pages/Apex2/APEX2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    elif apex2_page == "ABOUT_APEX2":
        # Load 'ABOUT_APEX2.py' content
        spec = importlib.util.spec_from_file_location("ABOUT_APEX2", "pages/Apex2/ABOUT_APEX2.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    elif apex2_page == "ASSEMBLY_AND_WEAR":
        # Load 'ASSEMBLY_AND_WEAR.py' content
        spec = importlib.util.spec_from_file_location("ASSEMBLY_AND_WEAR", "pages/Apex2/ASSEMBELY_AND_WEAR.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    elif apex2_page == "MEASUREMENT":
        # Load 'MEASUREMENT.py' content
        spec = importlib.util.spec_from_file_location("MEASUREMENT", "pages/Apex2/MEASUREMENT.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

elif main_page == "Xsens":
    if xsens_page == "XSENS":
        # Load 'XSENS.py' content
        spec = importlib.util.spec_from_file_location("XSENS", "pages/Xsens/XSENS.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    elif xsens_page == "ABOUT_XSENS":
        # Load 'ABOUT_XSENS.py' content
        spec = importlib.util.spec_from_file_location("ABOUT_XSENS", "pages/Xsens/ABOUT_XSENS.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
