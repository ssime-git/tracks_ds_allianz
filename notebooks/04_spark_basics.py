# Databricks notebook source
# MAGIC %md
# MAGIC # 04 — Spark Basics
# MAGIC
# MAGIC **Goal:** repeat the same analytical gestures you learned in pandas — load, inspect, select, filter, aggregate — using the Spark API available natively in Databricks.
# MAGIC
# MAGIC > Spark is the distributed computing engine behind Databricks.
# MAGIC > For now, you do **not** need to understand its architecture.
# MAGIC > Focus on the gestures: the syntax is slightly different from pandas, but the logic is identical.
# MAGIC >
# MAGIC > | pandas | Spark | What it does |
# MAGIC > |--------|-------|--------------|
# MAGIC > | `pd.read_csv(...)` | `spark.read.csv(...)` | Load a CSV file |
# MAGIC > | `df.head()` | `display(spark_df)` | Preview rows |
# MAGIC > | `df.dtypes` | `spark_df.printSchema()` | Inspect column types |
# MAGIC > | `df[["col1", "col2"]]` | `spark_df.select("col1", "col2")` | Select columns |
# MAGIC > | `df[df.col > value]` | `spark_df.filter(spark_df.col > value)` | Filter rows |
# MAGIC > | `df.groupby("col")["target"].mean()` | `spark_df.groupBy("col").agg(avg("target"))` | Aggregate |

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Spark in Databricks
# MAGIC
# MAGIC > In Databricks, a variable called `spark` is available automatically in every notebook — you do not need to import or create it.
# MAGIC > It is your entry point to the Spark engine.
# MAGIC >
# MAGIC > Run `spark` on its own to confirm it is available and to see the Spark version.
# MAGIC >
# MAGIC > ```python
# MAGIC > spark   # displays the SparkSession object
# MAGIC > ```
# MAGIC >
# MAGIC > You will also use `display(...)` instead of `.head()` to preview a Spark DataFrame.
# MAGIC > `display()` renders an interactive table in the notebook output.

# COMMAND ----------

spark

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell above. Read the output — it shows the Spark version and the session name.
# MAGIC >
# MAGIC > **(b)** What is the difference between running `spark` and running `print(spark)`? Try both and compare the output format.

# COMMAND ----------

# (a) — already done above

# (b) — try print(spark) here
# Insert your code here

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
<pre><code class="language-python"># (b)
print(spark)    # plain text: SparkSession - hive

spark           # interactive link in Databricks UI</code></pre>
<p><code>print(spark)</code> returns a plain text string. Running <code>spark</code> as the last line of a cell renders a clickable link in the Databricks output.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: do not worry about Spark's distributed architecture today. Concentrate on the analytical gestures — they are the same as pandas.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Load a CSV with Spark
# MAGIC
# MAGIC > The path for Spark is **different** from the pandas path — it does **not** start with `/dbfs`.
# MAGIC >
# MAGIC > | Tool | Path format | Example |
# MAGIC > |------|-------------|---------|
# MAGIC > | pandas | starts with `/dbfs` | `/dbfs/FileStore/tables/insurance.csv` |
# MAGIC > | Spark | no `/dbfs` prefix | `/FileStore/tables/insurance.csv` |
# MAGIC >
# MAGIC > The three parameters to know:
# MAGIC >
# MAGIC > - `header=True` — the first row is the column names
# MAGIC > - `inferSchema=True` — Spark reads column types automatically (int, double, string)
# MAGIC > - Without `inferSchema=True`, every column comes in as a string
# MAGIC >
# MAGIC > Example:
# MAGIC > ```python
# MAGIC > spark_df = spark.read.csv(
# MAGIC >     "/FileStore/tables/insurance.csv",
# MAGIC >     header=True,
# MAGIC >     inferSchema=True
# MAGIC > )
# MAGIC > display(spark_df)
# MAGIC > ```

# COMMAND ----------

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

display(spark_df)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run `spark_df.printSchema()` to display each column's name and inferred type.
# MAGIC > You should see 7 columns: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`.
# MAGIC >
# MAGIC > **(b)** What type does Spark assign to `charges`? What type does it assign to `smoker`? Are these what you would expect?
# MAGIC >
# MAGIC > **(c)** Load the CSV a second time **without** `inferSchema=True`. Call it `spark_df_noschema`. Run `printSchema()` on it. What changes?

# COMMAND ----------

# (a) — print the schema
# Insert your code here

# COMMAND ----------

# (c) — load without inferSchema and inspect schema
# Insert your code here

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
spark_df.printSchema()
# Expected output:
# root
#  |-- age: integer (nullable = true)
#  |-- sex: string (nullable = true)
#  |-- bmi: double (nullable = true)
#  |-- children: integer (nullable = true)
#  |-- smoker: string (nullable = true)
#  |-- region: string (nullable = true)
#  |-- charges: double (nullable = true)

