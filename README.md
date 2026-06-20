# dbt AI Teammate

A small personalized AI teammate for dbt projects.

## What it does
- Reads a dbt repo
- Learns repo style
- Retrieves relevant files for a task
- Drafts SQL / tests / fixes
- Runs dbt compile and dbt test
- Shows results in a Streamlit demo

## How to run
1. Create and activate a Python virtual environment
2. Install dependencies
3. Set your `.env`
4. Seed and compile the dbt project
5. Run Streamlit

## Main entrypoint
```bash
streamlit run streamlit_app.py