import streamlit as st
import extra_streamlit_components as stx
from st_btn_select import st_btn_select

# Set page configuration
st.set_page_config(page_title="Purchase Request System", layout="wide")
item_prompt = st.text_input("What are you looking for?")

if item_prompt is not None:
    # Add confirmation buttons
    st.write("I understand its a new purchase request, please confirm ")
    option = st_btn_select(('Yes', "No, it's a sourcing request"))
    #st.write(f'Selected option: {option}')

    # Add header
    st.header("Intake Purchase Request - 1276")

    # Define stepper bar steps
    steps = [
        "Item Details",
        "Supplier Discovery",
        "Accounting",
        "Approvals",
        "Track Status"
    ]

    # Add stepper bar
    selected_step = stx.stepper_bar(steps=steps)

    # Render content based on selected step
    if selected_step == 0:
        with st.container():
            st.subheader("Item Details")
            item_description = st.text_input("Item Description")
            requester = st.text_input("Requester")
            category = st.text_input("Category")
            department = st.text_input("Department")
            ship_to_address = st.text_input("Ship to address")
            more_info = st.text_area("More info about the supplier")
    elif selected_step == 1:
        with st.container():
            st.subheader("Supplier Discovery")
            recommended_supplier = st.text_input("Recommended Supplier")
            supplier_score = st.text_input("Supplier Score / Previous Purchases")
            delivery_date = st.date_input("Delivery Date")
    elif selected_step == 2:
        with st.container():
            st.subheader("Accounting")
            cost_center = st.text_input("Cost Center")
            gl_account = st.text_input("GL Account")
    elif selected_step == 3:
        with st.container():
            st.subheader("Approvals")
            st.write("David Joanes, Supervisor - Typically approves in 2 hrs")
            st.write("Julian Philips, Cost Center Manager - Typically approves in 5 hrs")
            st.write("PO issued to supplier - Typically same day or next day")
    elif selected_step == 4:
        with st.container():
            st.subheader("Track Status")
            # Add any relevant status tracking components here

    

