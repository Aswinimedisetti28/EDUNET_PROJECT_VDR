import streamlit as st
import cv2
import os
from PIL import Image

def show():
    st.markdown("<h1 style='text-align: center;'>📸 Virtual Try-On</h1>", unsafe_allow_html=True)

    # 📸 Open Camera
    capture = st.button("📷 Open Camera & Take Picture")
    
    if capture:
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("⚠️ Camera not detected.")
                break
            cv2.imshow("Press 'c' to capture | 'q' to exit", frame)
            key = cv2.waitKey(1)
            if key == ord('c'):
                cv2.imwrite("assets/captured_image.jpg", frame)
                st.success("✅ Image Captured!")
                break
            elif key == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    # 📌 Show Captured Image & Clothing Options
    if os.path.exists("assets/captured_image.jpg"):
        st.image("assets/captured_image.jpg", caption="📷 Your Captured Image", use_container_width=True)

        # Display Clothing Images
        clothing_images = {file.split(".")[0]: f"assets/clothes/{file}" for file in os.listdir("assets/clothes") if file.endswith(("png", "jpg"))}
        cols = st.columns(len(clothing_images))
        
        selected_clothing = None
        for i, (name, path) in enumerate(clothing_images.items()):
            with cols[i]:
                if st.button(name):
                    selected_clothing = path
                st.image(path, caption=name, use_container_width=True)

        # Apply Selected Clothing
        if selected_clothing:
            st.image(selected_clothing, caption=f"👕 Applied: {selected_clothing}", use_container_width=True)
            st.success(f"✅ {selected_clothing} applied successfully!")
