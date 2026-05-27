# Databricks notebook source
# MAGIC %md
# MAGIC # 05 — SQL Basics in Databricks
# MAGIC
# MAGIC **Goal:** run SQL queries directly inside a Databricks notebook using the `%sql` magic command.
# MAGIC
# MAGIC > You already know SQL from SAS `PROC SQL`. The syntax in Databricks is standard SQL — nearly identical.
# MAGIC > The only step that is new: you must first **expose your Spark DataFrame as a SQL view** so that
# MAGIC > SQL cells can query it by name.
# MAGIC >
# MAGIC > | SAS PROC SQL | Databricks SQL | Notes |
# MAGIC > |-------------|----------------|-------|
# MAGIC > | `PROC SQL;` | `%sql` magic at top of cell | Switches the cell to SQL mode |
# MAGIC > | `CREATE TABLE AS SELECT ...` | `CREATE OR REPLACE TEMP VIEW ...` | Temporary in-session table |
# MAGIC > | `SELECT * FROM lib.table` | `SELECT * FROM view_name` | Query by view name |
# MAGIC > | `GROUP BY col` | `GROUP BY col` | Identical |
# MAGIC > | `WHERE condition` | `WHERE condition` | Identical |
# MAGIC > | `QUIT;` | (nothing) | No closing statement needed |

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Create a Temporary View
# MAGIC
# MAGIC > SQL cells in Databricks cannot directly query a Python variable like `spark_df`.
# MAGIC > You first need to register it as a **temporary view** — a named SQL table that lives for the duration of your session.
# MAGIC >
# MAGIC > ```python
# MAGIC > spark_df.createOrReplaceTempView("insurance")
# MAGIC > ```
# MAGIC >
# MAGIC > After this line, any `%sql` cell can use `FROM insurance`.
# MAGIC >
# MAGIC > - `createOrReplace` means: if a view named `insurance` already exists, overwrite it.
# MAGIC > - The view is **temporary** — it disappears when the cluster restarts.
# MAGIC > - You can create as many views as you need, with different names.

# COMMAND ----------

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

spark_df.createOrReplaceTempView("insurance")

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell above. No output is expected — the view is created silently.
# MAGIC >
# MAGIC > **(b)** Run the SQL cell below to verify the view exists. If you see rows, the view was created correctly.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC LIMIT 3

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
<pre><code class="language-python"># (a) — Python cell: register the view
spark_df.createOrReplaceTempView("insurance")

# (b) — SQL cell: check the view exists</code></pre>
<pre><code class="language-sql">SELECT *
FROM insurance
LIMIT 3</code></pre>
<p>If you see 3 rows with columns age, sex, bmi, children, smoker, region, charges — the view is ready.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always run the Python cell that creates the view <strong>before</strong> running any SQL cell. If you see "Table or view not found: insurance", run the setup cell first.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Preview and Count
# MAGIC
# MAGIC > Two queries you run on every new dataset:
# MAGIC >
# MAGIC > **Preview** — see the first few rows:
# MAGIC > ```sql
# MAGIC > SELECT *
# MAGIC > FROM insurance
# MAGIC > LIMIT 10
# MAGIC > ```
# MAGIC >
# MAGIC > **Count** — verify the total number of rows:
# MAGIC > ```sql
# MAGIC > SELECT COUNT(*) AS row_count
# MAGIC > FROM insurance
# MAGIC > ```
# MAGIC >
# MAGIC > `COUNT(*)` counts every row regardless of NULL values.
# MAGIC > `AS row_count` gives the result column a readable name.
# MAGIC >
# MAGIC > | SAS | SQL |
# MAGIC > |-----|-----|
# MAGIC > | `PROC PRINT DATA=ds (OBS=10);` | `SELECT * FROM table LIMIT 10` |
# MAGIC > | `PROC SQL; SELECT COUNT(*) FROM ds; QUIT;` | `SELECT COUNT(*) AS row_count FROM table` |

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS row_count
# MAGIC FROM insurance

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** The count should return **420**. If you get a different number, re-run the setup cell in Section 1.
# MAGIC >
# MAGIC > **(b)** Write a query that selects only `age`, `smoker`, and `charges`, limited to 10 rows.
# MAGIC >
# MAGIC > **(c)** Write a query that counts only the rows where `smoker = 'yes'`. Use `WHERE` inside a `COUNT`.
# MAGIC > Hint: `SELECT COUNT(*) FROM insurance WHERE smoker = 'yes'`

# COMMAND ----------

-- (b) — select three columns, limit 10
-- Insert your query here

# COMMAND ----------

-- (c) — count smokers only
-- Insert your query here

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
<pre><code class="language-sql">-- (b)
SELECT age, smoker, charges
FROM insurance
LIMIT 10

