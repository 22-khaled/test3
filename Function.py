import streamlit as st
from Ghazaleh import budget_app
from Tarek import budget_app
from Khaled import budget_app
from Leen import budget_app
from Sondos import budget_app
from Husam import budget_app

def main():
    st.title("My Streamlit App")

    page = st.sidebar.selectbox("Select a page", ["Ghazaleh", "Tarek", "Khaled", "Leen", "Sondos", "Husam"])

    if page == "Ghazaleh":
        budget_app()
    elif page == "Tarek":
        budget_app()
    elif page == "Khaled":
        budget_app()
    elif page == "Leen":
        budget_app()
    elif page == "Sondos":
        budget_app()
    elif page == "Husam":
        budget_app()

if __name__ == "__main__":
    main()