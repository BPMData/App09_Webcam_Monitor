import cv2
import streamlit as st
import time
from time import strftime
def ord(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

daymonth = time.strftime("%A, %B ")
date = ord(int(time.strftime("%d")))
dayofyear = ord(int(time.strftime("%j")))


timer_text = f"{daymonth}{date}"


st.title("Motion Detector")
start = st.button("Start Camera")




if start:
    streamlit_image = st.image([])
    webcam = cv2.VideoCapture(0)


    current_time = time.strftime("%I:%M:%S %p")
    last_update_time = time.time()
    update_interval = 0.9  # Update current_time every 0.5 seconds
    time_text = f"{current_time}"

    while True:
        check, frame = webcam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Update current_time at the specified interval
        if time.time() - last_update_time > update_interval:
            current_time = time.strftime("%I:%M:%S %p")
            last_update_time = time.time()
            time_text = f"{current_time}"
            print("Time Updated")

        cv2.putText(img=frame, text=timer_text, org=(360, 435),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(240, 255, 60),
                    thickness=2, lineType=cv2.LINE_AA) # Classic camcorder yellow with that 240,255,60

        cv2.putText(img=frame, text=time_text, org=(360, 465),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(240, 255, 60),
                    thickness=2, lineType=cv2.LINE_AA) # Classic camcorder yellow with that 240,255,60

        streamlit_image.image(frame)