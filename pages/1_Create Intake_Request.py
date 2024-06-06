import streamlit as st
import extra_streamlit_components as stx
from st_btn_select import st_btn_select

# Set page configuration
st.set_page_config(page_title="Purchase Request System", layout="wide")

# Define the approval statuses
PENDING = "Pending"
IN_REVIEW = "In Review"
APPROVED = "Approved"

# Initialize session state for approval data
if "approvals" not in st.session_state:
    st.session_state.approvals = [
        {
            "name": "David Joanes",
            "title": "Supervisor",
            "typical_approval_time": "2 hrs",
            "status": PENDING
        },
        {
            "name": "Julian Philips",
            "title": "Cost Center Manager",
            "typical_approval_time": "5 hrs",
            "status": PENDING
        },
        {
            "name": "PO issued to supplier",
            "title": "",
            "typical_approval_time": "Same day or next day",
            "status": PENDING
        }
    ]

# Function to display the approval status
def display_approval_status(approval):
    name = approval["name"]
    title = approval["title"]
    typical_approval_time = approval["typical_approval_time"]
    status = approval["status"]

    color = "red" if status == PENDING else "yellow" if status == IN_REVIEW else "green"

    st.write(f"""
        <div>
            <span style="color: {color}; font-size: 20px; font-weight: bold;">&#9679;</span>
            <span>{name}</span>
            <br>
            <span style="font-size: 12px;">{title}</span>
            <br>
            <span style="font-size: 12px;">Typically approves in {typical_approval_time}</span>
        </div>
        <hr>
    """, unsafe_allow_html=True)

item_prompt = st.text_input("What are you looking for?")
if item_prompt:
    # Add confirmation buttons
    st.write("I understand it's a new purchase request, please confirm ")
    option = st_btn_select(('Yes', "No, it's a sourcing request"), index=1)

    # Display content only if 'Yes' is selected
    if option == 'Yes':
        # Add header
        st.header("Intake Purchase Request")

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
                product_ID = st.text_input("Product ID")
                product_name = st.text_input("Product Name")
                requester = st.text_input("Requester")
                category = st.text_input("Category")
                department = st.text_input("Department")
                ship_to_address = st.text_input("Ship to address")
                more_info = st.text_area("Quantity")
        elif selected_step == 1:
            with st.container():
                st.subheader("Buying Channel")
                st.caption("Recommended Supplier")
                supplier_data = {
                    "Source": ["Catalog Name", "Contract", "Preferred"],
                    "Supplier": [8, 6, 7],
                    "Document ID": ["Catalog ID", "Contract ID", ""],
                    "Item name": ["", "", ""],
                    "Price": ["", "", ""],
                    "SKU": ["", "", ""],
                    "Lead time": ["", "", ""]
                }
                st.table(supplier_data)

                st.caption("Delivery Date")
                choose_date = st.date_input("Choose Date")
                st.write("Supplier Score")
                score_data = {
                    "Parameter": ["Ontime", "Quality", "Price"],
                    "Quality": [8, 6, 7],
                    "Price": ["", "", ""],
                    "Finance": ["", "", ""],
                    "Score updated on": ["", "", ""]
                }
                st.table(score_data)

                st.caption("Supplier News")
                news_data = {
                    "News": ["", "", ""],
                    "News Summary": ["", "", ""],
                    "News Source": ["", "", ""],
                    "News update date": ["", "", ""]
                }
                st.table(news_data)
        elif selected_step == 2:
            with st.container():
                st.subheader("Accounting")
                cost_center = st.text_input("Cost Center")
                gl_account = st.text_input("GL Account")
        elif selected_step == 3:
            with st.container():
                st.subheader("Approvals")

                for approval in st.session_state.approvals:
                    display_approval_status(approval)

                # Add interactivity to update approval statuses
                st.subheader("Update Approval Status")
                selected_name = st.selectbox("Select Name", [approval["name"] for approval in st.session_state.approvals])
                selected_approval = next((approval for approval in st.session_state.approvals if approval["name"] == selected_name), None)

                if selected_approval:
                    current_status = selected_approval["status"]
                    new_status = st.selectbox("Select New Status", [PENDING, IN_REVIEW, APPROVED], index=[PENDING, IN_REVIEW, APPROVED].index(current_status))

                    if new_status != current_status:
                        selected_approval["status"] = new_status
                        st.success(f"Updated {selected_name}'s status to {new_status}")
        elif selected_step == 4:
            with st.container():
                st.subheader("Track Status")
                # Add any relevant status tracking components here

        if st.button('Next'):
            selected_step += 1
        if st.button('Previous'):
            selected_step -= 1