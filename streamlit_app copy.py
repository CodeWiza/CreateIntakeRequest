import streamlit as st

# Define the sections dictionary
sections = {
    "Item Details": {"description": "Enter details about the item...", "previous_purchases": "..."},
    "Supplier Discovery": {"recommended_supplier": "...", "gl_account": "..."},
    "Accounting": {"cost_center": "...", "po_created_in": "..."},
    "Approvals": {"approver": "...", "po_issued_to": "..."},
    "Track Status": {"delivery_date": "...", "more_info": "..."}
}


# Set the current section to be displayed
current_section = "Item Details"

# Function to display a section
def show_section(section_name):
  st.header(section_name)
  st.write(sections[section_name]["description"])
  # Add more elements based on your data

  # Button to move to the next section
  if section_name != "Track Status":
    if st.button("Next"):
      global current_section
      next_index = (list(sections.keys()).index(current_section) + 1) % len(sections)
      current_section = list(sections.keys())[next_index]
      show_section(current_section)

# Function to display the circular progress bar
def show_progress_bar():
  progress_bar = st.empty()
  # Display progress bar based on current section
  if current_section == "Item Details":
    progress_bar.text("1 out of 5")
  elif current_section == "Supplier Discovery":
    progress_bar.text("2 out of 5")
  # Add logic for other sections
  else:
    progress_bar.text(f"{sections.keys().index(current_section) + 1} out of 5")

# Main app flow
st.set_page_config(layout="wide")

show_progress_bar()
show_section(current_section)

