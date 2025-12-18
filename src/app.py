import streamlit as st
from io import StringIO
import csv
import json

from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown



st.set_page_config(page_title="CSV Profiler",layout="wide")
st.title("CSV Profiler")
st.caption("Week 01 • Day 04 — Streamlit GUI")
st.sidebar.header("inputs")


uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:

    text=uploaded_file.getvalue().decode("utf-8-sig")
    file_like=StringIO(text)
    reader=csv.DictReader(file_like)
    rows=list(reader)



    st.write("Filename:", uploaded_file.name)
    st.write("size (byets)",uploaded_file.size,"bytes")

    if not rows:
        st.error("file empty")
        st.stop()

    if st.checkbox("show preview"):
        st.write(rows[:5])

  
    if st.button("Generate report"):
        report=profile_rows(rows)
        st.session_state["report"]=report


    if "report" in st.session_state:
        report=st.session_state["report"]




        cols = st.columns(2)
        cols[0].metric("rows",report['n_rows'])
        cols[1].metric("Columns",report['n_cols'] )

        with st.expander("raw json debug"):
            st.json(report)


        st.markdown(render_markdown(report))
        
        json_text=json.dumps(report)
        md_text=render_markdown(report)
        st.download_button("get json", data=json_text,file_name='report.json')
        st.download_button("get markdown", data=md_text,file_name='report.md')