-- (c)
SELECT COUNT(*) AS smoker_count
FROM insurance
WHERE smoker = 'yes'</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always run COUNT(*) after loading a dataset — it is the fastest way to confirm the data loaded correctly.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Filter with WHERE
# MAGIC
# MAGIC > `WHERE` restricts which rows are returned — equivalent to a `filter()` in pandas or Spark.
# MAGIC >
# MAGIC > ```sql
# MAGIC > SELECT *
# MAGIC > FROM insurance
# MAGIC > WHERE smoker = 'yes'
# MAGIC > ```
# MAGIC >
# MAGIC > Important syntax notes:
# MAGIC > - Text values use **single quotes**: `'yes'`, `'northeast'`
# MAGIC > - Numbers use no quotes: `age > 50`, `bmi > 30`
# MAGIC > - Combine conditions: `AND`, `OR`, `NOT`
# MAGIC >
# MAGIC > ```sql
# MAGIC > WHERE smoker = 'yes' AND age > 40
# MAGIC > ```
# MAGIC >
# MAGIC > | pandas | SQL |
# MAGIC > |--------|-----|
# MAGIC > | `df[df.smoker == "yes"]` | `WHERE smoker = 'yes'` |
# MAGIC > | `df[df.age > 50]` | `WHERE age > 50` |
# MAGIC > | `df[(df.smoker == "yes") & (df.age > 40)]` | `WHERE smoker = 'yes' AND age > 40` |

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM insurance
# MAGIC WHERE smoker = 'yes'
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Write a query that returns all rows where `age > 50`. Add `LIMIT 20`.
# MAGIC >
# MAGIC > **(b)** Write a query that returns rows where `bmi > 30` **and** `smoker = 'yes'`. Count how many rows match.
# MAGIC >
# MAGIC > **(c)** Write a query that returns all columns for the `northeast` region. How many rows are there?

# COMMAND ----------

-- (a) — age > 50
-- Insert your query here

# COMMAND ----------

-- (b) — bmi > 30 AND smoker = 'yes', count rows
-- Insert your query here

# COMMAND ----------

-- (c) — northeast region, count rows
-- Insert your query here

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
<pre><code class="language-sql">-- (a)
SELECT *
FROM insurance
WHERE age > 50
LIMIT 20

-- (b)
SELECT COUNT(*) AS n
FROM insurance
WHERE bmi > 30 AND smoker = 'yes'

-- (c)
SELECT COUNT(*) AS n
FROM insurance
WHERE region = 'northeast'</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: in SQL, text values go in single quotes — <code>'yes'</code>, not <code>"yes"</code>. Double quotes are reserved for column/table names in standard SQL.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Aggregate with GROUP BY
# MAGIC
# MAGIC > `GROUP BY` groups rows by a column and computes an aggregate for each group.
# MAGIC > Equivalent to `df.groupby()` in pandas.
# MAGIC >
# MAGIC > Structure:
# MAGIC > ```sql
# MAGIC > SELECT <grouping_column>,
# MAGIC >        AGG_FUNCTION(<numeric_column>) AS result_name
# MAGIC > FROM table
# MAGIC > GROUP BY <grouping_column>
# MAGIC > ORDER BY result_name DESC
# MAGIC > ```
# MAGIC >
# MAGIC > Common aggregate functions:
# MAGIC >
# MAGIC > | Function | Meaning |
# MAGIC > |----------|---------|
# MAGIC > | `AVG(col)` | mean |
# MAGIC > | `COUNT(*)` | number of rows |
# MAGIC > | `SUM(col)` | total |
# MAGIC > | `MIN(col)` / `MAX(col)` | min / max |
# MAGIC >
# MAGIC > Every column in `SELECT` must either be in `GROUP BY` or inside an aggregate function.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT region,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Write a query that computes the average `charges` by `smoker` status, ordered from highest to lowest.
# MAGIC >
# MAGIC > **(b)** Write a query that computes **both** the average `charges` **and** the row count by `smoker`. Include both aggregations in a single query.
# MAGIC >
# MAGIC > **(c)** Write a query that computes the average `charges` by `region`. Which region has the highest average?

# COMMAND ----------

-- (a) — avg charges by smoker, ordered descending
-- Insert your query here

# COMMAND ----------

-- (b) — avg charges AND count by smoker
-- Insert your query here

# COMMAND ----------

-- (c) — avg charges by region
-- Insert your query here

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
<pre><code class="language-sql">-- (a)
SELECT smoker,
       AVG(charges) AS avg_charges
FROM insurance
GROUP BY smoker
ORDER BY avg_charges DESC

-- (b)
SELECT smoker,
       AVG(charges) AS avg_charges,
       COUNT(*) AS n
