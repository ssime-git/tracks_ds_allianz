# Databricks notebook source
# MAGIC %md
# MAGIC # 01 — Introduction to Azure Databricks
# MAGIC
# MAGIC **Goal:** navigate the Databricks workspace, run your first cells, and understand how code, data, and results connect — before writing any analysis.
# MAGIC
# MAGIC ## SAS → Databricks: what changes, what stays the same
# MAGIC
# MAGIC > You already know how to write logic, filter data, and produce aggregates in SAS.
# MAGIC > None of that knowledge disappears. What changes is the *environment* you work in.
# MAGIC >
# MAGIC > | SAS | Databricks | What it means |
# MAGIC > |-----|------------|---------------|
# MAGIC > | SAS Program | Notebook | Your code lives here |
# MAGIC > | Block of code | Cell | Executed one at a time |
# MAGIC > | Log / Output window | Result under the cell | Appears immediately |
# MAGIC > | SAS Dataset | DataFrame | The table you manipulate |
# MAGIC > | LIBNAME / library | FileStore / Catalog | Where your data lives |
# MAGIC > | Macro variable | Python variable | Stored value, reusable |
# MAGIC >
# MAGIC > **The goal of this notebook:** get comfortable with the environment before writing any analysis.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. The Notebook
# MAGIC
# MAGIC > A Databricks notebook mixes three things in the same document:
# MAGIC >
# MAGIC > - **Text cells** (Markdown) — explanations, titles, instructions. Not executed.
# MAGIC > - **Code cells** (Python, SQL) — the logic you run. Results appear immediately below.
# MAGIC > - **Results** — displayed directly under the cell that produced them.
# MAGIC >
# MAGIC > Every cell is **independent**. You can run them one by one, in any order.
# MAGIC > Running a cell does **not** automatically run the cells above or below it.
# MAGIC >
# MAGIC > **How to run a cell:** click on it and press **Shift + Enter**, or click the ▶ button on the left.
# MAGIC >
# MAGIC > The cell below is a Python code cell. It uses `print()` to display a message.

# COMMAND ----------

# This is a Python code cell.
# Run it: click here and press Shift + Enter.
print("Hello Databricks")

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Replace `"Hello Databricks"` with your first name. Run the cell. Read the result below.
# MAGIC >
# MAGIC > **(b)** Replace it with your team name. Run again.
# MAGIC > Notice: the previous result disappears — only the most recent execution is shown.

# COMMAND ----------

# (a) and (b) — modify and run
print("...")

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
print("Alice")

# (b)
print("Allianz Analytics")</code></pre>
<p>The result updates each time you run the cell. Each new execution replaces the previous output.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** run cells one at a time when learning. Avoid **Run All** until you understand what each cell does.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Variables
# MAGIC
# MAGIC > A variable gives a name to a value so you can reuse it later.
# MAGIC > In SAS you might write:
# MAGIC >
# MAGIC > ```sas
# MAGIC > %let age = 45;
# MAGIC > %let region = 'southwest';
# MAGIC > ```
# MAGIC >
# MAGIC > In Python:
# MAGIC >
# MAGIC > ```python
# MAGIC > age = 45
# MAGIC > region = "southwest"
# MAGIC > ```
# MAGIC >
# MAGIC > - The `=` sign **stores** a value into a name. It does not test equality.
# MAGIC > - There are no quotes around the variable name — only around text values.
# MAGIC > - Numbers are written without quotes: `45`, `27.5`.
# MAGIC > - Text is written with double or single quotes: `"southwest"`, `'yes'`.
# MAGIC >
# MAGIC > Use `print()` to display a variable's value.

# COMMAND ----------

age = 45
region = "southwest"

print(age)
print(region)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Change `age` to `52` and `region` to `"northeast"`. Run the cell. Verify both values printed.
# MAGIC >
# MAGIC > **(b)** Add a third variable `premium` with value `1200.50`. Print all three variables.
# MAGIC >
# MAGIC > **(c)** Before running: predict which type each variable is — whole number, decimal, or text?

# COMMAND ----------

# (a) Modify age and region
age = ...
region = ...

print(age)
print(region)

# COMMAND ----------

# (b) Add premium and print all three
age = 52
region = "northeast"
premium = ...

print(age)
print(region)
print(premium)

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
<pre><code class="language-python">age = 52
region = "northeast"
premium = 1200.50

print(age)      # 52      → int (whole number)
print(region)   # northeast → str (text)
print(premium)  # 1200.5  → float (decimal)</code></pre>
<p>(c) Types: <code>age</code> is an integer, <code>region</code> is a string, <code>premium</code> is a float.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** if the result does not change after you edit the cell, check that you actually ran it (Shift + Enter).

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Arithmetic and Expressions
# MAGIC
# MAGIC > Python can compute directly on variables. The result of an expression is displayed
# MAGIC > if it is the **last line** of the cell — no `print()` needed.
# MAGIC >
# MAGIC > Common operators:
# MAGIC >
# MAGIC > | Operator | Meaning | Example |
# MAGIC > |----------|---------|---------|
# MAGIC > | `+` | addition | `premium + 100` |
# MAGIC > | `-` | subtraction | `charges - tax` |
# MAGIC > | `*` | multiplication | `premium * 1.2` |
# MAGIC > | `/` | division | `charges / 12` |
# MAGIC > | `**` | power | `bmi ** 2` |
# MAGIC >
# MAGIC > Example: calculate a premium with a 20 % tax applied.

