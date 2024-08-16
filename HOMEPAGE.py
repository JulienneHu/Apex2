import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="HeroWear Apex2 Sizing Guide",
    page_icon="🦸‍♂️",  # You can use an emoji as an icon or a link to an image
    layout="wide",  # 'centered' or 'wide'
    initial_sidebar_state="expanded"  # 'expanded' or 'collapsed'
)

st.title("Welcome to the HeroWear Apex2 Sizing Guide")

st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://herowearexo.com/wp-content/uploads/MG_5074-23-23-edit-scaled-e1678235727752-1188x720.jpg' width='700'>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("About This App")
st.write("""
This application is designed to help you find the perfect size for the HeroWear Apex2 exosuit. 
By inputting your height, chest circumference, and thigh circumference, 
the app will recommend the best fit for shoulder straps, thigh sleeves, and bands.
""")
