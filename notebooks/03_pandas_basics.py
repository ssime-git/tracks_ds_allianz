# Databricks notebook source
# MAGIC %md
# MAGIC # 03 — pandas Basics
# MAGIC
# MAGIC **Goal:** load a table, inspect it, filter rows, select columns, sort, and aggregate.
# MAGIC These are the five operations you repeat in every analysis.
# MAGIC
# MAGIC > **Dataset:** `insurance.csv` — 420 rows, 7 columns.
# MAGIC > Each row is one policyholder. The target column is `charges` (annual medical cost).
# MAGIC >
# MAGIC > | Column | Type | Description |
# MAGIC > |--------|------|-------------|
# MAGIC > | `age` | int | age of the beneficiary |
# MAGIC > | `sex` | str | `male` / `female` |
# MAGIC > | `bmi` | float | body mass index |
# MAGIC > | `children` | int | number of dependents |
# MAGIC > | `smoker` | str | `yes` / `no` |
# MAGIC > | `region` | str | geographic zone (4 values) |
# MAGIC > | `charges` | float | annual medical cost — our target |

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Import pandas
# MAGIC
# MAGIC > `pandas` is the standard Python package for working with tabular data.
# MAGIC > Think of it as a programmable spreadsheet — same structure (rows and columns),
# MAGIC > but with code instead of mouse clicks.
# MAGIC >
# MAGIC > The universal convention is to import it under the alias `pd`:
# MAGIC >
# MAGIC > ```python
# MAGIC > import pandas as pd
# MAGIC > ```
# MAGIC >
# MAGIC > You will see `pd.` in front of every pandas function throughout the session.
# MAGIC > If you write `pandas.read_csv(...)` it also works, but `pd.read_csv(...)` is the standard.

# COMMAND ----------

import pandas as pd

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** always keep the `pd` alias. It is understood by every Python analyst.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Load a CSV file
# MAGIC
# MAGIC > To read a CSV file into a pandas DataFrame, use `pd.read_csv()`.
# MAGIC > In Databricks, pandas reads files through the cluster filesystem — the path must start with `/dbfs`.
# MAGIC >
# MAGIC > ```python
# MAGIC > df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")
# MAGIC > ```
# MAGIC >
# MAGIC > - `pd.read_csv(...)` — the function that reads a CSV.
# MAGIC > - `/dbfs/FileStore/tables/` — the path where the file was uploaded.
# MAGIC > - `df` — the name of the resulting DataFrame. You can choose any name; `df` is the convention.

# COMMAND ----------

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell above. Then check the type of `df` using `type(df)`.
# MAGIC >
# MAGIC > **(b)** What is the expected output? Predict before running.

# COMMAND ----------

# (a) and (b)
type(df)

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python">type(df)
# → pandas.core.frame.DataFrame</code></pre>
<p>After loading, always verify the object is a DataFrame before continuing.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** if you get a `FileNotFoundError`, check that the path starts with `/dbfs`. That is the most common cause.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Inspect the Table
# MAGIC
# MAGIC > Three commands you run on every new dataset before doing anything else:
# MAGIC >
# MAGIC > | Command | Question it answers |
# MAGIC > |---------|---------------------|
# MAGIC > | `df.head()` | What do the first rows look like? |
# MAGIC > | `df.info()` | How many rows? What columns? What types? Any missing values? |
# MAGIC > | `df.describe()` | What are the ranges, averages, and quartiles of numeric columns? |
# MAGIC >
# MAGIC > SAS equivalents:
# MAGIC >
# MAGIC > | SAS | pandas |
# MAGIC > |-----|--------|
# MAGIC > | `PROC PRINT (obs=5)` | `df.head()` |
# MAGIC > | `PROC CONTENTS` | `df.info()` |
# MAGIC > | `PROC MEANS` | `df.describe()` |

# COMMAND ----------

df.head()

# COMMAND ----------

df.info()

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** How many rows does the dataset have? Find the answer in the output of `df.info()`.
# MAGIC >
# MAGIC > **(b)** Use `df.columns` to list all column names. Which column represents medical cost?
# MAGIC >
# MAGIC > **(c)** From `df.describe()`, what is the average value of `charges`? Is the max much higher than the mean — what might that suggest?

# COMMAND ----------

# (a) — already visible above, note the number

# (b)
df.columns

# COMMAND ----------

# (c) — already visible above, read and interpret
df.describe()

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<p>(a) 420 rows — visible in <code>df.info()</code> as "420 entries".</p>
<p>(b) The target column is <code>charges</code>.</p>
<p>(c) The max of <code>charges</code> is much higher than the mean, suggesting a right-skewed distribution — a small number of policyholders have very high medical costs.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** never filter or aggregate before running these three inspection commands. Always know your data first.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Select Columns
# MAGIC
# MAGIC > To keep only specific columns, pass a list of names inside double brackets.
# MAGIC >
# MAGIC > ```python
# MAGIC > df[["age", "charges"]]        # two columns → DataFrame
# MAGIC > df["charges"]                 # one column  → Series (different object)
# MAGIC > ```
# MAGIC >
# MAGIC > Double brackets `[[ ]]` = multiple columns → returns a DataFrame.
# MAGIC > Single bracket `[ ]` = one column → returns a Series.
# MAGIC >
# MAGIC > SAS equivalent:
# MAGIC > ```sas
# MAGIC > data work.small;
# MAGIC >     set insurance (keep = age charges);
# MAGIC > run;
# MAGIC > ```

