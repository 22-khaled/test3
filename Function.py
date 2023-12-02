import streamlit as st
from Ghazaleh import budget_app as ghazaleh_budget_app
from Tarek import budget_app as tarek_budget_app
from Khaled import budget_app as khaled_budget_app
from Leen import budget_app as leen_budget_app
from Sondos import budget_app as sondos_budget_app
from Husam import budget_app as husam_budget_app

def main():
    st.title("My Streamlit App")

    page = st.sidebar.selectbox("Select a page", ["Ghazaleh", "Tarek", "Khaled", "Leen", "Sondos", "Husam"])

    if page == "Ghazaleh":
        ghazaleh_budget_app()
    elif page == "Tarek":
        tarek_budget_app()
    elif page == "Khaled":
        khaled_budget_app()
    elif page == "Leen":
        leen_budget_app()
    elif page == "Sondos":
        sondos_budget_app()
    elif page == "Husam":
        husam_budget_app()

if __name__ == "__main__":
    main()
