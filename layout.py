import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data as vega_data

st.set_page_config(layout="wide")

# Create charts using Altair
charts = []

# Line chart
source = vega_data.stocks()
line = alt.Chart(source).mark_line().encode(
    x='date:T',
    y='price:Q',
    color='symbol:N',
)
charts.append(('Line', line))

# Grouped bar chart
source = pd.DataFrame({
    "Category": list("AAABBBCCC"),
    "Group": list("xyzxyzxyz"),
    "Value": [0.1, 0.6, 0.9, 0.7, 0.2, 1.1, 0.6, 0.1, 0.2]
})
bar = alt.Chart(source).mark_bar().encode(
    x="Category:N",
    y="Value:Q",
    xOffset="Group:N",
    color="Group:N"
)
charts.append(('Bar', bar))

# Bar and line chart
source = vega_data.wheat()
bar = alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='wheat:Q'
)
line = alt.Chart(source).mark_line(color='red').transform_window(
    rolling_mean='mean(wheat)',
    frame=[-9, 0]
).encode(
    x='year:O',
    y='rolling_mean:Q'
)
charts.append(('Line-Bar', bar + line))

# Stacked area chart
source = vega_data.iowa_electricity()
stacked_area = alt.Chart(source).mark_area().encode(
    x="year:T",
    y="net_generation:Q",
    color="source:N"
)
charts.append(('Stacked Area', stacked_area))

# Layout Generator class
class LayoutGenerator:
    def __init__(self, layout_type):
        self.layout_type = layout_type

    def generate_layout(self):
        if self.layout_type == 1:
            return self.layout_type_1()
        elif self.layout_type == 2:
            return self.layout_type_2()
        elif self.layout_type == 3:
            return self.layout_type_3()
        elif self.layout_type == 4:
            return self.layout_type_4()
        elif self.layout_type == 5:
            return self.layout_type_5()
        elif self.layout_type == 6:
            return self.layout_type_6()
        elif self.layout_type == 7:
            return self.layout_type_7()
        elif self.layout_type == 8:
            return self.layout_type_8()
        elif self.layout_type == 9:
            return self.layout_type_9()
        else:
            st.error("Invalid layout type")
            return None

    def layout_type_1(self):
        cols = st.columns(4)
        return cols

    def layout_type_2(self):
        cols = []
        for _ in range(4):
            col = st.columns(1)[0]
            cols.append(col)
        return cols

    def layout_type_3(self):
        cols1 = st.columns(2)
        cols2 = st.columns(2)
        return cols1 + cols2

    def layout_type_4(self):
        col1 = st.columns(1)
        col2 = st.columns(3)
        return col1 + col2

    def layout_type_5(self):
        cols1 = st.columns(3)
        col2 = st.columns(1)
        return cols1 + col2
    
    def layout_type_6(self):
        cols1 = st.columns(2, vertical_alignment='center')
        subcol1 = cols1[1].columns(1)
        subcol2 = cols1[1].columns(1)
        col3 = st.columns(1)
        return [cols1[0], subcol1[0], subcol2[0], col3[0]]

    def layout_type_7(self):
        cols1 = st.columns(2, vertical_alignment='center')
        subcol1 = cols1[0].columns(1)
        subcol2 = cols1[0].columns(1)
        col3 = st.columns(1)
        return [subcol1[0], subcol2[0], cols1[1], col3[0]]
    
    def layout_type_8(self):
        col1, col2 = st.columns([3, 5])
        with col2:
            subcols = st.columns(1)
            for _ in range(2):
                subcols += st.columns(1)
        return [col1] + subcols
    
    def layout_type_9(self):
        col1, col2 = st.columns([5, 3])
        with col1:
            subcols = st.columns(1)
            for _ in range(2):
                subcols += st.columns(1)
        return subcols + [col2]
    

# Add CSS for borders
st.markdown(
    """
    <style>
    [data-testid="column"] {
        border: 2px solid #4CAF50;
        padding: 10px;
        margin: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for selected charts
if 'selected_charts' not in st.session_state:
    st.session_state['selected_charts'] = ['Line', 'Bar', 'Line-Bar', 'Stacked Area']

# Chart labels
chart_labels = [label for label, _ in charts]

# Layout selection
layout_type = st.selectbox("Select layout type", [i+1 for i in range(9)])

# Create select boxes for user to choose charts
cols = st.columns(4)
for i in range(4):
    st.session_state['selected_charts'][i] = cols[i].selectbox(
        f"Select chart for chart no. {i+1}",
        options=chart_labels,
        index=chart_labels.index(st.session_state['selected_charts'][i]),
        key=f"select_chart_{i}"
    )

layout_generator = LayoutGenerator(layout_type)
columns = layout_generator.generate_layout()


if columns:
    # Display the selected charts in the columns
    for i, col in enumerate(columns):
        with col:
            st.write(f"Chart {i+1}")
            selected_chart_label = st.session_state['selected_charts'][i]
            selected_chart = next(chart for label, chart in charts if label == selected_chart_label)
            st.altair_chart(selected_chart, use_container_width=True)

