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

bar_chart = alt.Chart(df).transform_joinaggregate(
        count_gross='sum(metric_value)',
        groupby=['quarter']
    ).mark_bar().encode(
    x=alt.X('quarter:N', title='Quarter', sort=None, axis=alt.Axis(labelAngle=0)),
    y=alt.Y('metric_value:Q', title='Quarter Gross metric'),
    color=alt.Color('month:N', legend=None),
    tooltip=[alt.Tooltip('quarter:N', title='Quarter'), alt.Tooltip('month:N', title='Month'), alt.Tooltip('metric_value:Q', title='Monthly Metric'), alt.Tooltip('count_gross:Q', title='Total Quarter Metric')]
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