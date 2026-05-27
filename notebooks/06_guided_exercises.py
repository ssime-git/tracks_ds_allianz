# Databricks notebook source
# MAGIC %md
# MAGIC # 06 — Guided Exercises
# MAGIC
# MAGIC **Goal:** apply everything from this week's notebooks in a single connected practice session — from exploration to interpretation.
# MAGIC
# MAGIC > This session does not introduce new concepts. It is a practice run using the `insurance` dataset.
# MAGIC > You will move from exploration → filtering → aggregation → interpretation, choosing the right tool (pandas, Spark, or SQL) for each step.
# MAGIC >
# MAGIC > **Dataset reminder:**
# MAGIC > - 420 rows, 7 columns: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, `charges`
# MAGIC > - `charges` = annual medical costs — this is the variable we want to understand
# MAGIC >
# MAGIC > Work through each exercise. If you are stuck, use the hint first before revealing the solution.

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import avg, count

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")
spark_df = spark.read.csv("/FileStore/tables/insurance.csv", header=True, inferSchema=True)
spark_df.createOrReplaceTempView("insurance")

print("Data loaded. Rows:", len(df))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise 1 — Explore the Dataset
# MAGIC
# MAGIC > Before any analysis, take stock of what you have.
# MAGIC > Run the cells below and answer the questions.

# COMMAND ----------

df.head()

# COMMAND ----------

df.info()

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** How many rows does the dataset have? Confirm using `len(df)`.
# MAGIC >
# MAGIC > **(b)** Which column would you use as the analysis target (the thing you want to explain)?
# MAGIC >
# MAGIC > **(c)** Name two columns that could be used to segment the population.
# MAGIC >
# MAGIC > **(d)** Look at the `describe()` output. What is the mean value of `charges`? What is the maximum?

# COMMAND ----------

# (a) — confirm row count
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
len(df)   # Expected: 420</code></pre>
<p>(b) Target column: <code>charges</code> — it is the numeric outcome we want to understand.</p>
<p>(c) Segmentation candidates: <code>smoker</code>, <code>region</code>, <code>sex</code>, <code>age</code>.</p>
<p>(d) Read the <code>mean</code> and <code>max</code> rows from the <code>describe()</code> output for <code>charges</code>.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Exploration must produce a concrete check, not just display a table. Always note row count, column names, and the range of your target variable.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise 2 — Filter with pandas
# MAGIC
# MAGIC > You have already seen two filter examples:
# MAGIC >
# MAGIC > ```python
# MAGIC > df[df["age"] > 50].head()       # rows where age > 50
# MAGIC > df[df["smoker"] == "yes"].head() # rows where smoker is "yes"
# MAGIC > ```

# COMMAND ----------

df[df["age"] > 50].head()

# COMMAND ----------

df[df["smoker"] == "yes"].head()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Write a filter that shows people with `bmi > 30`. Use `.head()` to preview.
# MAGIC >
# MAGIC > **(b)** How many rows have `bmi > 30`? Use `len(...)` around your filter.
# MAGIC >
# MAGIC > **(c)** Write a filter that shows smokers older than 50. Combine two conditions with `&`.
# MAGIC > Remember: each condition must be in its own parentheses.

# COMMAND ----------

# (a) — bmi > 30 preview
# Insert your code here

# COMMAND ----------

# (b) — count rows with bmi > 30
# Insert your code here

# COMMAND ----------

# (c) — smokers older than 50
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
df[df["bmi"] > 30].head()

# (b)
len(df[df["bmi"] > 30])

# (c)
df[(df["smoker"] == "yes") &amp; (df["age"] > 50)].head()</code></pre>
<p>For (c): each condition needs its own parentheses. Without them, Python raises a TypeError about operator precedence.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Read every filter as a business sentence: "show me people where BMI is above 30 and who smoke". If the sentence makes sense, the code is probably right.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise 3 — Aggregate with pandas
# MAGIC
# MAGIC > You have seen how to compute average charges by region:
# MAGIC > ```python
# MAGIC > df.groupby("region")["charges"].mean()
# MAGIC > ```

# COMMAND ----------

