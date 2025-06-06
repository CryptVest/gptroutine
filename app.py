import streamlit as st
from calendar import monthrange
from datetime import datetime
import calendar
import os
import json

# Load existing pages
DATA_FILE = 'data/pages.json'
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        pages = json.load(f)
else:
    pages = {}

st.set_page_config(page_title="Daily Routine Calendar", layout="wide")

st.title("📅 Daily Routine Calendar - 2025")

months = list(calendar.month_name)[1:]  # January to December
selected_month = st.selectbox("Select Month", months)

month_index = months.index(selected_month) + 1
year = 2025
num_days = monthrange(year, month_index)[1]

# Generate calendar
days = [datetime(year, month_index, day) for day in range(1, num_days + 1)]

# Display calendar in a table
cols = st.columns(7)
weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for col, day_name in zip(cols, weekdays):
    col.markdown(f"**{day_name}**")

row = 0
cols = st.columns(7)
for day in days:
    weekday = day.weekday()  # Monday is 0
    if day.day == 1:
        for i in range(weekday):
            cols[i].markdown("")

    date_str = day.strftime("%Y-%m-%d")
    if date_str in pages:
        # Page exists
        cols[weekday].markdown(f"[{day.day}](pages/page_viewer.py?date={date_str})")
    else:
        # No page exists
        cols[weekday].markdown(f"{day.day} [+]")

    if weekday == 6:
        cols = st.columns(7)