# (b) charges → double (decimal number), smoker → string (text: "yes"/"no")

# (c)
spark_df_noschema = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True
)
spark_df_noschema.printSchema()
# Without inferSchema, every column is string — including age and charges</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always check the schema after loading. If numeric columns show as <code>string</code>, add <code>inferSchema=True</code> — otherwise filters and aggregations will fail.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Select Columns
# MAGIC
# MAGIC > In pandas you select columns using double brackets: `df[["col1", "col2"]]`.
# MAGIC > In Spark you use `.select()` and pass column names as separate arguments:
# MAGIC >
# MAGIC > ```python
# MAGIC > spark_df.select("age", "charges")
# MAGIC > ```
# MAGIC >
# MAGIC > Wrap the result in `display(...)` to see a formatted table.
# MAGIC >
# MAGIC > | pandas | Spark |
# MAGIC > |--------|-------|
# MAGIC > | `df[["age", "charges"]]` | `spark_df.select("age", "charges")` |
# MAGIC > | `df[["age"]]` | `spark_df.select("age")` |
# MAGIC > | `df.columns` | `spark_df.columns` |

# COMMAND ----------

display(spark_df.select("age", "charges"))

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Select `smoker` and `charges`. Display the result.
# MAGIC >
# MAGIC > **(b)** Select `age`, `bmi`, and `smoker` together. Display the result.
# MAGIC >
# MAGIC > **(c)** Run `spark_df.columns`. What does it return? How is it different from `spark_df.select(...)`?

# COMMAND ----------

# (a) — select smoker and charges
# Insert your code here

# COMMAND ----------

# (b) — select age, bmi, smoker
# Insert your code here

# COMMAND ----------

# (c) — run spark_df.columns
# Insert your code here

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
display(spark_df.select("smoker", "charges"))

# (b)
display(spark_df.select("age", "bmi", "smoker"))

# (c)
spark_df.columns
# Returns a Python list of column name strings: ['age', 'sex', 'bmi', ...]
# select() returns a new Spark DataFrame; .columns returns a plain list</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: use <code>display(...)</code> in Databricks to preview Spark DataFrames. <code>print(spark_df)</code> only shows the schema summary, not the rows.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Filter Rows
# MAGIC
# MAGIC > In Spark, filtering uses `.filter()` with a column condition:
# MAGIC >
# MAGIC > ```python
# MAGIC > spark_df.filter(spark_df.age > 50)
# MAGIC > ```
# MAGIC >
# MAGIC > You can also write the column name as a string using `col()`:
# MAGIC >
# MAGIC > ```python
# MAGIC > from pyspark.sql.functions import col
# MAGIC > spark_df.filter(col("age") > 50)
# MAGIC > ```
# MAGIC >
# MAGIC > Both syntaxes work. `spark_df.age` is shorter; `col("age")` is more explicit.
# MAGIC >
# MAGIC > Combine conditions with `&` (and) and `|` (or), wrapped in parentheses:
# MAGIC >
# MAGIC > ```python
# MAGIC > spark_df.filter((spark_df.age > 50) & (spark_df.smoker == "yes"))
# MAGIC > ```
# MAGIC >
# MAGIC > | pandas | Spark |
# MAGIC > |--------|-------|
# MAGIC > | `df[df.age > 50]` | `spark_df.filter(spark_df.age > 50)` |
# MAGIC > | `df[df.smoker == "yes"]` | `spark_df.filter(spark_df.smoker == "yes")` |
# MAGIC > | `df[(df.age > 50) & (df.smoker == "yes")]` | `spark_df.filter((spark_df.age > 50) & (spark_df.smoker == "yes"))` |

# COMMAND ----------

display(spark_df.filter(spark_df.age > 50))

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Filter rows where `bmi > 30`. Display the result.
# MAGIC >
# MAGIC > **(b)** Filter rows where `smoker == "yes"`. How many rows remain? (Use `.count()` after `.filter()`)
# MAGIC >
# MAGIC > **(c)** Filter rows where `smoker == "yes"` **and** `age > 40`. Display the result.

# COMMAND ----------

# (a) — bmi > 30
# Insert your code here

# COMMAND ----------

# (b) — smoker == "yes", count the rows
# Insert your code here

# COMMAND ----------

# (c) — smoker and age combined
# Insert your code here

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
display(spark_df.filter(spark_df.bmi > 30))

# (b)
spark_df.filter(spark_df.smoker == "yes").count()