FROM insurance
GROUP BY smoker
ORDER BY avg_charges DESC

-- (c)
SELECT region,
       AVG(charges) AS avg_charges
FROM insurance
GROUP BY region
ORDER BY avg_charges DESC</code></pre>
<p>For (b): every column in SELECT must appear in GROUP BY or inside an aggregate function. Here <code>smoker</code> is in GROUP BY; <code>AVG(charges)</code> and <code>COUNT(*)</code> are aggregates.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: every non-aggregated column in SELECT must appear in GROUP BY. A common error is putting a column in SELECT but forgetting to add it to GROUP BY.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Combine WHERE and GROUP BY
# MAGIC
# MAGIC > You can combine `WHERE` (filter rows before grouping) with `GROUP BY` (aggregate the filtered rows).
# MAGIC >
# MAGIC > ```sql
# MAGIC > SELECT region,
# MAGIC >        AVG(charges) AS avg_charges,
# MAGIC >        COUNT(*) AS n
# MAGIC > FROM insurance
# MAGIC > WHERE smoker = 'yes'
# MAGIC > GROUP BY region
# MAGIC > ORDER BY avg_charges DESC
# MAGIC > ```
# MAGIC >
# MAGIC > The order of clauses is always: `SELECT → FROM → WHERE → GROUP BY → ORDER BY`.
# MAGIC > `WHERE` filters rows **before** grouping; to filter the groups themselves use `HAVING` (not covered here).

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT region,
# MAGIC        AVG(charges) AS avg_charges,
# MAGIC        COUNT(*) AS n
# MAGIC FROM insurance
# MAGIC WHERE smoker = 'yes'
# MAGIC GROUP BY region
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Write a query that computes the average `charges` by `region` **for non-smokers only** (`smoker = 'no'`). Order by `avg_charges` descending.
# MAGIC >
# MAGIC > **(b)** Write a query that computes the average `charges` and count by `smoker` status, but only for rows where `age > 40`.
# MAGIC >
# MAGIC > **(c)** Compare the result from (b) with the unrestricted groupby from Section 4. Does the age filter change which group has higher average charges?

# COMMAND ----------

-- (a) — avg charges by region, non-smokers only
-- Insert your query here

# COMMAND ----------

-- (b) — avg charges by smoker, age > 40 only
-- Insert your query here

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
<pre><code class="language-sql">-- (a)
SELECT region,
       AVG(charges) AS avg_charges,
       COUNT(*) AS n
FROM insurance
WHERE smoker = 'no'
GROUP BY region
ORDER BY avg_charges DESC

-- (b)
SELECT smoker,
       AVG(charges) AS avg_charges,
       COUNT(*) AS n
FROM insurance
WHERE age > 40
GROUP BY smoker
ORDER BY avg_charges DESC</code></pre>
<p>(c) Smokers still have higher average charges than non-smokers even when filtering to age &gt; 40 — the pattern holds across age groups.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: clause order is always SELECT → FROM → WHERE → GROUP BY → ORDER BY. Putting WHERE after GROUP BY will raise a syntax error.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this notebook you learned to run SQL inside Databricks using the `%sql` magic:
# MAGIC >
# MAGIC >> * **`spark_df.createOrReplaceTempView("name")`** — expose a Spark DataFrame as a SQL view named `"name"`.
# MAGIC >> * **`SELECT * FROM table LIMIT n`** — preview the first n rows.
# MAGIC >> * **`SELECT COUNT(*) AS row_count FROM table`** — count all rows.
# MAGIC >> * **`WHERE condition`** — filter rows; text values in single quotes, numbers without quotes.
# MAGIC >> * **`GROUP BY col`** — group rows and apply an aggregate function (AVG, COUNT, SUM, MIN, MAX).
# MAGIC >> * **`ORDER BY col DESC`** — sort results; `DESC` = highest first.
# MAGIC >> * Combine: `WHERE` filters rows before grouping; clause order is SELECT → FROM → WHERE → GROUP BY → ORDER BY.
# MAGIC >
# MAGIC > | Operation | SAS PROC SQL | Databricks SQL |
# MAGIC > |-----------|-------------|----------------|
# MAGIC > | Preview | `SELECT * FROM ds (OBS=10)` | `SELECT * FROM view LIMIT 10` |
# MAGIC > | Count | `SELECT COUNT(*) FROM ds` | `SELECT COUNT(*) AS n FROM view` |
# MAGIC > | Filter | `WHERE col = 'val'` | `WHERE col = 'val'` (identical) |
# MAGIC > | Group | `GROUP BY col` | `GROUP BY col` (identical) |
# MAGIC > | Sort | `ORDER BY col DESC` | `ORDER BY col DESC` (identical) |
