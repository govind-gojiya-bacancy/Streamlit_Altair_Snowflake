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
        65000000, 60000000, 70000000,
        80000000, 80000000, 100000000,
        110000000, 190000000, 90000000, 
        140000000, 190000000
    ],
}

# Manually calculate growth (this is an example, please adjust based on your calculation)
data['growth'] = [None] + [(data['revenue'][i] - data['revenue'][i-1]) / data['revenue'][i-1] * 100 for i in range(1, len(data['revenue']))]

df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df["month"] = df['date'].dt.strftime('%b')  

# Get the height of the 2nd bin (2nd month's revenue)
second_bin_height = df['revenue'].iloc[1]
min_revenue = min(df["revenue"])
max_revenue = max(df["revenue"]) + min_revenue
# max_revenue = max(df["revenue"])
max_line_scale = ((max_revenue * 100) / second_bin_height) - 100
print(max_revenue)
print(-100 + df['growth'].iloc[1], max_line_scale + df['growth'].iloc[1])

st.markdown('<style>#vg-tooltip-element{z-index: 1000051}</style>',
             unsafe_allow_html=True)

base = alt.Chart(df).encode(
    x=alt.X('month:N', title='Month', axis=alt.Axis(labelAngle=0), sort=None),
)

# Bar chart for revenue
bar_chart = base.mark_bar().encode(
    y=alt.Y('revenue:Q', title='Monthly Revenue', sort=None, scale=alt.Scale(domain=[0, max_revenue], nice=False)),
    tooltip=[alt.Tooltip('month:N', title='Month'), alt.Tooltip('revenue:Q', title='Revenue')],
)

# Line chart for growth rate with adjusted y-axis
line_chart = base.mark_line(point=alt.OverlayMarkDef(filled=False, fill="white"), color='red').encode(
    y=alt.Y('growth:Q', title='Growth Rate (%)', sort=None, scale=alt.Scale(domain=[-100 + df['growth'].iloc[1], max_line_scale + df['growth'].iloc[1]], nice=False)),
).interactive()

# Helper line at first point
helper = base.mark_line(color="green").encode(
    y=alt.datum(second_bin_height)
)

bar_chart = alt.layer(bar_chart, helper)

# Combine both charts
chart = alt.layer(bar_chart, line_chart).resolve_scale(
    x='shared',
    y='independent'
).interactive()

st.altair_chart(chart, use_container_width=True)