import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from google.cloud import firestore

def budget_app():
    st.title("Budget Tracker App")
    st.divider()

    st.title('Husam payments: ')
    st.divider()
    start_date5 = datetime(2023, 12, 1)
    end_date5 = datetime(2023, 12, 31)

    # Create a list of days for December
    day_list5 = [start_date5 + timedelta(days=x) for x in range((end_date5 - start_date5).days + 1)]

    # Create a DataFrame with columns 'Date', 'Day', and 'Day_Name'
    df5 = pd.DataFrame({'Date': day_list5, 'Day': [d.day for d in day_list5], 'Day_Name': [d.strftime('%A') for d in day_list5]})

    # Create a list of dates for December
    date_list5 = [start_date5 + timedelta(days=x) for x in range((end_date5 - start_date5).days + 1)]

    if ("is_initialized5" not in st.session_state) or not st.session_state["is_initialized5"]:
        # Created a data table
        _data5 = pd.DataFrame({
            "Days": df5['Day_Name'],
            "Date":date_list5,
            "Payment":[0] * len(day_list5)
        })

        # Setting state variables
        st.session_state["data5"] = _data5
        st.session_state["is_edit_mode5"] = False
        st.session_state["edit_button_label5"] = "Edit5"

        st.session_state["is_initialized5"] = True
    def toggle_edit_mode(enabled: bool):
        st.session_state["is_edit_mode5"] = enabled

        if enabled:
            st.session_state["edit_button_label5"] = "Editing5..."
        else:
            st.session_state["edit_button_label5"] = "Edit5"

    # Callbacks
    def on_reset_button_click():
        st.session_state["is_initialized5"] = False

    def on_edit_button_click():
        toggle_edit_mode(True)

    def on_save_button_click(new_data5: pd.DataFrame):
        toggle_edit_mode(False)
        st.session_state["data5"] = new_data5

    def on_cancel_button_click():
        toggle_edit_mode(False)


    st.button(st.session_state["edit_button_label5"],
            on_click=on_edit_button_click,
            disabled=st.session_state["is_edit_mode5"])


    # State-based layout
    if st.session_state["is_edit_mode5"]:
        # Edit mode layout
        new_data5 = st.data_editor(st.session_state["data5"],
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
            st.button("Cancel5", type="secondary", on_click=on_cancel_button_click)
        with cols[1]:
            st.button("Save5", type="primary", on_click=on_save_button_click, args=(new_data5, ))
    else:
        # Viewing mode layout
        st.table(st.session_state["data5"])
        gpa = st.session_state["data5"]["Payment"].sum()
        st.write("Counted payments:", f'{gpa}')

        st.button("Reset", on_click=on_reset_button_click)

    # Display GPA
    db5 = firestore.Client.from_service_account_json("budjet-7a5ac-firebase-adminsdk-iohd5-9a378ad90d.json")
    if st.button("Save to Firestore", key='save_firestore'):
        # Assuming _data5 is a Pandas DataFrame
        if "data5" not in st.session_state:
            st.error("Data not found. Please load or create the data first.")
        else:
            # Create a reference to the Firestore collection
            collection_ref = db5.collection("Payment")

            # Iterate over the DataFrame and add each record to Firestore
            done_flag = False  # Initialize the flag

            for _, row in st.session_state["data5"].iterrows():
                record = row.to_dict()
                doc_ref = collection_ref.add(record)[1]
                edited_value5 = record.get('fieldName')  # Adjust 'fieldName' to the actual field name in your document

                # Optionally, retrieve and display the last added document
                if "doc_ref" in locals():
                    doc = doc_ref.get()
                    # st.write("The id is:", doc5.id)

            # Set the flag to True once the loop is done
            done_flag = True

            # Display 'Done...' only once
            if done_flag:
                st.write('Done...')
                st.write(f"Edited Value: {edited_value5}")

