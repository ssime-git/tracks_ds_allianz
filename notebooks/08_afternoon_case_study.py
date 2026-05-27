# Databricks notebook source
# MAGIC %md
# MAGIC # 08 — Afternoon Session 2: Business Case Study
# MAGIC
# MAGIC **Goal:** answer a business question end-to-end — from data preparation to written interpretation — with a complete, guided workflow.
# MAGIC
# MAGIC > **Business question:**
# MAGIC >
# MAGIC >> Which segments are associated with the highest medical charges?
# MAGIC >
# MAGIC > This notebook is more autonomous than the previous one. Steps are still clearly marked, but you write more of the code yourself.
# MAGIC >
# MAGIC > You will:
# MAGIC > 1. Prepare a segmentation variable using `pd.cut()`
# MAGIC > 2. Analyse charges by smoker status
# MAGIC > 3. Analyse charges by age segment
# MAGIC > 4. Cross two dimensions (smoker × age segment)
# MAGIC > 5. Repeat the cross-analysis in SQL
# MAGIC > 6. Write a structured business conclusion

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
# MAGIC ## Step 1 — Prepare a Segmentation Variable
# MAGIC
# MAGIC > A continuous numeric variable like `age` is hard to aggregate directly — you get a row per unique value.
# MAGIC > **Binning** converts it into ordered categories (segments), which are much easier to group and compare.
# MAGIC >
# MAGIC > pandas provides `pd.cut()` for this:
# MAGIC >
# MAGIC > ```python
# MAGIC > pd.cut(
# MAGIC >     series,          # the column to bin
# MAGIC >     bins=[0, 30, 50, 100],   # bin boundaries (exclusive left, inclusive right)
# MAGIC >     labels=["<30", "30-50", ">50"]  # label for each bin
# MAGIC > )
# MAGIC > ```
# MAGIC >
# MAGIC > - `bins=[0, 30, 50, 100]` creates three intervals: (0, 30], (30, 50], (50, 100]
# MAGIC > - `labels` must have exactly one fewer element than `bins` — one label per interval
# MAGIC > - Use `.assign(...)` to add the new column without modifying the original DataFrame
# MAGIC >
# MAGIC > In SAS this would be a DATA step with `IF age <= 30 THEN age_segment = "<30"; ...`

# COMMAND ----------

df_with_segments = df.assign(
    age_segment=pd.cut(
        df["age"],
        bins=[0, 30, 50, 100],
        labels=["<30", "30-50", ">50"]
    )
)

df_with_segments[["age", "age_segment", "smoker", "charges"]].head(10)

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell above and verify that the `age_segment` column is populated correctly.
# MAGIC > Check: a row with `age = 25` should have segment `<30`; `age = 45` should be `30-50`.
# MAGIC >
# MAGIC > **(b)** Count the number of rows per `age_segment` to check the distribution. Use `df_with_segments["age_segment"].value_counts()`.
# MAGIC >
# MAGIC > **(c)** What would you change if you wanted four segments instead of three? Think about the `bins` and `labels` parameters before looking at the solution.

# COMMAND ----------

# (b) — count rows per age_segment
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
df_with_segments["age_segment"].value_counts()

# (c) — four segments
df.assign(
    age_segment=pd.cut(
        df["age"],
        bins=[0, 25, 40, 55, 100],
        labels=["<25", "25-40", "40-55", ">55"]
    )
)["age_segment"].value_counts()
# 4 bins boundaries → 3 intervals... wait, 5 boundaries → 4 intervals
# bins has n+1 values for n labels</code></pre>
<p>Key: <code>bins</code> has one more value than <code>labels</code>. For 4 segments: 5 bin boundaries and 4 labels.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: always check the distribution of a new segment with <code>value_counts()</code>. An uneven distribution (e.g., 400 in one bin and 5 in another) makes comparisons unreliable.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 2 — Analysis 1: Charges by Smoker Status
# MAGIC
# MAGIC > Start with the simplest dimension before crossing multiple ones.
# MAGIC > One variable at a time reveals clean, interpretable results.

# COMMAND ----------

analysis_smoker = (
    df_with_segments
    .groupby("smoker")["charges"]
    .mean()
    .sort_values(ascending=False)
)

analysis_smoker

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Run the cell above. Which group has higher average charges?
# MAGIC >
# MAGIC > **(b)** Add a row count alongside the mean. Use `.agg(["mean", "count"])`. Does the count affect how confident you are in the comparison?
# MAGIC >
# MAGIC > **(c)** Write one sentence in the Markdown cell below to summarise what you observe:
# MAGIC >> Average charges are higher for ... than for ...