# COMMAND ----------

df[["age", "charges"]].head()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Select the columns `smoker` and `charges`. Display the first 5 rows.
# MAGIC >
# MAGIC > **(b)** Select `age`, `bmi`, and `charges`. How many columns does the result have?
# MAGIC >
# MAGIC > **(c)** What happens if you write `df["smoker", "charges"]` (single bracket)?
# MAGIC > Try it and read the error.

# COMMAND ----------

# (a)
df[[..., ...]].head()

# COMMAND ----------

# (b)
df[[..., ..., ...]].head()

# COMMAND ----------

# (c) — expected error
df["smoker", "charges"]

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
df[["smoker", "charges"]].head()

# (b) — 3 columns
df[["age", "bmi", "charges"]].head()

# (c) KeyError — single bracket with a tuple is not the right syntax.
# Always use double brackets [[ ]] for multiple columns.</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** double brackets `[[ ]]` for multiple columns. The inner `[ ]` is the Python list.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Filter Rows
# MAGIC
# MAGIC > Filtering keeps only the rows where a condition is true.
# MAGIC >
# MAGIC > ```python
# MAGIC > df[df["smoker"] == "yes"]
# MAGIC > ```
# MAGIC >
# MAGIC > Read this as: "from `df`, keep the rows where the `smoker` column equals `yes`."
# MAGIC >
# MAGIC > - `df["smoker"] == "yes"` produces a true/false value for each row.
# MAGIC > - The outer `df[...]` keeps only the rows where the answer is `True`.
# MAGIC > - `==` is comparison (tests equality). `=` is assignment (stores a value). They are not the same.
# MAGIC >
# MAGIC > **Two conditions** — each wrapped in parentheses, joined with `&` (AND) or `|` (OR):
# MAGIC > ```python
# MAGIC > df[(df["age"] > 50) & (df["smoker"] == "yes")]
# MAGIC > ```
# MAGIC >
# MAGIC > SAS equivalent:
# MAGIC > ```sas
# MAGIC > data work.smokers;
# MAGIC >     set insurance;
# MAGIC >     where smoker = 'yes';
# MAGIC > run;
# MAGIC > ```

# COMMAND ----------

df[df["smoker"] == "yes"].head()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Filter rows where `bmi > 30`. How many rows are returned? Use `len()`.
# MAGIC >
# MAGIC > **(b)** Filter rows where `age > 50` AND `smoker == "yes"`. Display the first 5 rows.
# MAGIC >
# MAGIC > **(c)** Filter rows where `sex == "female"` OR `region == "northeast"`.
# MAGIC > Before running: do you expect more or fewer rows than the smoker filter?

# COMMAND ----------

# (a)
result_a = df[df[...] > ...]
len(result_a)

# COMMAND ----------

# (b)
df[(df[...] > ...) & (df[...] == ...)].head()

# COMMAND ----------

# (c)
df[(df[...] == ...) | (df[...] == ...)].head()

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
result_a = df[df["bmi"] > 30]
len(result_a)

# (b)
df[(df["age"] > 50) & (df["smoker"] == "yes")].head()

# (c) — OR returns more rows than AND
df[(df["sex"] == "female") | (df["region"] == "northeast")].head()</code></pre>
<p><strong>Common mistake:</strong> forgetting parentheses around each condition with <code>&amp;</code>.
Without them, Python raises a <code>ValueError</code>.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** `==` compares. `=` assigns. In SAS, one `=` does both — in Python they are strictly separate.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Sort
# MAGIC
# MAGIC > `sort_values()` sorts the DataFrame by one or more columns.
# MAGIC >
# MAGIC > ```python
# MAGIC > df.sort_values("charges", ascending=False)   # highest charges first
# MAGIC > ```
# MAGIC >
# MAGIC > - `"charges"` — the column to sort by.
# MAGIC > - `ascending=False` — descending order (largest first).
# MAGIC > - `ascending=True` (default) — ascending order (smallest first).
# MAGIC >
# MAGIC > SAS equivalent:
# MAGIC > ```sas
# MAGIC > proc sort data=insurance out=sorted;
# MAGIC >     by descending charges;
# MAGIC > run;
# MAGIC > ```

# COMMAND ----------

df.sort_values("charges", ascending=False).head()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Sort by `bmi`, highest first. Display the top 5 rows.
# MAGIC >
# MAGIC > **(b)** Sort by `age` from youngest to oldest. What is the youngest age in the dataset?
# MAGIC >
# MAGIC > **(c)** Sort by two columns: first by `smoker` (alphabetical), then by `charges` (descending).
# MAGIC > Hint: pass a list to `sort_values(["col1", "col2"], ascending=[True, False])`.

