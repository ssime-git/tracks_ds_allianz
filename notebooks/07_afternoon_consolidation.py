# Databricks notebook source
# MAGIC %md
# MAGIC # 07 — Afternoon Session 1: Guided Consolidation
# MAGIC
# MAGIC **Goal:** repeat the key gestures from this morning with a little less guidance — but still with starter code and hidden corrections.
# MAGIC
# MAGIC > This session is a stepping stone between the morning tutorials and the afternoon case study.
# MAGIC > You will:
# MAGIC >
# MAGIC > 1. Control the table before any analysis
# MAGIC > 2. Filter a simple segment and store it
# MAGIC > 3. Filter a combined segment
# MAGIC > 4. Aggregate with pandas
# MAGIC > 5. Sort and read the result
# MAGIC > 6. Repeat in Spark
# MAGIC > 7. Repeat in SQL
# MAGIC > 8. Write a business sentence
# MAGIC >
# MAGIC > At each step: fill in the `...` placeholder, then check your result before revealing the solution.

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import avg, count

df = pd.read_csv("/dbfs/FileStore/tables/insurance.csv")

spark_df = spark.read.csv(
    "/FileStore/tables/insurance.csv",
    header=True,
    inferSchema=True
)

spark_df.createOrReplaceTempView("insurance")

print("Rows loaded:", len(df))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 1 — Check the Table Before Analysing
# MAGIC
# MAGIC > A reliable analysis starts with verifying that the data loaded correctly.
# MAGIC > Do not skip this — a silent loading error can corrupt all downstream results.
# MAGIC >
# MAGIC > Run these four commands one by one and answer the questions below:
# MAGIC >
# MAGIC > ```python
# MAGIC > df.head()      # first 5 rows
# MAGIC > df.shape       # (rows, columns)
# MAGIC > df.columns     # column names
# MAGIC > df.describe()  # numeric summary statistics
# MAGIC > ```

# COMMAND ----------

df.head()

# COMMAND ----------

df.shape

# COMMAND ----------

df.columns

# COMMAND ----------

df.describe()

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** What is the row count? (It should be 420.)
# MAGIC >
# MAGIC > **(b)** Which column is the analysis target — the quantity you want to explain or predict?
# MAGIC >
# MAGIC > **(c)** Which column indicates smoker status? Which column indicates medical cost?
# MAGIC >
# MAGIC > Answer mentally, then check below.

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
<p>(a) Row count: <code>df.shape[0]</code> → 420.</p>
<p>(b) Analysis target: <code>charges</code> — annual medical costs, the outcome we want to understand.</p>
<p>(c) Smoker status: <code>smoker</code> (values: "yes" / "no"). Medical cost: <code>charges</code>.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: naming the target column before you start filtering prevents working on the wrong variable. Always identify your outcome variable first.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 — Filter a Simple Segment
# MAGIC
# MAGIC > Filtering and storing the result in a variable lets you reuse it later — without repeating the filter every time.
# MAGIC >
# MAGIC > Example: extract all smokers and check how many there are.
# MAGIC > ```python
# MAGIC > smokers = df[df["smoker"] == "yes"]
# MAGIC > len(smokers)
# MAGIC > ```

# COMMAND ----------

smokers = df[df["smoker"] == "yes"]
len(smokers)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Create a table `older_than_50` that keeps only people older than 50. Preview it with `.head()`.
# MAGIC >
# MAGIC > **(b)** How many rows does `older_than_50` contain? What percentage of the total is that?

# COMMAND ----------

# (a) — filter age > 50
older_than_50 = df[df["age"] > ...]

older_than_50.head()

# COMMAND ----------

# (b) — count and percentage
len(older_than_50)

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
older_than_50 = df[df["age"] > 50]
older_than_50.head()

# (b)
print(len(older_than_50))
print(f"{len(older_than_50) / len(df) * 100:.1f}%")</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: store filtered subsets in named variables. <code>older_than_50 = df[df["age"] > 50]</code> is much more readable than repeating the filter inline every time.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 — Filter a Combined Segment
# MAGIC
# MAGIC > To combine two conditions in pandas, use `&` (and) or `|` (or).
# MAGIC > Each condition must be in its own parentheses:
# MAGIC >
# MAGIC > ```python
# MAGIC > older_smokers = df[(df["age"] > 50) & (df["smoker"] == "yes")]
# MAGIC > ```
# MAGIC >
# MAGIC > Without parentheses, Python misinterprets operator precedence and raises a confusing error.

