import streamlit as st
import extra_streamlit_components as stx

# Set page configuration
st.set_page_config(page_title="Purchase Request System", layout="wide")

# Add header
st.header("Intake Purchase Request - 1276")

# Define tab bar data
tab_bar_data = [
    stx.TabBarItemData(id=1, title="Item Details", description="Enter item details"),
    stx.TabBarItemData(id=2, title="Supplier Discovery", description="Supplier information"),
    stx.TabBarItemData(id=3, title="Accounting", description="Cost center and GL account"),
    stx.TabBarItemData(id=4, title="Approvals", description="Approval workflow"),
    stx.TabBarItemData(id=5, title="Track Status", description="Track request status")
]

# Add tab bar
selected_tab_id = stx.tab_bar(data=tab_bar_data, default=1)

# Render content based on selected tab
if selected_tab_id == 1:
    with st.container():
        st.subheader("Item Details")
        item_description = st.text_input("Item Description")
        requester = st.text_input("Requester")
        category = st.text_input("Category")
        department = st.text_input("Department")
        ship_to_address = st.text_input("Ship to address")
        more_info = st.text_area("More info about the supplier")
elif selected_tab_id == 2:
    with st.container():
        st.subheader("Supplier discovery")
        recommended_supplier = st.text_input("Recommended Supplier")
        supplier_score = st.text_input("Supplier Score / Previous Purchases")
        delivery_date = st.date_input("Delivery Date")
elif selected_tab_id == 3:
    with st.container():
        st.subheader("Accounting")
        cost_center = st.text_input("Cost Center")
        gl_account = st.text_input("GL Account")
elif selected_tab_id == 4:
    with st.container():
        st.subheader("Approvals")
        st.write("David Joanes, Supervisor - Typically approves in 2 hrs")
        st.write("Julian Philips, Cost Center Manager - Typically approves in 5 hrs")
        st.write("PO issued to supplier - Typically same day or next day")
elif selected_tab_id == 5:
    with st.container():
        st.subheader("Track Status")
        # Add any relevant status tracking components here

# Add confirmation buttons
confirm = st.button("Yes")
sourcing_request = st.button("No, it's a Sourcing Request")