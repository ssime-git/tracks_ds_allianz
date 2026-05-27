# Week 1 — Update Plan

## What changes and why

The current materials are functional but written in a "minimal guided" style: brief explanations, one practice cell per concept, hidden toggle corrections via `displayHTML`. The reference course (DataScientest `101_python_pour_la_data_science_fr`) uses a richer pedagogical pattern that is much better for beginners:

- **Rich blockquoted explanations** (`>` blockquotes) with nested detail levels (`>>`)
- **Worked example before every exercise** — learners read before they try
- **Multiple sub-exercises per concept** — labelled **(a)**, **(b)**, **(c)** — increasing difficulty
- **Plain solution code cells** — no `displayHTML` toggle tricks; solutions are just the next cell
- **`# Insert your code here` placeholder** in every exercise cell
- **Alert boxes** (`<div class="alert alert-info">`) for tips and pitfalls
- **Conclusion cell** at the end of every notebook — lists all methods seen with syntax reference
- **All in English**

---

## Bugs to fix (identified in initial review)

| # | Severity | Location | Issue |
|---|----------|----------|-------|
| 1 | 🔴 Critical | Slides 3 & 44 | Row count says **1338** (Kaggle original) but synthetic CSV has **420 rows** |
| 2 | 🟠 Medium | `02_python_basics.py` | **Lists concept missing** — slide 30 covers it, notebook does not |
| 3 | 🟠 Medium | `04_spark_basics.py` | `printSchema` labelled "À vous" but code is pre-filled — not a real exercise |
| 4 | 🟠 Medium | `06_guided_exercises.py` | Exercise 2: `bmi > 30` solution already written in practice cell |
| 5 | 🟠 Medium | `05_sql_basics.py` | GROUP BY exercises: SELECT already shows the column, making `<à remplacer>` trivial |
| 6 | 🟡 Minor | Slides 18, 92 | Notebook path `/Shared/training/01_Intro_Databricks` — inconsistent with other slides using `/Shared/training/week1/` |
| 7 | 🟡 Minor | Slide 82 vs run-of-show | Challenge duration: slide says **20 min**, run-of-show says **10 min** |
| 8 | 🟡 Minor | Slide 49 | References 4th filter (female smokers) pointing to notebook 03, but that notebook only has 3 filters |

---

## Pedagogical standard to apply (from reference course)

### Why keep `displayHTML` for solutions

In Databricks, **all cells are always visible** — there is no way to hide a cell from learners. A plain solution code cell placed after an exercise cell would immediately reveal the answer. The `displayHTML` + `<details>/<summary>` pattern is therefore the **correct Databricks approach**: learners see the exercise, write their answer, then actively click to reveal the solution. This is intentional and should be kept as-is across all notebooks.

The reference course (DataScientest) uses standard Jupyter where cells can be hidden — that mechanism does not exist in Databricks.

### Cell pattern per concept
```
# MAGIC %md
## Concept N — Name

> [Rich explanation with blockquotes]
>
> SAS equivalent (where relevant):
> | SAS | Python |
>
> Example:
> ```python
> # Worked example with inline comments
> ```

# COMMAND ----------
# Worked example code

# COMMAND ----------
# MAGIC %md
> **(a)** First sub-exercise — direct application of the example.
>
> **(b)** Second sub-exercise — slight variation.

# COMMAND ----------
# Insert your code here — (a)

# COMMAND ----------
# Insert your code here — (b)

# COMMAND ----------
# displayHTML(...) — hidden solution for (a) and (b)

# COMMAND ----------
# MAGIC %md
> <div class="alert alert-info">💡 Key takeaway: ...</div>
```

### End-of-notebook conclusion
```
# MAGIC %md
## Summary

> In this notebook you learned to:
>> * **Method** `syntax()` — what it does.
>> * **Method** `syntax()` — what it does.
>
> | Concept | Python | SAS equivalent |
> |---------|--------|----------------|
```

---

## Notebook-by-notebook changes