# COMMAND ----------

# (a)
df.sort_values(..., ascending=...).head()

# COMMAND ----------

# (b)
df.sort_values(..., ascending=...).head(1)

# COMMAND ----------

# (c) — multi-column sort
df.sort_values([..., ...], ascending=[..., ...]).head()

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
df.sort_values("bmi", ascending=False).head()

# (b)
df.sort_values("age", ascending=True).head(1)

# (c)
df.sort_values(["smoker", "charges"], ascending=[True, False]).head()</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** after sorting, read the first rows and verify the order matches your expectation before drawing conclusions.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. Aggregate with `groupby`
# MAGIC
# MAGIC > `groupby` splits the table by a category, applies a function to each group, and combines the results.
# MAGIC > It is the equivalent of `PROC MEANS` with a `CLASS` statement.
# MAGIC >
# MAGIC > ```python
# MAGIC > df.groupby("region")["charges"].mean()
# MAGIC > ```
# MAGIC >
# MAGIC > Read: "group by `region`, take the `charges` column, compute the mean."
# MAGIC >
# MAGIC > SAS equivalent:
# MAGIC > ```sas
# MAGIC > proc means data=insurance mean;
# MAGIC >     class smoker;
# MAGIC >     var charges;
# MAGIC > run;
# MAGIC > ```
# MAGIC >
# MAGIC > | SAS | pandas |
# MAGIC > |-----|--------|
# MAGIC > | `CLASS smoker` | `.groupby("smoker")` |
# MAGIC > | `VAR charges` | `["charges"]` |
# MAGIC > | `MEAN` | `.mean()` |
# MAGIC > | `N` | `.count()` |
# MAGIC > | `MAX` | `.max()` |

# COMMAND ----------

df.groupby("region")["charges"].mean()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Compute the mean of `charges` grouped by `smoker`. Which group has higher costs?
# MAGIC >
# MAGIC > **(b)** Compute the mean of `charges` grouped by `sex`.
# MAGIC >
# MAGIC > **(c)** For each `region`, compute both the **mean** and the **count** of `charges`.
# MAGIC > Use `.agg(["mean", "count"])` after selecting the column.
# MAGIC > Then write one sentence interpreting the region with the highest average.

# COMMAND ----------

# (a)
df.groupby(...)["charges"].mean()

# COMMAND ----------

# (b)
df.groupby(...)["charges"].mean()

# COMMAND ----------

# (c)
df.groupby(...)["charges"].agg([..., ...])

# COMMAND ----------

displayHTML("""
<style>
.solution-box {font-family: Arial, sans-serif; border: 1px solid #d8d4ca; border-left: 6px solid #ff6745; background: #f8f7f3; padding: 12px 16px; border-radius: 6px; margin: 8px 0;}
.solution-box summary {cursor: pointer; font-weight: 700; color: #1a1a33;}
.solution-box pre {background: #1a1a33; color: #ffffff; padding: 12px; border-radius: 4px; overflow-x: auto;}
.solution-box code {font-family: Menlo, Consolas, monospace;}
</style>
<details class="solution-box">
<summary>Show solution</summary>
<div>
<pre><code class="language-python"># (a)
df.groupby("smoker")["charges"].mean()
# Smokers (yes) have much higher average charges than non-smokers.

# (b)
df.groupby("sex")["charges"].mean()

# (c)
df.groupby("region")["charges"].agg(["mean", "count"])</code></pre>
<p>(c) Interpretation example: "The southeast region has the highest average charges in this dataset.
This is a descriptive observation — it does not prove causality."</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** an aggregated number without a business sentence is just a number.
# MAGIC > Always end with: "the segment with the highest average is X — this means..."

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this notebook you learned the five core pandas operations:
# MAGIC >
# MAGIC > | Operation | pandas | SAS equivalent |
# MAGIC > |-----------|--------|----------------|
# MAGIC > | Load CSV | `pd.read_csv("/dbfs/...")` | `PROC IMPORT` |
# MAGIC > | Preview | `df.head()` | `PROC PRINT (obs=5)` |
# MAGIC > | Inspect structure | `df.info()` | `PROC CONTENTS` |
# MAGIC > | Statistics | `df.describe()` | `PROC MEANS` |
# MAGIC > | Select columns | `df[["col1", "col2"]]` | `KEEP =` |
# MAGIC > | Filter rows | `df[df["col"] == "val"]` | `WHERE col = 'val'` |
# MAGIC > | Sort | `df.sort_values("col", ascending=False)` | `PROC SORT by descending col` |
# MAGIC > | Aggregate | `df.groupby("col")["target"].mean()` | `PROC MEANS class col var target` |
# MAGIC >
# MAGIC > **The analysis workflow:**
# MAGIC >> 1. Load → 2. Inspect → 3. Filter → 4. Aggregate → 5. Interpret with a business sentence.