# (c)
display(
    spark_df.filter(
        (spark_df.smoker == "yes") &amp; (spark_df.age > 40)
    )
)</code></pre>
<p>Always wrap each condition in its own parentheses when combining with <code>&amp;</code> or <code>|</code> — otherwise Python raises a syntax error.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always wrap each condition in parentheses when combining filters — <code>(cond1) & (cond2)</code>. Without parentheses, Python raises a confusing error about operator precedence.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Aggregate with groupBy
# MAGIC
# MAGIC > Spark uses `.groupBy()` (capital B) followed by `.agg()` to compute aggregations.
# MAGIC > You need to import aggregation functions from `pyspark.sql.functions`.
# MAGIC >
# MAGIC > ```python
# MAGIC > from pyspark.sql.functions import avg, count
# MAGIC >
# MAGIC > spark_df.groupBy("region").agg(avg("charges").alias("avg_charges"))
# MAGIC > ```
# MAGIC >
# MAGIC > `.alias(...)` renames the result column — always use it to produce readable output.
# MAGIC >
# MAGIC > | pandas | Spark |
# MAGIC > |--------|-------|
# MAGIC > | `df.groupby("region")["charges"].mean()` | `spark_df.groupBy("region").agg(avg("charges").alias("avg_charges"))` |
# MAGIC > | `df.groupby("region")["charges"].count()` | `spark_df.groupBy("region").agg(count("charges").alias("n"))` |
# MAGIC > | multiple `.agg(["mean", "count"])` | `.agg(avg("charges").alias("avg_charges"), count("charges").alias("n"))` |
# MAGIC >
# MAGIC > Common functions: `avg`, `count`, `sum`, `min`, `max` — all from `pyspark.sql.functions`.

# COMMAND ----------

from pyspark.sql.functions import avg, count

display(
    spark_df
    .groupBy("region")
    .agg(avg("charges").alias("avg_charges"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Compute the average `charges` by `smoker` status. Display the result.
# MAGIC >
# MAGIC > **(b)** Compute both the average `charges` and the row count by `smoker`. Use two aggregations inside `.agg()`.
# MAGIC >
# MAGIC > **(c)** Compute the average `charges` by `region`, then sort the result by `avg_charges` descending.
# MAGIC > Hint: chain `.orderBy("avg_charges", ascending=False)` after `.agg(...)`.

# COMMAND ----------

# (a) — avg charges by smoker
# Insert your code here

# COMMAND ----------

# (b) — avg charges AND count by smoker
# Insert your code here

# COMMAND ----------

# (c) — avg charges by region, sorted descending
# Insert your code here

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
<pre><code class="language-python">from pyspark.sql.functions import avg, count

# (a)
display(
    spark_df
    .groupBy("smoker")
    .agg(avg("charges").alias("avg_charges"))
)

# (b)
display(
    spark_df
    .groupBy("smoker")
    .agg(
        avg("charges").alias("avg_charges"),
        count("charges").alias("n")
    )
)

# (c)
display(
    spark_df
    .groupBy("region")
    .agg(avg("charges").alias("avg_charges"))
    .orderBy("avg_charges", ascending=False)
)</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always rename aggregated columns with <code>.alias(...)</code>. Without it, the column appears as <code>avg(charges)</code> — hard to reference later.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this notebook you learned to work with the Spark API in Databricks:
# MAGIC >
# MAGIC >> * **`spark.read.csv(path, header=True, inferSchema=True)`** — load a CSV into a Spark DataFrame. Path has no `/dbfs` prefix.
# MAGIC >> * **`spark_df.printSchema()`** — inspect column names and inferred types.
# MAGIC >> * **`display(spark_df)`** — preview rows interactively (equivalent to `df.head()` in pandas).
# MAGIC >> * **`spark_df.select("col1", "col2")`** — select columns by name.
# MAGIC >> * **`spark_df.filter(spark_df.col > value)`** — filter rows; combine conditions with `&` and `|` inside parentheses.
# MAGIC >> * **`spark_df.groupBy("col").agg(avg("target").alias("name"))`** — aggregate by group; import functions from `pyspark.sql.functions`.
# MAGIC >> * **`.orderBy("col", ascending=False)`** — sort the result.
# MAGIC >
# MAGIC > | Operation | pandas | Spark |
# MAGIC > |-----------|--------|-------|
# MAGIC > | Load CSV | `pd.read_csv("/dbfs/...")` | `spark.read.csv("/FileStore/...", header=True, inferSchema=True)` |
# MAGIC > | Preview | `df.head()` | `display(spark_df)` |
# MAGIC > | Schema | `df.dtypes` | `spark_df.printSchema()` |
# MAGIC > | Select | `df[["col1", "col2"]]` | `spark_df.select("col1", "col2")` |
# MAGIC > | Filter | `df[df.col > val]` | `spark_df.filter(spark_df.col > val)` |
# MAGIC > | GroupBy | `df.groupby("col")["target"].mean()` | `spark_df.groupBy("col").agg(avg("target").alias(...))` |
# MAGIC > | Sort | `df.sort_values("col", ascending=False)` | `spark_df.orderBy("col", ascending=False)` |