# COMMAND ----------

older_smokers = df[(df["age"] > 50) & (df["smoker"] == "yes")]
older_smokers.head()

# COMMAND ----------

len(older_smokers)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Create a table `high_bmi_smokers` that keeps rows where `bmi > 30` **and** `smoker == "yes"`. Preview and count.
# MAGIC >
# MAGIC > **(b)** Create a table `non_smokers_northeast` that keeps non-smokers in the `northeast` region.

# COMMAND ----------

# (a) — bmi > 30 and smoker
high_bmi_smokers = df[(df["bmi"] > ...) & (df["smoker"] == ...)]
high_bmi_smokers.head()

# COMMAND ----------

len(high_bmi_smokers)

# COMMAND ----------

# (b) — non-smokers in northeast
non_smokers_northeast = df[(df["smoker"] == ...) & (df["region"] == ...)]
len(non_smokers_northeast)

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
high_bmi_smokers = df[(df["bmi"] > 30) &amp; (df["smoker"] == "yes")]
high_bmi_smokers.head()
len(high_bmi_smokers)

# (b)
non_smokers_northeast = df[(df["smoker"] == "no") &amp; (df["region"] == "northeast")]
len(non_smokers_northeast)</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: each condition must be in its own parentheses when using <code>&</code> or <code>|</code>. Missing parentheses is the most common filter error in pandas.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4 — Aggregate with pandas
# MAGIC
# MAGIC > Now compute average charges by group. A sorted result is easier to read than an unsorted one.
# MAGIC >
# MAGIC > ```python
# MAGIC > df.groupby("smoker")["charges"].mean().sort_values(ascending=False)
# MAGIC > ```

# COMMAND ----------

df.groupby("smoker")["charges"].mean().sort_values(ascending=False)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Compute average `charges` by `region`, sorted highest to lowest.
# MAGIC >
# MAGIC > **(b)** Add a row count alongside the mean. Use `.agg(["mean", "count"])` instead of `.mean()`.

# COMMAND ----------

# (a) — avg charges by region, sorted
df.groupby(...)["charges"].mean().sort_values(ascending=False)

# COMMAND ----------

# (b) — mean AND count by region
df.groupby("region")["charges"].agg(...)

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
df.groupby("region")["charges"].mean().sort_values(ascending=False)

# (b)
df.groupby("region")["charges"].agg(["mean", "count"])</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: after every grouped aggregation, look for the highest and lowest group — and check group size. A mean based on 5 rows is unreliable.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5 — Sort and Store the Result
# MAGIC
# MAGIC > Storing the aggregated result in a named variable lets you reference it later without recomputing.

# COMMAND ----------

avg_by_region = (
    df
    .groupby("region")["charges"]
    .mean()
    .sort_values(ascending=False)
)

avg_by_region

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Create `avg_by_smoker` — average `charges` by `smoker`, sorted highest to lowest.
# MAGIC >
# MAGIC > **(b)** What is the ratio between the highest and lowest smoker group? Compute it using the variable.
# MAGIC > Hint: `avg_by_smoker.iloc[0] / avg_by_smoker.iloc[-1]`

# COMMAND ----------

# (a)
avg_by_smoker = (
    df
    .groupby(...)["charges"]
    .mean()
    .sort_values(ascending=False)
)

avg_by_smoker

# COMMAND ----------

# (b) — ratio highest / lowest
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
avg_by_smoker = (
    df
    .groupby("smoker")["charges"]
    .mean()
    .sort_values(ascending=False)
)

# (b)
avg_by_smoker.iloc[0] / avg_by_smoker.iloc[-1]
# Smokers have roughly 3-4x higher average charges than non-smokers in this dataset</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: store aggregation results in variables with descriptive names. <code>avg_by_smoker</code> communicates intent; <code>result</code> or <code>x</code> does not.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6 — Repeat in Spark
# MAGIC
# MAGIC > The same analysis in Spark. The logic is identical; only the syntax changes.

