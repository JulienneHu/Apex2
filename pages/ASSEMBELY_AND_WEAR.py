import streamlit as st

st.title("How to Assemble the Apex2")
st.subheader("Step 1: Take out all required parts")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step1.jpg', caption='Step 1', width=400)
st.subheader("Step 2: Rotate clockwise to lock the clutch on the back support")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step2.jpg', caption='Step 2', width=400)
st.subheader("Step 3: Back view of the assembled part")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step3.jpg', caption='Step 3', width=400)
st.subheader("Step 4: Slide the bands to the clutch")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step4.jpg', caption='Step 4', width=400)
st.subheader("Step 5:Set all the bands to the clutch")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step5.jpg', caption='Step 5', width=400)   
st.subheader("Step 6: Set all the thigh sleeves to the bands conencted to the clutch")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step6.jpg', caption='Step 6', width=400)
st.subheader("Step 7: Final look of the assembled Apex2")
st.image('/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Step7.jpg', caption='Step 7', width=400)



st.subheader("Reference Videos")
video = open("/Users/julienne_hu/Desktop/Apex2/Web/assests/Apex2/Apex2.mov", "rb")
video_bytes = video.read()
st.video(video_bytes)

VIDEO_URL = "https://www.youtube.com/watch?v=JlH979tmzUg"
st.video(VIDEO_URL)

st.title("How to Wear the Apex2") 
VIDEO_URL = "https://www.youtube.com/watch?v=qBY_dm6FRdo&list=PLVJQIJn1dSyTd1jcVBI7VKILt_J-QA8pw&index=6"
st.video(VIDEO_URL)