# COMMAND ----------

# (b) — mean AND count by smoker
# Insert your code here

# COMMAND ----------

# MAGIC %md
# MAGIC > **(c)** Write your sentence here (double-click to edit):
# MAGIC >
# MAGIC > Average charges are higher for ...

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
df_with_segments.groupby("smoker")["charges"].agg(["mean", "count"])</code></pre>
<p>(c) Average charges are higher for smokers than for non-smokers in this dataset.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: start with a simple one-variable analysis before crossing multiple dimensions. A clear single result builds confidence before adding complexity.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 3 — Analysis 2: Charges by Age Segment
# MAGIC
# MAGIC > Now use the `age_segment` column you created in Step 1.
# MAGIC > Note: when grouping by a column created with `pd.cut()`, always add `observed=True` to avoid warnings about unobserved categories.

# COMMAND ----------

analysis_age = (
    df_with_segments
    .groupby("age_segment", observed=True)["charges"]
    .mean()
    .sort_values(ascending=False)
)

analysis_age

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Add a row count alongside the mean. Which age segment has the most rows? Which has the fewest?
# MAGIC >
# MAGIC > **(b)** Create `age_segment_summary` with both `row_count` and `avg_charges` using `.agg(row_count=(..., "size"), avg_charges=(..., "mean"))`. Sort by `avg_charges` descending.

# COMMAND ----------

