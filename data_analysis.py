import streamlit as st
import pandas as pd
import duckdb

st.title("Interactive Data Analysis")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.sidebar.title("Data Analysis Options")
    columns = st.sidebar.multiselect("Select columns to display", data.columns.tolist(), default=data.columns.tolist())
    st.write("Selected Columns")
    st.write(data[columns])

    query = st.sidebar.text_area("Write a query (remember that the name of the table is 'data')")
    if st.sidebar.button("Run Query"):
        result = duckdb.query(query).df()
        st.write("Query Result")
        st.write(result)

    if st.sidebar.button("Generate Summary"):
        st.write(data[columns].describe())