### 01 — Introduction to Databricks
**Current:** 4 concepts (notebook, first cell, variables, arithmetic). Brief explanations. `displayHTML` solutions.  
**Changes:**
- Translate to English
- Richer explanations for all 4 concepts
- Add SAS → Databricks mapping table in the introduction
- Multiple sub-exercises per concept (a/b/c)
- Keep `displayHTML` hidden solutions (correct Databricks pattern)
- Add "Common errors" section (cluster not attached, path without `/dbfs`, running cells out of order)
- Add conclusion

### 02 — Python Basics
**Current:** Modules, Variables, Types, Conditions, Functions. Missing Lists entirely.  
**Changes:**
- Translate to English
- **Add Lists concept** after Variables/Types: `regions = ["northeast", ...]`, `len()`, indexing `[0]`, negative indexing, adding elements with `append()`
- Richer explanations with SAS DATA step comparisons
- Multiple sub-exercises per concept
- Keep `displayHTML` hidden solutions
- Add conclusion

### 03 — pandas Basics
**Current:** 7 concepts (import, load, inspect, select, filter, sort, groupby). Good coverage, brief explanations.  
**Changes:**
- Translate to English
- Richer blockquoted explanations for each concept
- Enrich SAS → pandas comparison (add `PROC SORT → sort_values`, `PROC CONTENTS → info()`)
- Multiple sub-exercises per concept (particularly for filter and groupby)
- Keep `displayHTML` hidden solutions
- Add conclusion with full method reference table

### 04 — Spark Basics
**Current:** 5 concepts (intro, read CSV, select, filter, groupby).  
**Changes:**
- Translate to English
- **Fix printSchema exercise**: add `...` placeholder — currently pre-filled
- Richer explanations
- Add pandas ↔ Spark side-by-side reference table embedded in each concept
- Multiple sub-exercises
- Keep `displayHTML` hidden solutions
- Add conclusion

### 05 — SQL Basics
**Current:** 5 concepts (temp view, preview, count, groupby, where).  
**Changes:**
- Translate to English
- **Fix GROUP BY exercises**: exercise cell currently shows `SELECT smoker` then asks learner to fill `GROUP BY <à remplacer>` — the SELECT already gives the answer. Restructure so the full query needs to be modified (e.g., `SELECT <column>` is also blank)
- Richer explanations with SAS PROC SQL → Databricks SQL comparison
- Multiple sub-exercises
- Keep `displayHTML` hidden solutions
- Add conclusion

### 06 — Guided Exercises
**Current:** 5 exercises + mini challenge. Exercise 2 has the answer already written.  
**Changes:**
- Translate to English
- **Fix exercise 2**: replace `df[df["bmi"] > 30].head()` with `df[df[...] > ...].head()`
- Restructure as a cohesive practice session with a clear narrative: "from exploration to interpretation"
- Each exercise: context cell → `# Insert your code here` → solution cell
- Add a warm-up intro cell explaining what the session covers
- Add conclusion

### 07 — Afternoon Consolidation
**Current:** 8 steps, good progressive structure, French.  
**Changes:**
- Translate to English
- Richer step explanations (blockquotes)
- Keep `displayHTML` hidden solutions
- Add intro cell explaining session objectives
- Add conclusion

### 08 — Afternoon Case Study
**Current:** 6 steps, case study structure, French.  
**Changes:**
- Translate to English
- Richer explanations — particularly around `pd.cut()` (segmentation concept, explain bins/labels)
- Keep `displayHTML` hidden solutions
- Add structured conclusion template: "1. The most expensive segment is... 2. The result is based on... 3. Limitation: ..."

---

## Slides changes

| Slide(s) | Change |
|----------|--------|
| 3, 44 | Row count: 1338 → **420** |
| 18, 92 | Notebook path: `/Shared/training/01_Intro_Databricks` → `/Shared/training/week1/01_intro_databricks` |
| 82 | Challenge duration: 20 min → **10 min** |
| 49 | Remove 4th filter (female smokers) from exercise list since it's not in notebook 03, or add it to notebook 03 |
| All | Translate all text to **English** |

---

## Execution order

1. `01_intro_databricks.py`
2. `02_python_basics.py`
3. `03_pandas_basics.py`
4. `04_spark_basics.py`
5. `05_sql_basics.py`
6. `06_guided_exercises.py`
7. `07_afternoon_consolidation.py`
8. `08_afternoon_case_study.py`
9. Slides (pptx)
