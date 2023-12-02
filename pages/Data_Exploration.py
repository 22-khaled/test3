import streamlit as st
import pandas as pd
from sklearn import datasets
import io
# Side bar layout

@st.cache_data
def load_data(dataset_name: str):
    if dataset_name == 'Iris':
        data = datasets.load_iris()

    elif dataset_name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    # return whole datasets (all columns)
    features = pd.DataFrame(data['data'], columns=data['feature_names'])
    target = pd.Series(data['target'], name='Class')
    return pd.concat([features, target], axis=1)
        

dataset_name = st.sidebar.selectbox(label='Select dataset', 
                     options= ('Iris', 'Breast Cancer'), 
                     index=None)
#Main layout
if dataset_name == None:
    st.subheader('Please choose a dataset from the sidebar...')
else:
    st.header(f'The {dataset_name} dataset')
    #loading data based on the selection
    data = load_data(dataset_name)
    st.subheader("Properties")

    props_tabs = st.tabs(["Dimensions", "Data Types", "Desctiptive Stats"])
    
    with props_tabs[0]:#Dimentions
        props_dimensions_cols = st.columns(2, gap='large')
        with props_dimensions_cols[0]:

            st.write('Total enteries (rows):', data.shape[0])
            st.write('Total features (columns):', data.shape[1])

        with props_dimensions_cols[1]:
            data_range = st.slider(label = 'Data preview Range (up to 50)',
                                min_value=1,
                                max_value=min(data.shape[0],50),
                                value = (1, min(data.shape[0], 10)),
                                )
    
        st.dataframe(data.iloc[range(data_range[0]-1, data_range[1]),:], use_container_width=True)


    with props_tabs[1]: #State base layout:
        #renaming the series 'Series', and converting it to 'DataFrame for
        # a better UI

        st.dataframe(pd.Series(data.dtypes, name="Data Types"), 
                     use_container_width=True)
        with st.expander('Detailed info'):
            buffer = io.StringIO()
            data.info(buf=buffer)
            st.text(buffer.getvalue())

    with props_tabs[2]: #describtive
        st.dataframe(data.describe().T, use_container_width=True)

st.divider()

st.subheader('Correlation')

class_column = 'class'
feature_columns = ['mean radius', 'mean_texture']

corr_matrix = (data
                .corr(numeric_only=True)
                .loc[feature_columns, [class_column]]
                .sort_values(axis=0, by = class_column, assending=False)
                .style
                .background_gradient(cmap='twilight_shifted')
                )


st.dataframe(data = corr_matrix, use_container_width=True)


if dataset_name == 'Iris':
    pass
elif dataset_name == 'Breast Cancer':
    pass