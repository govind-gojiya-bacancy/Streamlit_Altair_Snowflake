import pandas as pd
import altair as alt
import streamlit as st

# Sample data
data = {
    'date': [
        '2023-01-01', '2023-02-01', '2023-03-01',
        '2023-04-01', '2023-05-01', '2023-06-01',
        '2023-07-01', '2023-08-01', '2023-09-01', 
        '2023-10-01', '2023-11-01', 
    ],
    'metric_value': [
        50000, 60000, 70000,
        80000, 90000, 100000,
        110000, 120000, 80000, 
        140000, 150000
    ],
    'growth': [
        12, 14, 15,
        16, 17, 20,
        25, 27, 30,
        28, 29
    ]
}

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df["quarter"] = df['date'].dt.to_period('Q').astype(str)  # Convert to string for proper labeling
df["month"] = df['date'].dt.strftime('%b')  # Month abbreviation

st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>',
             unsafe_allow_html=True)

bar_chart = alt.Chart(df).transform_joinaggregate(
        count_gross='sum(metric_value)',
        groupby=['quarter']
    ).transform_calculate(
        order="{'Jan':0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5, 'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}[datum.month]"  
    ).mark_bar().encode(
    x=alt.X('quarter:N', title='Quarter', axis=alt.Axis(labelAngle=0), sort=None),
    y=alt.Y('metric_value:Q', title='Quarter Gross metric'),
    # color=alt.Color('month:N', legend=None, scale=alt.Scale(scheme='category20'), sort=alt.SortField("order", "ascending")),
    tooltip=[alt.Tooltip('quarter:N', title='Quarter'), alt.Tooltip('month:N', title='Month'), alt.Tooltip('metric_value:Q', title='Monthly Metric'), alt.Tooltip('count_gross:Q', title='Total Quarter Metric')],
    order="order:O"
)

line_chart = alt.Chart(df).mark_line(point=True, color='red').encode(
    x=alt.X('month:N', title='Month', sort=None, axis=None),
    y=alt.Y('growth:Q', title='Growth Rate (%)', scale=alt.Scale(domain=[-100, 100])),
)

chart = alt.layer(bar_chart, line_chart).resolve_scale(
    x='independent',
    y='independent'
)

st.altair_chart(chart, use_container_width=True)

import altair as alt
import pandas as pd
import streamlit as st

# Sample data
data = {
    'date': [
        '2023-01-01', '2023-02-01', '2023-03-01',
        '2023-04-01', '2023-05-01', '2023-06-01',
        '2023-07-01', '2023-08-01', '2023-09-01', 
        '2023-10-01', '2023-11-01',
    ],
    'revenue': [
        60000000, 80000000, 70000000,
        80000000, 90000000, 100000000,
        110000000, 180000000, 90000000, 
        140000000, 10000000
    ],
}

# Manually calculate growth (this is an example, please adjust based on your calculation)
data['growth'] = [None] + [(data['revenue'][i] - data['revenue'][i-1]) / data['revenue'][i-1] * 100 for i in range(1, len(data['revenue']))]

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df["month"] = df['date'].dt.strftime('%b')  # Month abbreviation

# Get the height of the 2nd bin (2nd month's revenue)
second_bin_height = df['revenue'].iloc[1]
max_revenue = max(df["revenue"])
max_value = (max_revenue * 100 / second_bin_height) - 100

# # Calculate the range for the growth y-axis to align 0 with the 2nd bin's height
# growth_max = 100  # Maximum of the growth scale
# growth_min = -100 # Minimum of the growth scale

# # Adjust the domain such that 0 on the growth scale aligns with the 2nd bin height
# growth_offset = second_bin_height / max(df['revenue']) * (growth_max - growth_min)
# adjusted_growth_min = -growth_offset
# adjusted_growth_max = growth_max - growth_offset


# # Calculate the offset needed to align 0% with the 2nd bin's height
# max_growth = max(df['growth'][1:], key=abs)  # Assuming the largest growth magnitude determines the line domain
# min_growth = -max_growth  # Symmetric domain for simplicity
# growth_domain = [min_growth, max_growth]
# growth_midpoint = 0  # This should align with the second_bin_height

# # Calculate the scaling factor and the offset
# scaling_factor = (max(df['revenue']) - 0) / (max_growth - min_growth)
# offset = second_bin_height - (growth_midpoint * scaling_factor)


# # Calculate the necessary shift for the line chart
# growth_domain = [-100, 100]
# growth_midpoint = 0  # This should align with the second_bin_height

# # Calculate the required scale factor to align 0% with the second bin's height
# revenue_scale_factor = (max(df['revenue']) - 0) / (growth_domain[1] - growth_domain[0])
# y_shift = second_bin_height / revenue_scale_factor


st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>',
             unsafe_allow_html=True)

base = alt.Chart(df).encode(
    x=alt.X('month:N', title='Month', axis=alt.Axis(labelAngle=0), sort=None),
)

# Bar chart for revenue
bar_chart = base.mark_bar().encode(
    y=alt.Y('revenue:Q', title='Monthly Revenue', sort=None, scale=alt.Scale(domain=[0, max_revenue])),
    tooltip=[alt.Tooltip('month:N', title='Month'), alt.Tooltip('revenue:Q', title='Revenue')],
)

# breakpoint()

# Line chart for growth rate with adjusted y-axis
line_chart = base.mark_line(point=alt.OverlayMarkDef(filled=False, fill="white"), color='red').encode(
    y=alt.Y('growth:Q', title='Growth Rate (%)', sort=None, scale=alt.Scale(domain=[-100, max_value])),
)

# Combine both charts
chart = alt.layer(bar_chart, line_chart).resolve_scale(
    x='shared',
    y='independent'
)

st.altair_chart(chart, use_container_width=True)
