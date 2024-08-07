import streamlit as st
import pandas as pd
import altair as alt
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, max, when, lag
from snowflake.snowpark.window import Window

st.set_page_config(layout="wide")

# Load secrets
snowpark_secrets = st.secrets["expense_tracker"]

# Snowpark connection
def get_snowpark_session():
    connection_parameters = {
        "user": snowpark_secrets["user"],
        "password": snowpark_secrets["password"],
        "account": snowpark_secrets["account"],
        "warehouse": snowpark_secrets["warehouse"],
        "database": snowpark_secrets["database"],
        "schema": snowpark_secrets["schema"],
        "role": snowpark_secrets["role"]
    }
    return Session.builder.configs(connection_parameters).create()

# CRUD operations with Snowpark
def create_expense(session, item_name, category, amount, payment_mode, purchase_date, description):
    query = f"""
    INSERT INTO EXPENSES (ITEM_NAME, CATEGORY, AMOUNT, PAYMENT_MODE, PURCHASE_DATE, DESCRIPTION)
    VALUES ('{item_name}', '{category}', {amount}, '{payment_mode}', '{purchase_date}', '{description}')
    """
    session.sql(query).collect()

def read_expenses(session):
    df = session.table("EXPENSES")
    return df.to_pandas()

def update_expense(session, expense_id, item_name, category, amount, payment_mode, purchase_date, description):
    session.table("EXPENSES") \
        .update(
            {"ITEM_NAME": item_name, "CATEGORY": category, "AMOUNT": amount, "PAYMENT_MODE": payment_mode, "PURCHASE_DATE": purchase_date, "DESCRIPTION": description},
            col("ID") == expense_id
        )

def delete_expense(session, expense_id):
    session.table("EXPENSES").delete(col("ID") == expense_id)

# Streamlit UI
st.title('Expense Tracker')

session = get_snowpark_session()

# Form to add or update expense
with st.form(key='expense_form'):
    item_name = st.text_input('Item Name')
    category = st.selectbox('Category', ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other'])
    amount = st.number_input('Amount', min_value=0.0, format='%f')
    payment_mode = st.selectbox('Payment Mode', ['Cash', 'Card', 'Online'])
    purchase_date = st.date_input('Purchase Date')
    description = st.text_area('Description')
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    create_expense(session, item_name, category, amount, payment_mode, purchase_date, description)
    st.success('Expense added successfully!')

# Display expenses
expenses_df = read_expenses(session)
st.write('### Expenses')
st.dataframe(expenses_df)

# Update and Delete options
if not expenses_df.empty:
    expense_id = st.selectbox('Select Expense to Update/Delete', expenses_df['ID'])
    selected_expense = expenses_df[expenses_df['ID'] == expense_id].iloc[0]

    with st.form(key='update_delete_form'):
        item_name = st.text_input('Item Name', value=selected_expense['ITEM_NAME'])
        category = st.selectbox('Category', ['Food', 'Transport', 'Entertainment', 'Utilities', 'Other'], index=['Food', 'Transport', 'Entertainment', 'Utilities', 'Other'].index(selected_expense['CATEGORY']))
        amount = st.number_input('Amount', min_value=0.0, format='%f', value=selected_expense['AMOUNT'])
        payment_mode = st.selectbox('Payment Mode', ['Cash', 'Card', 'Online'], index=['Cash', 'Card', 'Online'].index(selected_expense['PAYMENT_MODE']))
        purchase_date = st.date_input('Purchase Date', value=pd.to_datetime(selected_expense['PURCHASE_DATE']))
        description = st.text_area('Description', value=selected_expense['DESCRIPTION'])
        update_button = st.form_submit_button(label='Update')
        delete_button = st.form_submit_button(label='Delete')

    if update_button:
        update_expense(session, expense_id, item_name, category, amount, payment_mode, purchase_date, description)
        st.success('Expense updated successfully!')

    if delete_button:
        delete_expense(session, expense_id)
        st.success('Expense deleted successfully!')

# Visualize expenses
st.write('### Expense Analysis')
expenses_df['PURCHASE_DATE'] = pd.to_datetime(expenses_df['PURCHASE_DATE'])

# Total expenses over time
expenses_over_time = expenses_df.groupby('PURCHASE_DATE')['AMOUNT'].sum().reset_index()
line_chart = alt.Chart(expenses_over_time).mark_line().encode(
    x='PURCHASE_DATE:T',
    y='AMOUNT:Q'
).properties(
    title='Total Expenses Over Time'
)

# Expenses by category
expenses_by_category = expenses_df.groupby('CATEGORY')['AMOUNT'].sum().reset_index()
bar_chart = alt.Chart(expenses_by_category).mark_bar().encode(
    x='CATEGORY:N',
    y='AMOUNT:Q'
).properties(
    title='Expenses by Category'
)

# Ensure dates are in the correct format
expenses_df['PURCHASE_DATE'] = pd.to_datetime(expenses_df['PURCHASE_DATE'])

# Simplified Line-Bar Chart: Amount Spent Over Time
base = alt.Chart(expenses_df).encode(
    x='PURCHASE_DATE:T'
)

bar = base.mark_bar(opacity=0.5).encode(
    y='AMOUNT:Q',
    color='CATEGORY:N'
)

line = base.mark_line(color='red', size=2).encode(
    y='AMOUNT:Q'
)

combined_chart = alt.layer(bar, line).resolve_scale(
    y='independent'
).interactive().properties(
    width=800,
    height=400
)

# Stacked Area Chart: Amount Spent by Category Over Time
stacked_area_chart = alt.Chart(expenses_df).mark_area().encode(
    x='PURCHASE_DATE:T',
    y='sum(AMOUNT):Q',
    color='CATEGORY:N'
).interactive()


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
        # border: 2px solid #4CAF50;
        box-shadow: inset 0 0 0.5px 1px hsla(0, 0%,  
              100%, 0.075),
              /* shadow ring 👇 */
              0 0 0 1px hsla(0, 0%, 0%, 0.05),
              /* multiple soft shadows 👇 */
              0 0.3px 0.4px hsla(0, 0%, 0%, 0.02),
              0 0.9px 1.5px hsla(0, 0%, 0%, 0.045),
              0 3.5px 6px hsla(0, 0%, 0%, 0.09);
        padding: 10px;
        margin: 0px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for selected charts
if 'selected_charts' not in st.session_state:
    st.session_state['selected_charts'] = ['Total Expenses Over Time', 'Expenses by Category', 'Amount Spent Over Time', 'Amount Spent by Category Over Time']

# Chart labels
chart_labels = ['Total Expenses Over Time', 'Expenses by Category', 'Amount Spent Over Time', 'Amount Spent by Category Over Time']
charts = [line_chart, bar_chart, combined_chart, stacked_area_chart]

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
            selected_chart = charts[chart_labels.index(selected_chart_label)]
            st.altair_chart(selected_chart, use_container_width=True)
