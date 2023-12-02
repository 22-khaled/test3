import streamlit as st
import pages
from pages.Ghazaleh import budget_app
from pages.Tarek import budget_app1
from pages.Khaled import budget_app2
from pages.Leen import budget_app3
from pages.Sondos import budget_app4
from pages.Husam import budget_app5

def main():
    st.title("My Streamlit App")

    page = st.sidebar.selectbox("Select a page", ["Ghazaleh", "Tarek", "Khaled", "Leen", "Sondos", "Husam"])

    if page == "Ghazaleh":
        budget_app()
    elif page == "Tarek":
        budget_app1()
    elif page == "Khaled":
        budget_app2()
    elif page == "Leen":
        budget_app3()
    elif page == "Sondos":
        budget_app4()
    elif page == "Husam":
        budget_app5()


if __name__ == "__main__":
    main()
