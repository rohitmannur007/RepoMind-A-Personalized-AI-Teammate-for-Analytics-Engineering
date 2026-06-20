from __future__ import annotations

import json

import streamlit as st

from app.agent.orchestrator import run_task


st.set_page_config(page_title="dbt AI Teammate", layout="wide")
st.title("dbt AI Teammate")

st.write("This demo reads a dbt project, retrieves relevant context, drafts an answer, and runs dbt validation.")

with st.sidebar:
    repo_root = st.text_input("Repo folder", value="dbt_project")
    top_k = st.slider("Top K context files", 1, 10, 5)

task = st.text_area(
    "Task",
    value="Create a monthly revenue mart from the enriched orders model.",
    height=120,
)

run_button = st.button("Run task")

if run_button:
    with st.spinner("Running agent..."):
        result = run_task(task=task, repo_root=repo_root, top_k=top_k)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Plan")
        for step in result["plan"]:
            st.write(f"- {step}")

        st.subheader("Retrieved Context")
        for item in result["context"]:
            st.write(f"**{item['path']}**  \nscore: {item['score']:.3f}")
            st.code(item["snippet"])

    with col2:
        st.subheader("Draft")
        st.code(result["draft"])

        st.subheader("Validation")
        st.json(result["validation"])

        st.subheader("Review")
        st.json(result["review"])

    st.subheader("Style Profile")
    st.json(result["style_profile"])

    st.subheader("Raw JSON")
    st.code(json.dumps(result, indent=2))