import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from google.cloud import firestore

def budget_app():
    st.title("Budget Tracker App")
    st.divider()

    st.title('Tarek payments: ')
    st.divider()
    start_date1 = datetime(2023, 12, 1)
    end_date1 = datetime(2023, 12, 31)

    # Create a list of days for December
    day_list1 = [start_date1 + timedelta(days=x) for x in range((end_date1 - start_date1).days + 1)]

    # Create a DataFrame with columns 'Date', 'Day', and 'Day_Name'
    df1 = pd.DataFrame({'Date': day_list1, 'Day': [d.day for d in day_list1], 'Day_Name': [d.strftime('%A') for d in day_list1]})

    # Create a list of dates for December
    date_list1 = [start_date1 + timedelta(days=x) for x in range((end_date1 - start_date1).days + 1)]

    if ("is_initialized1" not in st.session_state) or not st.session_state["is_initialized1"]:
        # Created a data table
        _data1 = pd.DataFrame({
            "Days": df1['Day_Name'],
            "Date":date_list1,
            "Payment":[0] * len(day_list1)
        })

        # Setting state variables
        st.session_state["data1"] = _data1
        st.session_state["is_edit_mode1"] = False
        st.session_state["edit_button_label1"] = "Edit1"

        st.session_state["is_initialized1"] = True
    def toggle_edit_mode(enabled: bool):
        st.session_state["is_edit_mode1"] = enabled

        if enabled:
            st.session_state["edit_button_label1"] = "Editing1..."
        else:
            st.session_state["edit_button_label1"] = "Edit1"

    # Callbacks
    def on_reset_button_click():
        st.session_state["is_initialized1"] = False

    def on_edit_button_click():
        toggle_edit_mode(True)

    def on_save_button_click(new_data1: pd.DataFrame):
        toggle_edit_mode(False)
        st.session_state["data1"] = new_data1

    def on_cancel_button_click():
        toggle_edit_mode(False)


    st.button(st.session_state["edit_button_label1"],
            on_click=on_edit_button_click,
            disabled=st.session_state["is_edit_mode1"])


    # State-based layout
    if st.session_state["is_edit_mode1"]:
        # Edit mode layout
        new_data1 = st.data_editor(st.session_state["data1"],
                                disabled=["Days", "Date"],
                                use_container_width=True)

        # Fitting the columns to the width of their elements (i.e., buttons)
        st.markdown("""
                    <style>
                        div[data-testid="column"] {
                            width: fit-content !important;
                            flex: unset;
                        }
                        div[data-testid="column"] * {
                            width: fit-content !important;
                        }
                    </style>
                    """, unsafe_allow_html=True)

        cols = st.columns(2)
        with cols[0]:
            st.button("Cancel1", type="secondary", on_click=on_cancel_button_click)
        with cols[1]:
            st.button("Save1", type="primary", on_click=on_save_button_click, args=(new_data1, ))
    else:
        # Viewing mode layout
        st.table(st.session_state["data1"])
        gpa = st.session_state["data1"]["Payment"].sum()
        st.write("Counted payments:", f'{gpa}')

        st.button("Reset", on_click=on_reset_button_click)

    # Display GPA
    db1 = firestore.Client.from_service_account_json("budjet-7a5ac-firebase-adminsdk-iohd5-9a378ad90d.json")
    if st.button("Save to Firestore", key='save_firestore'):
        # Assuming _data5 is a Pandas DataFrame
        if "data1" not in st.session_state:
            st.error("Data not found. Please load or create the data first.")
        else:
            # Create a reference to the Firestore collection
            collection_ref = db1.collection("Payment")

            # Iterate over the DataFrame and add each record to Firestore
            done_flag = False  # Initialize the flag

            for _, row in st.session_state["data1"].iterrows():
                record = row.to_dict()
                doc_ref = collection_ref.add(record)[1]
                edited_value1 = record.get('fieldName')  # Adjust 'fieldName' to the actual field name in your document

                # Optionally, retrieve and display the last added document
                if "doc_ref" in locals():
                    doc = doc_ref.get()
                    # st.write("The id is:", doc5.id)

            # Set the flag to True once the loop is done
            done_flag = True

            # Display 'Done...' only once
            if done_flag:
                st.write('Done...')
                st.write(f"Edited Value: {edited_value1}")

if __name__ == "__main__":
    budget_app()

