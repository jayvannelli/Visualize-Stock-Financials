import streamlit as st
import matplotlib.pyplot as plt

def plot_statements(df, included_data):
    df.plot(x='date', y=included_data, kind='bar').invert_xaxis()
    st.pyplot(plt)