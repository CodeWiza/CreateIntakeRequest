import streamlit as st
import base64


def inject_sidebar_logo(image_path):
    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    # Inject custom CSS to display the logo at the top of the sidebar
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding-top: 20px;
        }}
        [data-testid="stSidebar"]::before {{
            content: '';
            display: block;
            height: 0;
            width: 80%;
            background-image: url(data:image/png;base64,{encoded_image});
            background-size: contain;
            background-repeat: no-repeat;
            background-position: left;
            padding-top: 80px;  /* Adjust this value to control logo height */
            margin-bottom: 2px;
            border-radius: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