# (b) — summary with row count and avg charges
age_segment_summary = (
    df_with_segments
    .groupby(..., observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

age_segment_summary

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
<pre><code class="language-python">age_segment_summary = (
    df_with_segments
    .groupby("age_segment", observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

age_segment_summary</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: a mean without a row count can be misleading. Always show both — a high average based on very few rows is much less reliable than one based on 100+ rows.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 4 — Analysis 3: Cross Two Dimensions
# MAGIC
# MAGIC > Crossing two segmentation variables reveals interactions that single-variable analysis misses.
# MAGIC > The question here: is the age effect consistent within smoker groups, and vice versa?
# MAGIC >
# MAGIC > To group by two columns, pass a list: `.groupby(["col1", "col2"], observed=True)`.

# COMMAND ----------

segment_summary = (
    df_with_segments
    .groupby(["smoker", "age_segment"], observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

segment_summary

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Which combination of smoker status and age segment has the highest average charges?
# MAGIC >
# MAGIC > **(b)** Modify the code to replace `age_segment` with `region` in the cross-analysis. Call the result `region_smoker_summary`.
# MAGIC >
# MAGIC > **(c)** As you add more dimensions, watch the `row_count` column. At what point does the group size become too small to be meaningful?

# COMMAND ----------

# (b) — cross smoker × region
region_smoker_summary = (
    df_with_segments
    .groupby(["smoker", ...], observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

region_smoker_summary

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
<pre><code class="language-python">region_smoker_summary = (
    df_with_segments
    .groupby(["smoker", "region"], observed=True)
    .agg(
        row_count=("charges", "size"),
        avg_charges=("charges", "mean")
    )
    .sort_values("avg_charges", ascending=False)
)

region_smoker_summary</code></pre>
<p>(c) As a rough rule of thumb: groups with fewer than 20–30 rows produce averages that are sensitive to individual outliers. Always flag small groups when reporting results.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: the more dimensions you cross, the smaller the groups become. Monitor <code>row_count</code> in every cross-analysis — small groups produce unreliable averages.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 5 — Repeat the Cross-Analysis in SQL
# MAGIC
# MAGIC > SQL reads naturally for cross-segment analysis — it is often easier to share with non-technical stakeholders.
# MAGIC > First, register the DataFrame with the `age_segment` column as a new SQL view.

# COMMAND ----------

spark_df_with_segments = spark.createDataFrame(df_with_segments)
spark_df_with_segments.createOrReplaceTempView("insurance_segments")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT smoker,
# MAGIC        age_segment,
# MAGIC        COUNT(*) AS row_count,
# MAGIC        AVG(charges) AS avg_charges
# MAGIC FROM insurance_segments
# MAGIC GROUP BY smoker, age_segment
# MAGIC ORDER BY avg_charges DESC

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Modify the query above to cross `smoker` and `region` instead of `smoker` and `age_segment`.
# MAGIC >
# MAGIC > **(b)** Add a `WHERE smoker = 'yes'` clause. Does the ranking of regions change for smokers only?

# COMMAND ----------

-- (a) — cross smoker × region in SQL
-- Insert your query here

# COMMAND ----------

-- (b) — smokers only, by region
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
       region,
       COUNT(*) AS row_count,
       AVG(charges) AS avg_charges
FROM insurance_segments
GROUP BY smoker, region
ORDER BY avg_charges DESC

-- (b)
SELECT region,
       COUNT(*) AS row_count,
       AVG(charges) AS avg_charges
FROM insurance_segments
WHERE smoker = 'yes'
GROUP BY region
ORDER BY avg_charges DESC</code></pre>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: SQL is the most readable format for cross-segment analysis when sharing results with business stakeholders. The query reads almost like a plain English question.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Step 6 — Business Conclusion
# MAGIC
# MAGIC > A good analytical conclusion has three parts:
# MAGIC >
# MAGIC > 1. **The finding** — name the segment, the metric, and the value.
# MAGIC > 2. **The basis** — state what the result is based on (which measure, which data).
# MAGIC > 3. **The limitation** — acknowledge what the analysis does NOT prove.
# MAGIC >
# MAGIC > Template:
# MAGIC >> 1. The segment with the highest average charges is **[segment]**, with an average of approximately **[value]**.
# MAGIC >> 2. This result is based on **average `charges`** across **[N] rows** in the synthetic insurance dataset.
# MAGIC >> 3. Limitation: this analysis is descriptive — it shows an association in the data, but does not prove that **[variable]** causes higher charges.

# COMMAND ----------

# MAGIC %md
# MAGIC > **(a)** Using the results from Steps 2–4, fill in the template above. Write your conclusion in the Markdown cell below.
# MAGIC >
# MAGIC > **(b)** Read it aloud. Does it make sense without seeing the code?

# COMMAND ----------

# MAGIC %md
# MAGIC > *Write your conclusion here (double-click to edit this cell):*
# MAGIC >
# MAGIC > 1. The segment with the highest average charges is ...
# MAGIC > 2. This result is based on ...
# MAGIC > 3. Limitation: this analysis is descriptive and does not prove that ...

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
<p>1. The segment with the highest average charges is smokers aged over 50, who show average annual charges well above all other groups.</p>
<p>2. This result is based on average <code>charges</code> computed across 420 rows in a synthetic insurance dataset, grouped by smoker status and age segment.</p>
<p>3. Limitation: this analysis is descriptive — it shows an association between smoker status, age, and charges in this dataset, but does not prove that smoking or age <em>causes</em> higher medical costs.</p>
</div>
</details>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC > <div class="alert alert-info">💡 Key rule: a conclusion must always mention the measure (average charges), the segment (smokers over 50), and the limitation (descriptive, not causal). Without the limitation, the finding can be misunderstood.</div>

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary
# MAGIC
# MAGIC > In this case study you completed an end-to-end analytical workflow:
# MAGIC >
# MAGIC >> * **`pd.cut(series, bins=[...], labels=[...])`** — bin a continuous variable into labelled categories. Number of labels = number of bins − 1.
# MAGIC >> * **`.assign(new_col=...)`** — add a derived column without modifying the original DataFrame.
# MAGIC >> * **`.groupby("col", observed=True)`** — use `observed=True` when grouping by a categorical column created with `pd.cut()`.
# MAGIC >> * **`.agg(name=("col", "func"))`** — named aggregation syntax: produces readable column names directly.
# MAGIC >> * **`spark.createDataFrame(pandas_df)`** — convert a pandas DataFrame to Spark, e.g. to register an enriched view for SQL.
# MAGIC >> * **Structured conclusion**: finding → basis → limitation. Always include all three parts.
# MAGIC >
# MAGIC > | Step | Tool | Key method |
# MAGIC > |------|------|------------|
# MAGIC > | Create segment | pandas | `pd.cut()` + `.assign()` |
# MAGIC > | Single-dimension agg | pandas | `.groupby().mean()` |
# MAGIC > | Multi-dimension agg | pandas | `.groupby([...]).agg(...)` |
# MAGIC > | Same in Spark | Spark | `.groupBy().agg(avg(...))` |
# MAGIC > | Same in SQL | SQL | `GROUP BY col1, col2` |
# MAGIC > | Interpret | Written | Finding + Basis + Limitation |