# COMMAND ----------

premium = 1000
premium_with_tax = premium * 1.2

premium_with_tax   # last line → displayed automatically

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Change `premium` to `1500`. Predict the result before running.
# MAGIC >
# MAGIC > **(b)** Create a variable `monthly_premium` equal to `premium_with_tax` divided by `12`. Display it.
# MAGIC >
# MAGIC > **(c)** A policy costs `850` per year. Calculate the cost over `5` years using only variables (no hard-coded multiplication).

# COMMAND ----------

# (a) Change premium and re-run
premium = ...
premium_with_tax = premium * 1.2
premium_with_tax

# COMMAND ----------

# (b) Monthly premium
premium = 1500
premium_with_tax = premium * 1.2
monthly_premium = ...
monthly_premium

# COMMAND ----------

# (c) Cost over 5 years
annual_cost = 850
years = 5
total_cost = ...
total_cost

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
<pre><code class="language-python"># (a) — expected: 1800.0
premium = 1500
premium_with_tax = premium * 1.2

# (b) — expected: 150.0
monthly_premium = premium_with_tax / 12

# (c) — expected: 4250
annual_cost = 850
years = 5
total_cost = annual_cost * years</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** store intermediate results in variables with clear names. `premium_with_tax` is readable; `x` or `tmp` is not.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. The Two File Paths
# MAGIC
# MAGIC > When you load a CSV file in Databricks, the path you write depends on **which tool** reads it.
# MAGIC >
# MAGIC > | Tool | Path format | Example |
# MAGIC > |------|-------------|---------|
# MAGIC > | **pandas** | starts with `/dbfs` | `/dbfs/FileStore/tables/insurance.csv` |
# MAGIC > | **Spark** | no `/dbfs` prefix | `/FileStore/tables/insurance.csv` |
# MAGIC >
# MAGIC > This is the most common source of `FileNotFoundError` for beginners.
# MAGIC > If pandas cannot find the file, the first thing to check is the `/dbfs` prefix.
# MAGIC >
# MAGIC > You will use both paths throughout the session:
# MAGIC >
# MAGIC > ```python
# MAGIC > # pandas
# MAGIC > df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")
# MAGIC >
# MAGIC > # Spark
# MAGIC > spark_df = spark.read.csv("/FileStore/tables/insurance.csv", header=True, inferSchema=True)
# MAGIC > ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Common Errors
# MAGIC
# MAGIC > Three errors that happen to everyone at the start:
# MAGIC >
# MAGIC > | Problem | Symptom | Fix |
# MAGIC > |---------|---------|-----|
# MAGIC > | Cluster not attached | Cell stays pending (spinning) | Go to Compute → attach a cluster |
# MAGIC > | Cell not executed yet | `NameError: name 'df' is not defined` | Run all cells above in order |
# MAGIC > | pandas path missing `/dbfs` | `FileNotFoundError` | Add `/dbfs` in front of the path |
# MAGIC > | Ran the wrong cell | Unexpected result | Check the cell number `[n]` on the left |
# MAGIC >
# MAGIC > **Rule:** always run cells top to bottom. A variable only exists after the cell that creates it has been executed.

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell below without having defined `x` first. Read the error message carefully.
# MAGIC > This is a `NameError` — Python does not know `x` yet.

# COMMAND ----------

# This will raise a NameError — that is expected.
# Read the message, then run the cell below to fix it.
print(x)

# COMMAND ----------

# Fix: define x first, then print it.
x = 10
print(x)

# COMMAND ----------

# MAGIC %md
# MAGIC > 💡 **Key rule:** when you see `NameError`, look for the cell that *defines* that variable and run it first.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this notebook you learned to:
# MAGIC >
# MAGIC > | Concept | Python | SAS equivalent |
# MAGIC > |---------|--------|----------------|
# MAGIC > | Display a value | `print("text")` | `PUT` / output window |
# MAGIC > | Store a value | `age = 45` | `%let age = 45;` |
# MAGIC > | Arithmetic | `premium * 1.2` | same operators |
# MAGIC > | pandas path | `/dbfs/FileStore/tables/file.csv` | LIBNAME path |
# MAGIC > | Spark path | `/FileStore/tables/file.csv` | — |
# MAGIC >
# MAGIC > **Three rules to remember:**
# MAGIC >> 1. Run cells one at a time — do not use Run All while learning.
# MAGIC >> 2. A variable only exists after you have run the cell that creates it.
# MAGIC >> 3. pandas paths start with `/dbfs`; Spark paths do not.
