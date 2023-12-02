import streamlit as st 


st.title("Classification: A Biological Assortment")

st.write("This application aims to showcase the effects of a variety of classification models on 2 biological datasets, namely:")
st.markdown("""
            - Iris Dataset :seedling:
            - Breast Cancer Dataset :dna:
            """)

st.divider()

st.header("Goal")
st.write("Finding the most suitable classification algorithm for each of the chosen datasets.")
st.write("Determining the most-fit machine learning algorithm for the dataset at hand is a major factor in deciding on which model to deploy to the real world.")

st.header("How-to")
st.markdown("""
            1. Use the **Data Exploration** page to explore the datasets and analyze their features.
                - Select the *dataset* from the sidebar.
                - Select/navigate to the *analysis step/operation*.
            """)

st.markdown("""
            2. Use the **Modeling** page to try out different machine learning algorithms on the datasets.
                - Select the *dataset* from the sidebar.
                - Select the *ML algorithm* to try from the sidebar.
            """)

st.markdown("""3. Use the **Conclusion** page to document your findings.""")

st.write(":point_left: Navigate using the sidebar on the left side of the web application.")
