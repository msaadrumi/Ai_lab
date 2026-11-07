# Lab 6 - NLP Fundamentals: Tokenization, Embeddings & Text Chunking

## Required files
`task1_tokens.py`, `task2_chunks.py`, `task3_retrieval.py`, `corpus.json`, `queries.json`,
`requirements.txt`, `README.md`, `retrieval_log.csv`, `lab6_search.py`,
five scenario scripts, `guided_examples.py`, `document_chatbot.py`, `Untitled22.ipynb`,
and `Lab6_Report.docx`.

## Setup
```bash
pip install -r requirements.txt
```

## Task 1
```bash
python task1_tokens.py
python guided_examples.py
python scenario_1_exact_faq.py
python scenario_2_paraphrase.py
python scenario_4_empty_query.py
python scenario_5_unsupported.py
```

## Task 2
```bash
python task2_chunks.py
python scenario_3_document_evidence.py
```

## Task 3
```bash
python task3_retrieval.py
```

The retrieval code reproduces the notebook experiment when `sentence-transformers`
is installed and the model is available. The supplied notebook recorded the completed
embedding run and its metrics.

## Model
`sentence-transformers/all-MiniLM-L6-v2`, CPU. The supplied notebook reports:
- model load: about 7.7 seconds
- token limit: 256

## Dataset
`corpus.json` contains the final six-document synthetic corpus used by the notebook.
`queries.json` contains 8 answerable and 2 unanswerable queries.

## Retrieval
The lab compares:
- 40-word windows, overlap 0
- 40-word windows, overlap 10
- sentence-aware chunks
- TF-IDF
- MiniLM embeddings

Metrics are Hit@3 and MRR@3.

## Reproducibility note
The current execution environment does not have `sentence-transformers` installed.
Therefore the embedding rows in `retrieval_log.csv` are marked as notebook-recorded
rather than fabricated. Install the requirements and run `task3_retrieval.py` to
regenerate the complete embedding log.

## GitHub hygiene
Do not commit credentials, private data, model caches, or virtual environments.
The corpus is synthetic lab data.

## Attribution
The corpus, queries, notebook experiment and recorded results are from the supplied
Lab 6 working notebook. The standalone scripts are cleaned/adapted versions prepared
for this submission.
