import streamlit as st

# Set page configuration
st.set_page_config(page_title="Purchase Request System", layout="wide")

# Add header
st.header("Intake Purchase Request - 1276")

# Add progress bar
progress_bar = st.progress(0.2)  # Assuming you're at the "Supplier Scoring" stage

# Add item details section
with st.container():
    st.subheader("Item Details")
    item_description = st.text_input("Item Description")
    requester = st.text_input("Requester")
    category = st.text_input("Category")
    department = st.text_input("Department")
    ship_to_address = st.text_input("Ship to address")
    more_info = st.text_area("More info about the supplier")

# Add supplier discovery section
with st.container():
    st.subheader("Supplier discovery")
    recommended_supplier = st.text_input("Recommended Supplier")
    supplier_score = st.text_input("Supplier Score / Previous Purchases")
    delivery_date = st.date_input("Delivery Date")

# Add accounting section
with st.container():
    st.subheader("Accounting")
    cost_center = st.text_input("Cost Center")
    gl_account = st.text_input("GL Account")

# Add approvals section
with st.container():
    st.subheader("Approvals")
    st.write("David Joanes, Supervisor - Typically approves in 2 hrs")
    st.write("Julian Philips, Cost Center Manager - Typically approves in 5 hrs")
    st.write("PO issued to supplier - Typically same day or next day")

# Add track status section
with st.container():
    st.subheader("Track Status")
    # Add any relevant status tracking components here

# Add confirmation buttons
confirm = st.button("Yes")
sourcing_request = st.button("No, it's a Sourcing Request")