# COMMAND ----------

display(
    spark_df
    .groupBy("smoker")
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Replace `"smoker"` with `"region"`. Display the result.
# MAGIC >
# MAGIC > **(b)** Add `.orderBy("avg_charges", ascending=False)` after `.agg(...)` to sort the Spark result.

# COMMAND ----------

# (a) — groupBy region
display(
    spark_df
    .groupBy(...)
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
)

# COMMAND ----------

# (b) — add orderBy
display(
    spark_df
    .groupBy("region")
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
    ...
)

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
display(
    spark_df
    .groupBy("region")
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
)

# (b)
display(
    spark_df
    .groupBy("region")
    .agg(
        count("*").alias("row_count"),
        avg("charges").alias("avg_charges")
    )
    .orderBy("avg_charges", ascending=False)
)</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Comparing the same result in pandas and Spark helps you separate the business logic from the syntax. The numbers should match — if they don't, check for a loading issue.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 7 — Repeat in SQL
# MAGIC
# MAGIC > The same analysis one more time, in SQL.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        COUNT(*) AS row_count,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance
# MAGIC GROUP BY smoker
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Rewrite the query to group by `region` instead of `smoker`.
# MAGIC >
# MAGIC > **(b)** Add a `WHERE age > 40` clause. Does the ranking of regions change?

# COMMAND ----------

-- (a) — group by region
-- Insert your query here

# COMMAND ----------

-- (b) — add WHERE age > 40
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
       COUNT(*) AS row_count,
       AVG(charges) AS avg_charges
FROM insurance
GROUP BY region
ORDER BY avg_charges DESC

-- (b)
SELECT region,
       COUNT(*) AS row_count,
       AVG(charges) AS avg_charges
FROM insurance
WHERE age > 40
GROUP BY region
ORDER BY avg_charges DESC</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Comparing pandas, Spark and SQL on the same question shows that the three tools share the same logic: filter → group → aggregate → sort. The syntax differs; the thinking is identical.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 8 — Write a Business Sentence
# MAGIC
# MAGIC > Every analysis should end with a plain-language conclusion — one sentence that names the metric, the segment, and the limitation.
# MAGIC >
# MAGIC > Template:
# MAGIC >> In this dataset, the segment with the highest average charges is **[segment]**, with an average of approximately **[value]**. This is a descriptive observation — it does not prove that **[variable]** causes higher charges.

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Complete the template above using the results from Steps 4–7. Write your sentence in the cell below.
# MAGIC >
# MAGIC > **(b)** Read it aloud. Does it make sense to someone who has not seen the code?

# COMMAND ----------

# MAGIC %md
# MAGIC > *Write your business sentence here (double-click to edit this Markdown cell):*
# MAGIC >
# MAGIC > In this dataset, the segment with the highest average charges is ...

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
<p>Example: In this dataset, smokers have average medical charges roughly 3–4 times higher than non-smokers. This is a descriptive observation on a synthetic sample of 420 rows — it does not prove that smoking <em>causes</em> higher charges.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always end an analysis with a plain sentence. If you cannot summarise the result in one sentence, you have not yet understood it.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this session you consolidated the key gestures from the morning — without a blank page, but with less hand-holding:
# MAGIC >
# MAGIC >> * **Control** the table first: `df.head()`, `df.shape`, `df.describe()`.
# MAGIC >> * **Filter** a segment: `df[df.col > val]` — store the result in a named variable.
# MAGIC >> * **Combine** conditions: `df[(cond1) & (cond2)]` — parentheses are mandatory.
# MAGIC >> * **Aggregate**: `df.groupby("col")["target"].mean().sort_values(ascending=False)`.
# MAGIC >> * **Spark equivalent**: `spark_df.groupBy(...).agg(avg(...).alias(...)).orderBy(...)`.
# MAGIC >> * **SQL equivalent**: `SELECT col, AVG(target) FROM view GROUP BY col ORDER BY ...`.
# MAGIC >> * **Interpret**: one sentence — name the metric, the segment, and the limitation.
# MAGIC >
# MAGIC > The same analytical logic runs in all three tools. Choosing between them is a matter of context and readability.
