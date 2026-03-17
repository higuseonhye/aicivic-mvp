"""Streamlit frontend - run and monitor AI company."""
import streamlit as st
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

st.set_page_config(page_title="AI Civic MVP", page_icon="🏢", layout="wide")

st.title("🏢 AI Company Demo")

mode = st.radio("Mode", ["Single company", "Market (multiple)"], horizontal=True)

if mode == "Single company":
    company_name = st.text_input("Company name", value="AI SaaS Builder")
    names = None
else:
    names_input = st.text_input(
        "Company names (comma-separated)",
        value="AI SaaS Builder, AI Analytics Co, AI Security Inc"
    )
    names = [n.strip() for n in names_input.split(",") if n.strip()]

if st.button("Run"):
    with st.spinner("Running..."):
        if mode == "Single company":
            args = [sys.executable, "main.py", company_name]
            proc = subprocess.run(args, capture_output=True, text=True, cwd=PROJECT_ROOT)
        else:
            args = [sys.executable, "main.py", "--market"] + (names or [])
            proc = subprocess.run(args, capture_output=True, text=True, cwd=PROJECT_ROOT)

        out = proc.stdout + proc.stderr
        st.code(out, language="text")
        if proc.returncode != 0:
            st.error("Run failed")

st.divider()
st.caption("Cost tracking and tool output (Notion/Slack) appear in the run log when configured.")