df.groupby("region")["charges"].mean().sort_values(ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Compute the average `charges` by `smoker` status. Which group has higher charges?
# MAGIC >
# MAGIC > **(b)** Compute the average `charges` by `sex`. Is the difference large or small?
# MAGIC >
# MAGIC > **(c)** Compute both the average **and** the count of rows by `smoker`. Use `.agg(["mean", "count"])`.
# MAGIC > Interpret: does the group size affect your confidence in the comparison?

# COMMAND ----------

# (a) — avg charges by smoker
# Insert your code here

# COMMAND ----------

# (b) — avg charges by sex
# Insert your code here

# COMMAND ----------

# (c) — avg AND count by smoker
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
df.groupby("smoker")["charges"].mean().sort_values(ascending=False)

# (b)
df.groupby("sex")["charges"].mean().sort_values(ascending=False)

# (c)
df.groupby("smoker")["charges"].agg(["mean", "count"])</code></pre>
<p>(c) Smokers have much higher average charges. The count shows the two groups are not equal in size — always check group size before drawing conclusions.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 An average without a group size can be misleading. Always check <code>count</code> alongside <code>mean</code> — a mean based on 5 rows is very different from one based on 200.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise 4 — Translate to Spark
# MAGIC
# MAGIC > The same three operations in Spark:

# COMMAND ----------

display(spark_df.select("age", "smoker", "charges"))

# COMMAND ----------

display(spark_df.filter(spark_df.bmi > 30))

# COMMAND ----------

display(spark_df.groupBy("smoker").agg(avg("charges").alias("avg_charges")))

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Replace `"smoker"` in the `groupBy` with `"region"`. Display the result.
# MAGIC >
# MAGIC > **(b)** Filter Spark to keep only smokers (`smoker == "yes"`), then compute average `charges` by `region`. Chain `.filter(...)` before `.groupBy(...)`.
# MAGIC >
# MAGIC > **(c)** Add a row count alongside the average using `count("charges").alias("n")` as a second argument inside `.agg(...)`.

# COMMAND ----------

# (a) — groupBy region
# Insert your code here

# COMMAND ----------

# (b) — filter smokers then groupBy region
# Insert your code here

# COMMAND ----------

# (c) — avg AND count in one agg
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
display(spark_df.groupBy("region").agg(avg("charges").alias("avg_charges")))

# (b)
display(
    spark_df
    .filter(spark_df.smoker == "yes")
    .groupBy("region")
    .agg(avg("charges").alias("avg_charges"))
)

# (c)
display(
    spark_df
    .groupBy("smoker")
    .agg(
        avg("charges").alias("avg_charges"),
        count("charges").alias("n")
    )
)</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 You can chain Spark operations: <code>.filter(...).groupBy(...).agg(...)</code>. Each step returns a new DataFrame — nothing is modified in place.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Exercise 5 — SQL
# MAGIC
# MAGIC > Rewrite the same analysis in SQL. The view `insurance` is already registered from the setup cell.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        AVG(charges) AS avg_charges,
# MAGIC        COUNT(*) AS n
# MAGIC FROM insurance
# MAGIC GROUP BY smoker
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Rewrite the query to group by `region` instead of `smoker`.
# MAGIC >
# MAGIC > **(b)** Add a `WHERE smoker = 'yes'` clause to see average charges by region for smokers only.
# MAGIC >
# MAGIC > **(c)** Remove the `WHERE` clause but keep the `GROUP BY region`. Compare this result with (b). What does the difference tell you?

# COMMAND ----------

-- (a) — group by region
-- Insert your query here

# COMMAND ----------

-- (b) — smokers only, group by region
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
GROUP BY region
ORDER BY avg_charges DESC

-- (b)
SELECT region,
       AVG(charges) AS avg_charges,
       COUNT(*) AS n
FROM insurance
WHERE smoker = 'yes'
GROUP BY region
ORDER BY avg_charges DESC</code></pre>
<p>(c) Comparing (a) and (b): when filtered to smokers only, all regions show higher averages — the smoker effect dominates the regional variation.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 SQL is often the most readable format for sharing analysis results with business stakeholders — it reads almost like plain English.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Final Challenge — From Exploration to Interpretation
# MAGIC
# MAGIC > **Business question:** which segment is associated with the highest medical charges?
# MAGIC >
# MAGIC > Use the tools you have available — pandas, Spark, or SQL. There is no single right answer.
# MAGIC > The goal is to produce a number and then write a sentence that explains it.

# COMMAND ----------

# Starter code: cross smoker status and age segment
analysis = (
    df
    .assign(age_segment=pd.cut(df["age"], bins=[0, 30, 50, 100], labels=["<30", "30-50", ">50"]))
    .groupby(["smoker", "age_segment"], observed=True)["charges"]
    .agg(["mean", "count"])
    .sort_values("mean", ascending=False)
)

analysis

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell above. Identify the top 3 segments by average charges.
# MAGIC >
# MAGIC > **(b)** Write a query (pandas, Spark, or SQL) that answers the same question using only `smoker` and `region` as dimensions (no age segmentation).
# MAGIC >
# MAGIC > **(c)** Write a 2-sentence interpretation:
# MAGIC >> Sentence 1: the segment with the highest average charges is ...
# MAGIC >> Sentence 2: this analysis is descriptive — it does not prove that ... causes ...

# COMMAND ----------

# (b) — your analysis using smoker and region
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
<pre><code class="language-python"># (b) — pandas
df.groupby(["smoker", "region"])["charges"].agg(["mean", "count"]).sort_values("mean", ascending=False)</code></pre>
<pre><code class="language-sql">-- (b) — SQL equivalent
SELECT smoker, region,
       AVG(charges) AS avg_charges,
       COUNT(*) AS n
FROM insurance
GROUP BY smoker, region
ORDER BY avg_charges DESC</code></pre>
<p>(c) Example interpretation: the segment with the highest average charges is smokers aged over 50, with an average above the overall mean. This analysis is descriptive — it does not prove that smoking <em>causes</em> higher charges, only that the two are associated in this dataset.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Always distinguish observation from causation. A groupby result shows association — not proof of cause. A well-written conclusion always mentions what was measured, the segment, and a limitation.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this session you practiced the full analytical workflow on a single dataset:
# MAGIC >
# MAGIC >> * **Explore** — `df.head()`, `df.info()`, `df.describe()`, `len(df)` to understand shape and range before touching the data.
# MAGIC >> * **Filter** — `df[df.col > val]` in pandas; `.filter(spark_df.col > val)` in Spark; `WHERE col > val` in SQL.
# MAGIC >> * **Aggregate** — `df.groupby("col")["target"].agg(["mean", "count"])` in pandas; `.groupBy().agg(avg(...), count(...))` in Spark; `GROUP BY col` in SQL.
# MAGIC >> * **Interpret** — every result needs a sentence: name the metric, name the segment, state the limitation.
# MAGIC >
# MAGIC > The three tools are interchangeable for aggregation — choose whichever is most readable for your audience.
