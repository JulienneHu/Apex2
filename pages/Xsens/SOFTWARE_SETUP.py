import streamlit as st

st.title("Software Setup")  

st.subheader("Step1: Hardware Setup")
st.image('assests/Xsens/hardware_setup.png', caption='Step 1', width=400)
st.markdown("""The flash drive needs to be plugged into a laptop like this in order to active Analyze Pro """)

st.subheader("Step2: Confirming the Correct License")
st.image('assests/Xsens/confirm_license.png', caption='Step 2', width=400)
st.markdown("""License should be “Analyze Pro” not “Record”""")

st.subheader("Step3: Starting Motion Capture")
st.image('assests/Xsens/start_motion_capture.png', caption='Step 3', width=400)

st.subheader("Step4: Inputting Dimensions")
st.image('assests/Xsens/input_dimensions.png', caption='Step 4', width=400)
st.markdown("""Change the Body Height and Foot or Shoe length based on dimensions of each participant""")

st.subheader("Step5: Change Suit Configuration")
st.image('assests/Xsens/suit_configuration.png', caption='Step 5', width=400)
st.markdown("""After dimensions are inputted, change the suit configuration to full body, then click OK""")

st.subheader("Step6: Click Calibrate At the Left Menu")
st.image('assests/Xsens/click_calibrate.png', caption='Step 6', width=400)

st.subheader("Step7: Click Next")
st.image('assests/Xsens/click_next1.png', caption='Step 7', width=400)
st.image('assests/Xsens/click_next2.png', caption='Step 7', width=400)

st.subheader("Step8: Start Calibration")
st.image('assests/Xsens/start_calibration.png', caption='Step 8', width=400)

st.subheader("Step9: Calibration In Progress")
video = open("assests/Xsens/calibration.mov", "rb")
video_bytes = video.read()
st.video(video_bytes)

st.subheader("Step10: Calibration Complete and Save")
st.image('assests/Xsens/calibration_complete.png', caption='Step 10', width=400)
st.markdown("""Motion capture successful! Press Save""")