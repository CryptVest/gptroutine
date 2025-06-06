import streamlit as st
import json
import os

# Get query parameter
params = st.experimental_get_query_params()
date_str = params.get("date", [None])[0]

if not date_str:
    st.warning("No date selected. Please open a page from the calendar.")
    st.stop()

# Load page data
os.makedirs("data", exist_ok=True)
data_path = "data/pages.json"
if os.path.exists(data_path):
    with open(data_path, "r") as f:
        pages = json.load(f)
else:
    pages = {}

# Load or create new
page_data = pages.get(date_str, {"title": "", "content": ""})

st.title(f"📄 Page for {date_str}")
title = st.text_input("Title", value=page_data["title"])
content = st.text_area("Content", value=page_data["content"], height=300)

if st.button("Save"):
    pages[date_str] = {"title": title, "content": content}
    with open(data_path, "w") as f:
        json.dump(pages, f, indent=2)
    st.success("Page saved!")
