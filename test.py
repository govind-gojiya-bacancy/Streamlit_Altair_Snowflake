import streamlit as st
import altair as alt
import pandas as pd

st. set_page_config(layout="wide")

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y1': range(10),
    'y2': [x**2 for x in range(10)],
    'y3': [x**0.5 for x in range(10)],
    'y4': [10 - x for x in range(10)]
})

# Create charts using Altair
chart1 = alt.Chart(data).mark_line().encode(
    x='x',
    y='y1'
).properties(
    title='Chart 1'
)

chart2 = alt.Chart(data).mark_line().encode(
    x='x',
    y='y2'
).properties(
    title='Chart 2'
)

chart3 = alt.Chart(data).mark_line().encode(
    x='x',
    y='y3'
).properties(
    title='Chart 3'
)

chart4 = alt.Chart(data).mark_line().encode(
    x='x',
    y='y4'
).properties(
    title='Chart 4'
)

# CSS to add border around containers
st.markdown("""
    <style>
    [data-testid="column"]:has(div.container-box) {
        border: 2px solid #4CAF51;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(255, 255, 255, 0.1), 
              0 10px 20px rgba(0.2, 0.2, 0.2, 0.5);
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Create columns and add charts with styled boxes

sec1, sec2 = st.columns(2, vertical_alignment="center")

with sec1:
    with st.container(border=True):
        st.write("""<div class="container-box">""", unsafe_allow_html=True)
        st.altair_chart(chart1, use_container_width=True)
    with st.container(border=True):
        st.write("""<div class="container-box">""", unsafe_allow_html=True)
        st.altair_chart(chart2, use_container_width=True)

with sec2:
    with st.container(border=True):
        st.write("""<div class="container-box">""", unsafe_allow_html=True)
        st.altair_chart(chart3, use_container_width=True)
    with st.container(border=True):
        st.write("""<div class="container-box">""", unsafe_allow_html=True)
        st.altair_chart(chart4, use_container_width=True)