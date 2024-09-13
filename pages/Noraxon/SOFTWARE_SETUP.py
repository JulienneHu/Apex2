import streamlit as st

st.title("Software Setup")

st.subheader("Getting Started")
st.image('assests/Noraxon/Getting_Started.png',caption="Click on MR 3.20 (in red circle)", width=600)

st.subheader("First screen when you open MR3")
st.image('assests/Noraxon/First_Screen.png', caption="Click “New Subject” (in red rectangle)", width=600)

st.image('assests/Noraxon/step1.png', caption="Once information has been entered, x out of the page", width=600)
st.image('assests/Noraxon/step2.png', caption="Click “Hardware Setup” (in red rectangle)", width=600)
st.image('assests/Noraxon/step3.png', caption="Click “Ultium” (in red rectangle)", width=600)
st.image('assests/Noraxon/step4.png', caption="Click “Detect Sensors in Chargers” (in red rectangle)", width=600)
st.image('assests/Noraxon/step5.png', caption="Click “Add” (in red rectangle)", width=600)
st.image('assests/Noraxon/step6.png', caption="Click “Activate” (in red rectangle)", width=600)
st.image('assests/Noraxon/step7.png', caption="1. Click =  and 0 (This makes data fluctuate around 0. 2. Click “Record”", width=600)
st.image('assests/Noraxon/step8.png', caption="NOTE: the first time you press record (waiting for start trigger) in MR3, it will NOT start the recording for the first iteration of start and stop in MVN. Once you start and stop recording in MVN (and discard data), then press start again in MVN, then it will start recording in MR3. Stop recording in MVN will work as intended in MR3 as well. ​The start trigger will be visible in the sync window as shown to the right, but not the stop trigger. This is fine as there is no delay in the stop recording so you would not see the falling edge of the sync signal, we are still getting the EMG data we need at the right start/stop times. EMG window should show data collected in that duration.”", width=600)
st.image('assests/Noraxon/step9.png', caption="Click “Save & View” (in red rectangle) to save recording", width=600)
st.image('assests/Noraxon/step10.png', caption="Clicking “Save & View” takes you to “Viewer” tab", width=600)
