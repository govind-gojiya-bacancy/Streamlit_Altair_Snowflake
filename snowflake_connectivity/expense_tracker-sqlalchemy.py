import streamlit as st
import pandas as pd
import altair as alt
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

# Load secrets
sqlalchemy_secrets = st.secrets["expense_tracker"]

# Snowflake connection configuration
DATABASE_URL = f"snowflake://{sqlalchemy_secrets['user']}:{sqlalchemy_secrets['password']}@{sqlalchemy_secrets['account']}/{sqlalchemy_secrets['database']}/{sqlalchemy_secrets['schema']}?warehouse={sqlalchemy_secrets['warehouse']}"

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define ORM model for the EXPENSES table
class Expense(Base):
    __tablename__ = 'EXPENSES'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ITEM_NAME = Column(String)
    CATEGORY = Column(String)
    AMOUNT = Column(Float)
    PAYMENT_MODE = Column(String)
    PURCHASE_DATE = Column(Date)
    DESCRIPTION = Column(String)

# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# CRUD operations with SQLAlchemy ORM
def create_expense(session, item_name, category, amount, payment_mode, purchase_date, description):
    # expense = Expense(
    #     ITEM_NAME=item_name,
    #     CATEGORY=category,
    #     AMOUNT=amount,
    #     PAYMENT_MODE=payment_mode,
    #     PURCHASE_DATE=purchase_date,
    #     DESCRIPTION=description
    # )
    # session.add(expense)
    # session.commit()
    query = text("""
    INSERT INTO EXPENSES (ITEM_NAME, CATEGORY, AMOUNT, PAYMENT_MODE, PURCHASE_DATE, DESCRIPTION)
    VALUES (:item_name, :category, :amount, :payment_mode, :purchase_date, :description)
    """)
    session.execute(query, {
        'item_name': item_name,
        'category': category,
        'amount': amount,
        'payment_mode': payment_mode,
        'purchase_date': purchase_date,
        'description': description
    })
    session.commit()

def read_expenses(session):
    return pd.read_sql(session.query(Expense).statement, session.bind)

def update_expense(session, expense_id, item_name, category, amount, payment_mode, purchase_date, description):
    expense = session.query(Expense).filter_by(ID=expense_id).one()
    expense.ITEM_NAME = item_name
    expense.CATEGORY = category
    expense.AMOUNT = amount
    expense.PAYMENT_MODE = payment_mode
    expense.PURCHASE_DATE = purchase_date
    expense.DESCRIPTION = description
    session.commit()

def delete_expense(session, expense_id):
    expense = session.query(Expense).filter_by(ID=expense_id).one()
    session.delete(expense)
    session.commit()

# Streamlit UI
st.title('Expense Tracker using SQLAlchemy')

# Create a new SQLAlchemy session
session = Session()

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
chart = alt.Chart(expenses_over_time).mark_line().encode(
    x='PURCHASE_DATE:T',
    y='AMOUNT:Q'
).properties(
    title='Total Expenses Over Time'
)
st.altair_chart(chart, use_container_width=True)

# Expenses by category
expenses_by_category = expenses_df.groupby('CATEGORY')['AMOUNT'].sum().reset_index()
chart = alt.Chart(expenses_by_category).mark_bar().encode(
    x='CATEGORY:N',
    y='AMOUNT:Q'
).properties(
    title='Expenses by Category'
)
st.altair_chart(chart, use_container_width=True)

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

st.altair_chart(combined_chart, use_container_width=True)

# Stacked Area Chart: Amount Spent by Category Over Time
stacked_area_chart = alt.Chart(expenses_df).mark_area().encode(
    x='PURCHASE_DATE:T',
    y='sum(AMOUNT):Q',
    color='CATEGORY:N'
).interactive()

st.altair_chart(stacked_area_chart, use_container_width=True)
