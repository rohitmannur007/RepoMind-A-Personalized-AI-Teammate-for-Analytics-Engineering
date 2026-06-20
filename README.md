
<p align="center">
  <img src="docs/banner.png" alt="RepoMind Banner" width="100%" />
</p>

<h1 align="center">RepoMind</h1>
<p align="center">
  <b>Personalized AI Teammate for Analytics Engineering</b><br/>
  Repo-aware · dbt-native · Validation-driven · Research-ready
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue.svg" />
  <img src="https://img.shields.io/badge/dbt-DuckDB-orange.svg" />
  <img src="https://img.shields.io/badge/Hugging%20Face-LLM%20Ready-yellow.svg" />
  <img src="https://img.shields.io/badge/Streamlit-Demo%20App-ff4b4b.svg" />
  <img src="https://img.shields.io/badge/Research-Prototype-success.svg" />
</p>

<p align="center">
  <img src="docs/demo.gif" alt="RepoMind demo" width="100%" />
</p>

---

## What is RepoMind?

RepoMind is a **personalized AI teammate for analytics engineers**.

It reads a dbt repository, learns its style, retrieves the most relevant files, drafts SQL or tests, validates the result with dbt, and explains the impact of changes across the project.

Instead of acting like a generic chatbot, RepoMind behaves like a teammate that understands:
- how your repo is structured
- how your team names models
- what tests already exist
- which files will break if something changes
- how to generate changes that actually fit the project

---

## Why I built it

Modern data teams spend a lot of time on repetitive but critical work:
- understanding dbt projects
- tracing lineage
- writing tests
- fixing SQL errors
- onboarding new engineers
- checking whether a change will break downstream models

RepoMind is built to reduce that friction.

It turns a fuzzy request like:

> “Create a revenue mart from the enriched orders model”

into a structured workflow:
1. understand the repo
2. retrieve relevant context
3. draft a patch
4. validate with dbt
5. review the result
6. explain the impact

---

## What RepoMind does

RepoMind currently supports:

- repository parsing for dbt projects
- repo-style profiling
- file retrieval using semantic similarity
- task planning
- SQL / model / test drafting
- dbt validation through compile and test
- Streamlit UI for interactive demos
- benchmark task loading for evaluation

---

## Key capabilities

### 1) Repo understanding
RepoMind scans:
- `models/`
- `schema.yml`
- `seeds/`
- `macros/`
- project files

and builds a lightweight understanding of:
- model names
- refs
- tests
- SQL patterns
- repo structure

### 2) Context retrieval
Given a task, RepoMind finds the most relevant files and surfaces them first.

### 3) Draft generation
RepoMind produces a first-pass answer or SQL draft that follows the repo’s style.

### 4) Validation
RepoMind uses dbt compile/test to check whether the draft is actually usable.

### 5) Review layer
RepoMind flags obvious problems and explains whether the draft needs work.

---

## Why this is different from a normal chatbot

Most AI demos stop at generation.

RepoMind goes further:
- it reads the repository
- it retrieves context
- it drafts changes
- it validates the changes
- it tracks the outcome

That makes it much closer to a real teammate than a generic assistant.

---

## System architecture

```text
User
  ↓
Streamlit UI
  ↓
Task Orchestrator
  ↓
Repo Parser + Style Profiler
  ↓
Retriever
  ↓
Planner
  ↓
Draft Generator
  ↓
dbt Validation
  ↓
Reviewer
  ↓
Final Output
````

---

## Tech stack

* **Python**
* **dbt**
* **DuckDB**
* **Streamlit**
* **Pandas**
* **scikit-learn**
* **PyTorch** for the next version
* **Hugging Face** for the next version
* **FastAPI** if you want to expose the agent as an API later

---

## Project structure

```bash
RepoMind/
├── app/
│   ├── agent/
│   ├── retrieval/
│   ├── validation/
│   └── schemas/
├── dbt_project/
│   ├── models/
│   ├── seeds/
│   ├── profiles/
│   └── schema.yml
├── data/
│   ├── raw/
│   ├── processed/
│   └── benchmarks/
├── scripts/
├── tests/
├── streamlit_app.py
└── README.md
```

---

## Demo flow

Example task:

> Create a monthly revenue mart from the enriched orders model.

RepoMind will:

* read the repo
* retrieve relevant models
* draft SQL
* run validation
* return a review
* show the style profile

---

## Why this matters

This project is built for the kind of work modern data teams actually do.

Business impact:

* faster onboarding
* faster debugging
* fewer broken transformations
* better test coverage
* less manual SQL hunting
* more consistent dbt development

For large data teams, even a small reduction in debugging and onboarding time creates real savings.

---

## Research angle

RepoMind is not just a utility project.

It is also a research prototype for:

* repo-aware retrieval
* personalized AI assistants
* tool-augmented generation
* validation-driven LLM workflows
* evaluation of analytics-engineering tasks

That makes it relevant for internships and research roles focused on:

* LLMs
* agents
* RAG
* modern data stack workflows
* analytics engineering

---

## Current status

* [x] dbt project scaffold
* [x] repository parser
* [x] style profiler
* [x] retriever
* [x] planning layer
* [x] draft generator
* [x] dbt validation hooks
* [x] Streamlit UI
* [ ] Hugging Face model integration
* [ ] PyTorch experimentation
* [ ] benchmark suite
* [ ] evaluation dashboard
* [ ] stronger agent loop

---

## How to run

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the dbt setup

```bash
python -m scripts.setup_db
```

### 4. Start the demo

```bash
streamlit run streamlit_app.py
```

---

## Results to add later

Once the Hugging Face and evaluation layer is added, this README should include:

* pass rate on benchmark tasks
* compile success rate
* test success rate
* latency
* before/after comparison with and without personalization

---

## Future work

* replace TF-IDF with embeddings
* add local Hugging Face model support
* add agent planning and repair loops
* add benchmark dataset generation
* add pass@1 / pass@k evaluation
* add repo-specific fine-tuning with LoRA
* add GitHub issue / PR style workflow
* add lineage-aware impact prediction

---

## Best use case

RepoMind is especially useful for:

* dbt projects
* analytics engineering teams
* SQL-heavy workflows
* AI teammate research
* LLM + RAG + agent demos
* internship applications in AI/data engineering

---

## License

MIT

```

To make it look even cooler, add these three files in `docs/`:
- `banner.png`
- `demo.gif`
- `architecture.png`

That will make the README feel like a real product page instead of plain text.
```
